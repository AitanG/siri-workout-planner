from datetime import datetime, timedelta
import itertools
import os
import re
import time
import uuid

from .exercises import *
from .get_power_sets import *
from .muscle_groups import *
from .user_data import GYM_LOCAL, TEST_USER, USER_DATA


def test_exercise_distribution_over_single_workout():
    # Create empty history file
    filename = str(uuid.uuid4())
    open(filename, 'a').close()

    machines = USER_DATA[TEST_USER]['machines_by_gym'][GYM_LOCAL]
    num_possible_exercises = 0
    for workout_name, workout_details in EXERCISES.items():
        for machine in workout_details['machines']:
            if machine in machines:
                num_possible_exercises += 1
                break

    num_power_sets = num_possible_exercises // NUM_SETS_PER_POWER_SET + 1
    get_power_sets(TEST_USER,
                   num_power_sets=num_power_sets,
                   gym=GYM_LOCAL,
                   input_filename=filename,
                   output_filename=filename,
                   now=datetime.utcnow())

    now = datetime.utcnow()
    with open(filename, 'r', encoding='utf-8') as f:
        history = read_history(f.read(), now)

    os.remove(filename)

    # Assert that workout planning gives roughly uniform representation to all workouts within a given workout
    num_unique_exercises_done = len(set(map(lambda entry: entry[1], history)))
    assert num_unique_exercises_done > num_possible_exercises * 0.9 and num_unique_exercises_done < num_possible_exercises


def test_exercise_distribution_over_month():
    # Create empty history file
    filename = str(uuid.uuid4())
    open(filename, 'a').close()

    machines = USER_DATA[TEST_USER]['machines_by_gym'][GYM_LOCAL]
    num_possible_exercises = 0
    for workout_name, workout_details in EXERCISES.items():
        for machine in workout_details['machines']:
            if machine in machines:
                num_possible_exercises += 1
                break

    num_workouts = num_possible_exercises // (NUM_SETS_PER_POWER_SET * 2) + 1

    now = datetime.utcnow()
    for _ in range(num_workouts):
        get_power_sets(TEST_USER,
                       num_power_sets=2,
                       gym=GYM_LOCAL,
                       input_filename=filename,
                       output_filename=filename,
                       now=now)

        now += timedelta(days=1, seconds=1)

    with open(filename, 'r', encoding='utf-8') as f:
        history = read_history(f.read(), now)

    # Assert that workout planning gives roughly but not quite uniform representation to all workouts over time
    num_unique_exercises_done = len(set(map(lambda entry: entry[1], history)))
    assert num_unique_exercises_done > num_possible_exercises * 0.75 and num_unique_exercises_done < num_possible_exercises * 0.9

    for _ in range(num_workouts * 3):
        get_power_sets(TEST_USER,
                       num_power_sets=3,
                       gym=GYM_LOCAL,
                       input_filename=filename,
                       output_filename=filename,
                       now=now)

        now += timedelta(days=1, seconds=1)

    with open(filename, 'r', encoding='utf-8') as f:
        history = read_history(f.read(), now)

    os.remove(filename)

    # Assert that over time, all workouts eventually get done
    num_unique_exercises_done = len(set(map(lambda entry: entry[1], history)))
    assert num_unique_exercises_done == num_possible_exercises


def test_muscle_group_distribution():
    # Create empty history file
    filename = str(uuid.uuid4())
    open(filename, 'a').close()

    now = datetime.utcnow()

    muscle_group_utilization = {muscle_group: 0.0 for muscle_group in MUSCLE_GROUPS}

    # Remove cardio and forearms from calculation because these are intentionally excluded from workout plans
    del muscle_group_utilization[CARDIO]
    del muscle_group_utilization[FOREARMS]

    for _ in range(50):
        output = get_power_sets(TEST_USER,
                                num_power_sets=2,
                                gym=GYM_LOCAL,
                                input_filename=filename,
                                output_filename=filename,
                                now=now)

        # Add to muscle group utilization score for each exercise (average, secondaries count a third as much)
        for primaries, secondaries in itertools.product(re.findall(r'  1\) (.+)', output), re.findall(r'  2\) (.+)', output)):
            primaries = primaries.split(', ')
            secondaries = secondaries.split(', ')
            total_num_groups_used = len(primaries) + 1 / 3 * len(secondaries)
            for primary in primaries:
                muscle_group_utilization[primary] += 1.0 / total_num_groups_used

            for secondary in secondaries:
                muscle_group_utilization[secondary] += 1 / 3 / total_num_groups_used

        now += timedelta(days=1, seconds=1)

    os.remove(filename)

    muscle_group_utilization_list = [(utilization, group) for group, utilization in muscle_group_utilization.items()]

    # For debugging
    for utilization, group in sorted(muscle_group_utilization_list):
        print(round(utilization, 1), group)

    # Assert some reasonable uniformity in muscle groups by comparing the min and max
    assert max(muscle_group_utilization_list)[0] < 3.5 * min(muscle_group_utilization_list)[0]


def test_empty_history():
    # Create empty history file
    filename = str(uuid.uuid4())
    open(filename, 'a').close()

    num_power_sets = 2
    get_power_sets(TEST_USER,
                   num_power_sets=num_power_sets,
                   gym=GYM_LOCAL,
                   input_filename=filename,
                   output_filename=filename,
                   now=datetime.utcnow())

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    os.remove(filename)

    # Assert the correct number of sets is produced
    assert len(lines) == NUM_SETS_PER_POWER_SET * num_power_sets

    # Assert no repeated exercises
    assert len(set(lines)) == len(lines)


def test_performance():
    start_time = time.time()
    get_power_sets(TEST_USER,
                   num_power_sets=2,
                   gym=GYM_LOCAL,
                   input_filename='test_performance_input.txt',
                   output_filename='test_performance_output.txt',
                   now=datetime.utcnow())

    # Assert scoring given a long, full workout log takes under 2s
    assert time.time() - start_time < 2.0


def test_partition_history():
    now = datetime.utcnow()

    history = [
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
    ]
    expected_lengths = (2, 0, 0, 0)
    partitions = partition_history(history, now, set_index=2)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))

    history = [
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
    ]
    expected_lengths = (0, 3, 0, 0)
    partitions = partition_history(history, now, set_index=0)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))

    history = [
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
    ]
    expected_lengths = (0, 0, 3, 3)
    partitions = partition_history(history, now, set_index=0)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))

    history = [
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
    ]
    expected_lengths = (2, 0, 3, 3)
    partitions = partition_history(history, now, set_index=2)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))

    history = [
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
    ]
    expected_lengths = (1, 2, 3, 3)
    partitions = partition_history(history, now, set_index=1)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))

    history = [
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now, 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=1, seconds=1), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
        (now - timedelta(days=2, seconds=2), 'workout', 'variant'),
    ]
    expected_lengths = (0, 3, 3, 3)
    partitions = partition_history(history, now, set_index=0)
    assert all(len(partitions[i]) == expected_lengths[i] for i in range(len(partitions)))


def test_formatting_of_exercises():
    # For spreadsheet stuff
    for exercise_name, exercise in EXERCISES.items():
        assert '\n' not in exercise_name
        assert ',' not in exercise_name

        variations = ';'.join(exercise.get('variations', ()))
        assert '\n' not in variations
        assert ',' not in variations
