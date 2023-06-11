from datetime import datetime, timedelta
import json
import random
import sys

from .muscle_groups import *
from .exercises import EXERCISES
from .user_data import TEST_USER, USER_DATA


NUM_SETS_PER_POWER_SET = 3
MACHINE_BOOST_CONSTANT = 1.15
MAX_HISTORY_DAYS = 30                              # max number of days to look back
MAX_MUSCLE_GROUP_NEGLECTEDNESS = 3.0
PRIMARY_WEIGHT_PERCENT = 2 / 3
THIS_POWER_SET_MUSCLE_GROUP_NEGLECTEDNESS = 1 / 3
EARLIER_TODAY_MUSCLE_GROUP_NEGLECTEDNESS = 2 / 3
LAST_VISIT_MUSCLE_GROUP_NEGLECTEDNESS = 1.0
SECONDS_PER_DAY = 3600 * 24


def calculate_exercise_neglectedness(exercise_name, history, now):
    '''Calculates a single score for a specific exercise's neglectedness.
    This is used to promote variety.'''
    num_days_since_exercise = MAX_HISTORY_DAYS
    for timestamp, exercise, _ in history:
        if exercise == exercise_name:
            num_days_since_exercise = round((now - timestamp).total_seconds() / SECONDS_PER_DAY)
            break

    return 1.0 + num_days_since_exercise / MAX_HISTORY_DAYS / 2


def calculate_average_importance(user_key, muscle_groups):
    '''Calculates a single score for importance based on the `muscle_groups` involved in an
    exercise.'''
    average_importance = 0.0
    for muscle_group in muscle_groups:
        average_importance += USER_DATA[user_key]['muscle_group_importance'].get(muscle_group, 1.0)

    average_importance /= len(muscle_groups)
    return average_importance


def calculate_average_muscle_group_neglectedness(muscle_groups, partitions, now):
    '''Calculates a single score for neglectedness based on the `muscle_groups` involved in an
    exercise.'''
    this_power_set, earlier_today, last_visit, before_last_visit = partitions
    average_neglectedness = 0.0
    for muscle_group in muscle_groups:
        if any(muscle_group in EXERCISES[exercise]['primary_muscle_groups']
               for _, exercise, _ in this_power_set):
            neglectedness = THIS_POWER_SET_MUSCLE_GROUP_NEGLECTEDNESS
        elif (any(muscle_group in EXERCISES[exercise]['primary_muscle_groups']
                  for _, exercise, _ in earlier_today)
              or any(muscle_group in EXERCISES[exercise]['secondary_muscle_groups']
                     for _, exercise, _ in this_power_set)):
            neglectedness = EARLIER_TODAY_MUSCLE_GROUP_NEGLECTEDNESS
        elif (any(muscle_group in EXERCISES[exercise]['primary_muscle_groups']
                  for _, exercise, _ in last_visit)
              or any(muscle_group in EXERCISES[exercise]['secondary_muscle_groups']
                     for _, exercise, _ in earlier_today)):
            neglectedness = LAST_VISIT_MUSCLE_GROUP_NEGLECTEDNESS
        else:
            for timestamp, exercise_name, _ in before_last_visit:
                primary_muscle_groups = EXERCISES[exercise_name]['primary_muscle_groups']
                if muscle_group in primary_muscle_groups:
                    num_days = round((now - timestamp).total_seconds() / SECONDS_PER_DAY)
                    neglectedness = min(1 + max(num_days - 2, 0), MAX_MUSCLE_GROUP_NEGLECTEDNESS)
                    break
            else:
                neglectedness = MAX_MUSCLE_GROUP_NEGLECTEDNESS

        average_neglectedness += neglectedness

    average_neglectedness /= len(muscle_groups)
    # TODO: is average neglectedness the best?
    return average_neglectedness


def partition_history(history, now, set_index):
    '''Labels what exercises have been done this power set, earlier today, last exercise, or
    earlier.'''
    this_power_set = history[:set_index]

    try:
        for i, (timestamp, exercise_name, _) in enumerate(history[set_index:]):
            if timestamp != now:
                last_visit = timestamp
                last_visit_index = set_index + i
                break
        else:
            return this_power_set, history[set_index:], [], []

        earlier_today = history[set_index:last_visit_index]
    except Exception:
        earlier_today = []

    try:
        for i, (timestamp, exercise_name, _) in enumerate(history[last_visit_index:]):
            if timestamp != last_visit:
                earlier_index = last_visit_index + i
                break
        else:
            return this_power_set, earlier_today, history[last_visit_index:], []

        last_visit = history[last_visit_index:earlier_index]
    except Exception:
        last_visit = []

    before_last_visit = history[earlier_index:]

    return this_power_set, earlier_today, last_visit, before_last_visit


def get_score(user_key, exercise_name, exercise_details, history, now, set_index):
    '''Scores an exercise in terms of how good of a candidate it is as the next exercise.

    Score is a product of muscle group importance, muscle group neglectedness, exercise
    neglectedness, and machine score.
    '''
    partitions = partition_history(history, now, set_index)

    # Calculate neglectedness of exercise's muscle groups
    primary_neglectedness = calculate_average_muscle_group_neglectedness(
        exercise_details['primary_muscle_groups'], partitions, now)

    # Calculate importance of exercise's muscle groups
    primary_importance = calculate_average_importance(
        user_key, exercise_details['primary_muscle_groups'])

    if len(exercise_details['secondary_muscle_groups']) > 0:
        secondary_neglectedness = calculate_average_muscle_group_neglectedness(
            exercise_details['secondary_muscle_groups'], partitions, now)
        average_neglectedness = (PRIMARY_WEIGHT_PERCENT * primary_neglectedness
                              + (1.0 - PRIMARY_WEIGHT_PERCENT) * secondary_neglectedness)

        secondary_importance = calculate_average_importance(
            user_key, exercise_details['secondary_muscle_groups'])
        average_importance = (PRIMARY_WEIGHT_PERCENT * primary_importance
                              + (1.0 - PRIMARY_WEIGHT_PERCENT) * secondary_importance)
    else:
        average_neglectedness = primary_neglectedness
        average_importance = primary_importance

    # Calculate neglectedness of exercise (higher if it's been longer)
    exercise_neglectedness = calculate_exercise_neglectedness(exercise_name, history, now)

    if len(history) > 0 and len(EXERCISES[history[0][1]]['machines'].intersection(
            exercise_details['machines'])) > 0:
        machine_boost = MACHINE_BOOST_CONSTANT
    else:
        machine_boost = 1
    
    return average_importance * average_neglectedness * exercise_neglectedness * machine_boost


def select_variation(exercise, possible_variations, history):
    '''Selects the least recently used variation, or if not all variations are represented,
    a random selection from those which aren't represented.
    '''
    if len(possible_variations) > 1:
        most_recent_variations = set()
        for _, exercise_name, variation in history:
            if exercise_name == exercise:
                most_recent_variations.add(variation)
                if len(most_recent_variations) == len(possible_variations) - 1:
                    # Found LRU by process of elimination
                    return list(possible_variations - most_recent_variations)[0]

        # Process of elimination didn't yield a single LRU variation, select randomly
        return random.choice(list(possible_variations - most_recent_variations))

    elif len(possible_variations) == 1:
        return variation

    return ''


def get_set(user_key, history, now, set_index, gym):
    '''Computes the single next set to do using a greedy approach.

    We essentially want to pick the best exercise to do next given:
     * history
     * importance of muscle groups
     * what machine we're currently on

    Assumes all machines have availability.

    Because of the multi-factor nature of what the best next exercise is, a simple queue won't work.
    It has to be a system that scores each potential exercise and finds the max for each step.

    Then select a variation.
    '''
    max_score = float('-inf')
    max_score_exercise_name = None
    scores = []
    machines = USER_DATA[user_key]['machines_by_gym'][gym]
    for exercise_name, exercise_details in EXERCISES.items():
        if len(exercise_details['machines'].intersection(machines)) == 0:
            continue

        score = get_score(user_key, exercise_name, exercise_details, history, now, set_index)
        scores.append((round(score, 1), exercise_name))
        if score > max_score:
            max_score = score
            max_score_exercise_name = exercise_name

    scores = [f'{s} {n}' for s, n in scores if s == round(max_score, 1)]

    possible_variations = EXERCISES[max_score_exercise_name].get('variations', [])
    variation = select_variation(max_score_exercise_name, possible_variations, history)

    return max_score_exercise_name, variation


def get_power_set(user_key, history, now, gym):
    '''Computes next power set to assign at `gym` based on history.

    A power set consists of >1 different sets done at least twice.

    Returns human-readable power set.
    '''
    output = ''
    for set_index in range(NUM_SETS_PER_POWER_SET):
        exercise, variation = get_set(user_key, history, now, set_index, gym)
        if variation:
            output += f'\n{exercise} ({variation})'
        else:
            output += f'\n{exercise}'

        # For now, print muscle groups in case there are errors
        output += f'\n  1) {", ".join(EXERCISES[exercise]["primary_muscle_groups"])}'
        if len(EXERCISES[exercise]["secondary_muscle_groups"]) > 0:
            output += f'\n  2) {", ".join(EXERCISES[exercise]["secondary_muscle_groups"])}\n'

        history.insert(0, (now, exercise, variation or ''))
    
    output += '\n'
    return output


def read_history(txt_raw, now):
    '''Reads history as list from CSV file.

    History is an array of (timestamp, set name, variation) tuples.

    Only use history from past month.
    '''
    if '\n' not in txt_raw:
        return []

    return list(
        map(
            lambda tup: (datetime.fromisoformat(tup[0]), tup[1], tup[2]),
            map(
                lambda line: tuple(line.strip().split(',')),
                txt_raw.strip().split('\n')
            )
        )
    )


def write_history(data):
    '''Writes history list to CSV file.

    History is formatted as comma-separated datetime, exercise, variation. E.g.:
    2022-12-23 03:39:00,cable triceps,
    2022-12-23 03:40:00,dumbbell bicep curl,reverse incline
    '''
    return '\n'.join([','.join((str(timestamp), exercise, variation))
        for timestamp, exercise, variation in data])


def get_power_sets(user_key, num_power_sets, gym, input_filename='data.txt',
                   output_filename='data.txt', now=datetime.utcnow()):
    '''Computes next `num_power_sets` to assign at `gym` based on history TXT.
    Updates history and returns human-readable workout plan.
    '''
    output = ''
    with open(input_filename, 'r', encoding='utf-8') as f:
        history = read_history(f.read(), now)
        relevant_history = list(
            filter(
                lambda tup: tup[0] > now - timedelta(days=10),
                history
            )
        )
        archive = history[len(relevant_history):]
        for _ in range(num_power_sets):
            power_set = get_power_set(user_key, relevant_history, now, gym)
            output += '\n' + power_set

    if output_filename:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.seek(0)
            f.write(write_history(relevant_history + archive))

    return output.strip()


if __name__ == '__main__':
    get_power_sets(TEST_USER, int(sys.argv[1]), sys.argv[2])
