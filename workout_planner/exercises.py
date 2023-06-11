from .machines import *
from .muscle_groups import *


#################
# Legs
#################

# Cardio
EXERCISES_FOR_CARDIO = {
    'rower': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([UPPER_BACK, MIDDLE_BACK, LOWER_BACK, GLUTES, QUADS, LATS]),
        'machines': set([MACHINE_ROWER]),
    },
    'treadmill': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([CALVES, QUADS, HAMS, GLUTES, LOWER_BACK]),
        'machines': set([MACHINE_TREADMILL]),
    },
    'elliptical': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([QUADS, HAMS, GLUTES, LOWER_BACK]),
        'machines': set([MACHINE_ELLIPTICAL]),
    },
    'burpees': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([QUADS, HAMS, GLUTES, LOWER_BACK, PECS, TRICEPS, FRONT_DELTS, FRONT_ABS]),
        'machines': set([MACHINE_FLOOR]),
    },
}


# Calves
EXERCISES_FOR_CALVES = {
    'leg press calf raises': {
        'primary_muscle_groups': set([CALVES]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LEG_LIFT]),
        'variations': set(['wide', 'narrow']),
    },
    'calf machine calf raises': {
        'primary_muscle_groups': set([CALVES]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_CALF_MACHINE]),
        'variations': set(['wide', 'narrow']),
    },
    'standing calf raises': {
        'primary_muscle_groups': set([CALVES]),
        'secondary_muscle_groups': set([TRAPS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['wide', 'narrow']),
    },
    'walking calf raises': {
        'primary_muscle_groups': set([CALVES]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
}


# Quads
EXERCISES_FOR_QUADS = {
    'squats': {
        'primary_muscle_groups': set([QUADS, GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([MIDDLE_BACK, HAMS]),
        'machines': set([MACHINE_BARBELLS, MACHINE_RACK, MACHINE_SMITH_MACHINE, MACHINE_FLOOR]),
    },
    'leg presses': {
        'primary_muscle_groups': set([QUADS, GLUTES]),
        'secondary_muscle_groups': set([HAMS]),
        'machines': set([MACHINE_LEG_PRESS]),
    },
    'leg extensions': {
        'primary_muscle_groups': set([QUADS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LEG_EXTENSION]),
    },
}


# Hams
EXERCISES_FOR_HAMS = {
    'hamstring curls': {
        'primary_muscle_groups': set([HAMS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_HAMSTRING_CURL]),
    },
}


# Glutes
EXERCISES_FOR_GLUTES = {
    'lunges': {
        'primary_muscle_groups': set([GLUTES, QUADS]),
        'secondary_muscle_groups': set([HAMS, LOWER_BACK, CALVES]),
        'machines': set([MACHINE_DUMBBELLS, MACHINE_FLOOR]),
        'variations': set(['walking', 'in place']),
    },
    'bulgarian split squats': {
        'primary_muscle_groups': set([GLUTES, QUADS]),
        'secondary_muscle_groups': set([HAMS, LOWER_BACK, CALVES]),
        'machines': set([MACHINE_PLATFORM]),
    },
    'hip thrusters': {
        'primary_muscle_groups': set([GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([HAMS, MIDDLE_BACK]),
        'machines': set([MACHINE_BENCH]),
    },
    'glute bridges': {
        'primary_muscle_groups': set([GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([MIDDLE_BACK]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['single leg', 'regular']),
    },
    'step ups': {
        'primary_muscle_groups': set([GLUTES, QUADS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PLATFORM]),
    },
}


#################
# Abs
#################

# Front
EXERCISES_FOR_FRONT_ABS = {
    'decline situps': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set([OBLIQUES]),
        'machines': set([MACHINE_ABDOMINAL_BENCH]),
        'variations': set(['without weight', 'with weight']),
    },
    'decline oblique situps': {
        'primary_muscle_groups': set([FRONT_ABS, OBLIQUES]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_ABDOMINAL_BENCH]),
    },
    'v-ups': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
    'bicycles': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set([OBLIQUES]),
        'machines': set([MACHINE_FLOOR]),
    },
    'crunches': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
    'leg lifts': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LEG_LIFT]),
    },
    'floor leg lifts': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
    'ab crunches': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_AB_CRUNCH]),
    },
    'planks': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set([]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['regular', 'long lever']),
    },
}


# Obliques
EXERCISES_FOR_OBLIQUES = {
    'cable torso rotations': {
        'primary_muscle_groups': set([OBLIQUES]),
        'secondary_muscle_groups': set([FRONT_ABS, LOWER_BACK, GLUTES]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'rotary torso machine': {
        'primary_muscle_groups': set([OBLIQUES]),
        'secondary_muscle_groups': set([FRONT_ABS, LOWER_BACK]),
        'machines': set([MACHINE_ROTARY_TORSO]),
    },
    'side planks': {
        'primary_muscle_groups': set([OBLIQUES]),
        'secondary_muscle_groups': set([LOWER_BACK]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['regular', 'up-and-down', 'reach through']),
    },
    'resistance band torso rotations': {
        'primary_muscle_groups': set([OBLIQUES]),
        'secondary_muscle_groups': set([FRONT_ABS, LOWER_BACK, GLUTES]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
    'dumbbell side bends': {
        'primary_muscle_groups': set([OBLIQUES]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'russian twists': {
        'primary_muscle_groups': set([OBLIQUES, FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
}


# Lower back
EXERCISES_FOR_LOWER_BACK = {
    'back extensions': {
        'primary_muscle_groups': set([LOWER_BACK, GLUTES]),
        'secondary_muscle_groups': set([HAMS]),
        'machines': set([MACHINE_BACK_EXTENSION]),
        'variations': set(['without weight', 'with weight']),
    },
    'deadlifts': {
        'primary_muscle_groups': set([GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([HAMS, MIDDLE_BACK]),
        'machines': set([MACHINE_BARBELLS]),
    },
}


# Middle back
EXERCISES_FOR_MIDDLE_BACK = {
    'superman': {
        'primary_muscle_groups': set([MIDDLE_BACK, LOWER_BACK]),
        'secondary_muscle_groups': set([GLUTES, UPPER_BACK]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['hold', 'up-and-down']),
    },
    'cable silverback shrugs': {
        'primary_muscle_groups': set([UPPER_BACK, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
}


#################
# Upper body
#################

# Upper back
EXERCISES_FOR_UPPER_BACK = {
    'machine rows': {
        'primary_muscle_groups': set([UPPER_BACK]),
        'secondary_muscle_groups': set([BICEPS, LATS]),
        'machines': set([MACHINE_ROW_MACHINE]),
    },
    'reverse fly machine': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_REVERSE_FLY_MACHINE]),
    },
    'breaking chains': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DOUBLE_CABLE]),
    },
    'cable front raises': {
        'primary_muscle_groups': set([UPPER_BACK, FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK, MIDDLE_DELTS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'dumbbell front raises': {
        'primary_muscle_groups': set([UPPER_BACK, FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK, MIDDLE_DELTS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'resistance band front raises': {
        'primary_muscle_groups': set([UPPER_BACK, FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK, MIDDLE_DELTS]),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
    },
    'dumbbell rows': {
        'primary_muscle_groups': set([UPPER_BACK, LATS, OBLIQUES]),
        'secondary_muscle_groups': set([MIDDLE_BACK, LOWER_BACK, TRAPS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'incline TRX rows': {
        'primary_muscle_groups': set([UPPER_BACK, LATS, TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_TRX]),
    },
    'incline cable rows': {
        'primary_muscle_groups': set([UPPER_BACK, LATS, TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'cable reverse flys': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'pec deck reverse flys': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PEC_DECK]),
    },
    'resistance band pull aparts': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
    },
}


# Traps
EXERCISES_FOR_TRAPS = {
    'shrugs': {
        'primary_muscle_groups': set([TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_DUMBBELLS, MACHINE_BARBELLS]),
        'variations': set(['regular', 'incline']),
    },
    'face pulls': {
        'primary_muscle_groups': set([BACK_DELTS, UPPER_BACK, TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'resistance band face pulls': {
        'primary_muscle_groups': set([BACK_DELTS, UPPER_BACK, TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
    'elevated pike shrugs': {
        'primary_muscle_groups': set([TRAPS]),
        'secondary_muscle_groups': set([TRICEPS, FRONT_DELTS, MIDDLE_DELTS, FRONT_ABS]),
        'machines': set([MACHINE_PLATFORM]),
    },
    'barbell upright row': {
        'primary_muscle_groups': set([TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_BARBELLS]),
    },
    'cable upright row': {
        'primary_muscle_groups': set([TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'cable 30 degree shrugs': {
        'primary_muscle_groups': set([TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_DOUBLE_CABLE]),
    },
    'band shrugs': {
        'primary_muscle_groups': set([TRAPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
    },
    'band horizontal shrugs': {
        'primary_muscle_groups': set([TRAPS, UPPER_BACK]),
        'secondary_muscle_groups': set([MIDDLE_BACK]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
}


# Pecs
EXERCISES_FOR_PECS = {
    'fly machine': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_FLY_MACHINE]),
    },
    'cable flys': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_DOUBLE_CABLE]),
        'variations': set(['high', 'level', 'low']),
    },
    'pec deck': {
        'primary_muscle_groups': set([PECS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PEC_DECK]),
    },
    'bench presses': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_RACK]),
        'variations': set(['regular', 'close grip']),
    },
    'bench press machine': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_BENCH_PRESS_MACHINE]),
    },
    'incline bench presses': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS, MIDDLE_DELTS]),
        'machines': set([MACHINE_INCLINE_BENCH]),
    },
    'dumbbell bench presses': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['flat, guillotine', 'incline, guillotine', 'flat, neutral', 'incline, neutral', 'flat, squeeze', 'incline, squeeze']),
    },
    'pushups': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS, FRONT_ABS]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['diamond', 'clapping', 'normal']),
    },
    'resistance band flys': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
    'elevated pike presses': {
        'primary_muscle_groups': set([PECS, TRICEPS, FRONT_DELTS]),
        'secondary_muscle_groups': set([MIDDLE_DELTS, FRONT_ABS]),
        'machines': set([MACHINE_PLATFORM]),
    },
    # 'hollow plank presses': {
    #     'primary_muscle_groups': set([PECS, FRONT_DELTS, FRONT_ABS, OBLIQUES]),
    #     'secondary_muscle_groups': set([TRICEPS]),
    #     'machines': set([MACHINE_FLOOR]),
    #     'variations': set(),
    # },
}


# Lats
EXERCISES_FOR_LATS = {
    'lat pulldowns': {
        'primary_muscle_groups': set([LATS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LAT_PULLDOWN]),
        'variations': set(['bar', 'double handle']),
    },
    'pullups': {
        'primary_muscle_groups': set([BICEPS, LATS]),
        'secondary_muscle_groups': set([FRONT_ABS]),
        'machines': set([MACHINE_PULLUP_BAR]),
        'variations': set(['chin ups', 'neutral', 'regular']),
    },
    'pulldowns': {
        'primary_muscle_groups': set([LATS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_PULLDOWN_MACHINE]),
    },
}


# Front delts
EXERCISES_FOR_FRONT_DELTS = {
    'overhead dumbbell presses': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'overhead barbell presses': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_BARBELLS]),
    },
    'overhead press machine': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_SHOULDER_PRESS_MACHINE]),
    },
    'resistance band overhead presses': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
    },
    'bench dips': {
        'primary_muscle_groups': set([FRONT_DELTS, TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PLATFORM]),
    },
}


# Middle delts
EXERCISES_FOR_MIDDLE_DELTS = {
    'dumbbell lateral raises': {
        'primary_muscle_groups': set([MIDDLE_DELTS, TRAPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['thumbs out', 'thumbs down']),
    },
    'lateral raise machine': {
        'primary_muscle_groups': set([MIDDLE_DELTS, TRAPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_LATERAL_RAISE]),
    },
    'resistance band lateral raises': {
        'primary_muscle_groups': set([MIDDLE_DELTS, TRAPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
    },
    # https://musclewiki.com/cables/male/shoulders/cable-lateral-raise
    'cable lateral raises': {
        'primary_muscle_groups': set([MIDDLE_DELTS, TRAPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['across', 'bayesian']),
    },
    'resistance band anchored lateral raises': {
        'primary_muscle_groups': set([MIDDLE_DELTS, TRAPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
        'variations': set(),
    },
}


# Back delts
EXERCISES_FOR_BACK_DELTS = {
    'cable rear delt flys': {
        'primary_muscle_groups': set([BACK_DELTS, MIDDLE_DELTS]),
        'secondary_muscle_groups': set([UPPER_BACK]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['high', 'level', 'low']),
    },
    'resistance band delts': {
        'primary_muscle_groups': set([BACK_DELTS]),
        'secondary_muscle_groups': set([UPPER_BACK]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
}


#################
# Arms
#################

# Biceps
EXERCISES_FOR_BICEPS = {
    'dumbbell bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([TRAPS, FRONT_DELTS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['regular', 'hammer', 'reverse', 'regular, incline', 'hammer, incline', 'reverse, incline']),
    },
    'cable bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['vertical, bar', 'incline, bar', 'vertical, handles', 'incline, handles']),
    },
    'cable bayesian bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_DOUBLE_CABLE]),
        'variations': set(['regular', 'hammer', 'reverse']),
    },
    'cable high bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['horizontal, bar', 'high, bar', 'horizontal, handles, regular', 'high, handles, regular', 'horizontal, handles, hammer', 'high, handles, hammer', 'horizontal, handles, reverse', 'high, handles, reverse']),
    },
    'barbell preacher curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PREACHER_CURL_BENCH]),
        'variations': set(['regular bar', 'EZ bar']),
    },
    'dumbbell preacher curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PREACHER_CURL_BENCH]),
        'variations': set(['turned out', 'turned in', 'regular']),
    },
    'resistance band bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([TRAPS, FRONT_DELTS]),
        'machines': set([MACHINE_RESISTANCE_BANDS]),
        'variations': set(['regular', 'hammer', 'reverse']),
    },
    'resistance band bayesian bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
        'variations': set(['regular', 'hammer', 'reverse']),
    },
    'resistance band high bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
        'variations': set(['horizontal, regular', 'horizontal, hammer', 'horizontal, reverse', 'high, regular', 'high, hammer', 'high, reverse']),
    },
}


# Triceps
EXERCISES_FOR_TRICEPS = {
    'cable triceps': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['rope', 'handle']),
    },
    'cable skull crushers': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['rope', 'handles']),
    },
    'dumbbell overhead tricep extensions': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set([FRONT_DELTS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'skull crushers': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['arms parallel to body', 'arms perpendicular to body'])
    },
    'dips': {
        'primary_muscle_groups': set([TRICEPS, PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_DIPS]),
    },
    'barbell tricep extensions': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_BARBELLS]),
        'variations': set(['flat bench', 'incline bench', 'upright bench'])
    },
    'resistance band triceps': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
    'resistance band skull crushers': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_RESISTANCE_BANDS_WITH_ANCHOR]),
    },
}

EXERCISES_FOR_HIP_ABDUCTORS = {
    'hip abductors': {
        'primary_muscle_groups': set([HIP_ABDUCTORS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_HIPS]),
    },
}

EXERCISES_FOR_HIP_ADDUCTORS = {
    'hip adductors': {
        'primary_muscle_groups': set([HIP_ADDUCTORS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_HIPS]),
    },
}


EXERCISES = {
    # Excluding cardio
    # **EXERCISES_FOR_CARDIO,
    **EXERCISES_FOR_CALVES,
    **EXERCISES_FOR_QUADS,
    **EXERCISES_FOR_HAMS,
    **EXERCISES_FOR_GLUTES,
    **EXERCISES_FOR_FRONT_ABS,
    **EXERCISES_FOR_OBLIQUES,
    **EXERCISES_FOR_LOWER_BACK,
    **EXERCISES_FOR_MIDDLE_BACK,
    **EXERCISES_FOR_UPPER_BACK,
    **EXERCISES_FOR_TRAPS,
    **EXERCISES_FOR_PECS,
    **EXERCISES_FOR_LATS,
    **EXERCISES_FOR_FRONT_DELTS,
    **EXERCISES_FOR_MIDDLE_DELTS,
    **EXERCISES_FOR_BACK_DELTS,
    **EXERCISES_FOR_BICEPS,
    **EXERCISES_FOR_TRICEPS,
    **EXERCISES_FOR_HIP_ADDUCTORS,
    **EXERCISES_FOR_HIP_ABDUCTORS,
}