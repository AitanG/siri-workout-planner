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
        'secondary_muscle_groups': set([CALVES, QUADS, HAMSTRINGS, GLUTES, LOWER_BACK]),
        'machines': set([MACHINE_TREADMILL]),
    },
    'elliptical': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([QUADS, HAMSTRINGS, GLUTES, LOWER_BACK]),
        'machines': set([MACHINE_ELLIPTICAL]),
    },
    'burpees': {
        'primary_muscle_groups': set([CARDIO]),
        'secondary_muscle_groups': set([QUADS, HAMSTRINGS, GLUTES, LOWER_BACK, PECS, TRICEPS, FRONT_DELTS, FRONT_ABS]),
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
        'secondary_muscle_groups': set([MIDDLE_BACK, HAMSTRINGS]),
        'machines': set([MACHINE_BARBELLS, MACHINE_RACK, MACHINE_SMITH_MACHINE]),
    },
    'leg press': {
        'primary_muscle_groups': set([QUADS, GLUTES]),
        'secondary_muscle_groups': set([HAMSTRINGS]),
        'machines': set([MACHINE_LEG_PRESS]),
    },
    'leg extension': {
        'primary_muscle_groups': set([QUADS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LEG_EXTENSION]),
    },
}


# Hamstrings
EXERCISES_FOR_HAMSTRINGS = {
    'hamstring curl': {
        'primary_muscle_groups': set([HAMSTRINGS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_HAMSTRING_CURL]),
    },
}


# Glutes
EXERCISES_FOR_GLUTES = {
    'lunges': {
        'primary_muscle_groups': set([GLUTES, QUADS]),
        'secondary_muscle_groups': set([HAMSTRINGS, LOWER_BACK, CALVES]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['walking', 'in place', 'bulgarian split squat']),
    },
    'pelvic thrusts': {
        'primary_muscle_groups': set([GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([HAMSTRINGS, MIDDLE_BACK]),
        'machines': set([MACHINE_BENCH]),
    },
}


#################
# Abs
#################

# Front
EXERCISES_FOR_FRONT_ABS = {
    'decline situps': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_ABDOMINAL_BENCH]),
        'variations': set(['without weight', 'with weight']),
    },
    'decline oblique situps': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set([OBLIQUES]),
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
    'leg lift machine': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LEG_LIFT]),
    },
    'floor leg lifts': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_FLOOR]),
    },
    'ab crunch machine': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_AB_CRUNCH]),
    },
    'planks': {
        'primary_muscle_groups': set([FRONT_ABS]),
        'secondary_muscle_groups': set([]),
        'machines': set([MACHINE_FLOOR]),
    },
}


# Obliques
EXERCISES_FOR_OBLIQUES = {
    'cable torso rotation': {
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
    },
}


# Lower back
EXERCISES_FOR_LOWER_BACK = {
    'back extensions': {
        'primary_muscle_groups': set([LOWER_BACK, GLUTES]),
        'secondary_muscle_groups': set([HAMSTRINGS]),
        'machines': set([MACHINE_BACK_EXTENSION]),
        'variations': set(['without weight', 'with weight']),
    },
    'deadlifts': {
        'primary_muscle_groups': set([GLUTES, LOWER_BACK]),
        'secondary_muscle_groups': set([HAMSTRINGS, MIDDLE_BACK]),
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
    'reverse flys': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'breaking chains': {
        'primary_muscle_groups': set([UPPER_BACK, BACK_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DOUBLE_CABLE]),
    },
    'stiff arm raises': {
        'primary_muscle_groups': set([UPPER_BACK, FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK, MIDDLE_DELTS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'dumbbell rows': {
        'primary_muscle_groups': set([UPPER_BACK, LATS, TRAPS]),
        'secondary_muscle_groups': set([MIDDLE_BACK, LOWER_BACK]),
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
        'primary_muscle_groups': set([TRAPS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
}


# Pecs
EXERCISES_FOR_PECS = {
    'flys': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_DOUBLE_CABLE]),
    },
    'pec deck': {
        'primary_muscle_groups': set([PECS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PEC_DECK]),
    },
    'bench press': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_RACK]),
    },
    'incline bench press': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS, MIDDLE_DELTS]),
        'machines': set([MACHINE_INCLINE_BENCH]),
    },
    'dumbbell bench press': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'pushups': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS]),
        'secondary_muscle_groups': set([TRICEPS, FRONT_ABS]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(['diamond', 'clapping', 'normal']),
    },
    'hollow plank press': {
        'primary_muscle_groups': set([PECS, FRONT_DELTS, FRONT_ABS, OBLIQUES]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_FLOOR]),
        'variations': set(),
    },
}


# Lats
EXERCISES_FOR_LATS = {
    'lat pulldown': {
        'primary_muscle_groups': set([LATS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_LAT_PULLDOWN]),
        'variations': set(['bar', 'double handle']),
    },
    'pullups': {
        'primary_muscle_groups': set([LATS]),
        'secondary_muscle_groups': set([BICEPS, FRONT_ABS]),
        'machines': set([MACHINE_PULLUP_BAR]),
    },
    'pulldowns': {
        'primary_muscle_groups': set([LATS]),
        'secondary_muscle_groups': set([BICEPS]),
        'machines': set([MACHINE_PULLDOWN_MACHINE]),
    },
    # arms out -> to side, too agro though
}


# Front delts
EXERCISES_FOR_FRONT_DELTS = {
    'overhead dumbbell press': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_DUMBBELLS]),
    },
    'overhead barbell press': {
        'primary_muscle_groups': set([FRONT_DELTS, TRAPS]),
        'secondary_muscle_groups': set([TRICEPS]),
        'machines': set([MACHINE_BARBELLS]),
    },
}


# Middle delts
EXERCISES_FOR_MIDDLE_DELTS = {
    'dumbbell lateral raise': {
        'primary_muscle_groups': set([MIDDLE_DELTS]),
        'secondary_muscle_groups': set([FRONT_DELTS, TRAPS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['thumbs out', 'thumbs down', 'thumbs 3/4 down']),
    },
    'lateral raise machine': {
        'primary_muscle_groups': set([MIDDLE_DELTS]),
        'secondary_muscle_groups': set([FRONT_DELTS, TRAPS]),
        'machines': set([MACHINE_LATERAL_RAISE]),
    },
}


# Back delts
EXERCISES_FOR_BACK_DELTS = {
    'cable delts': {
        'primary_muscle_groups': set([BACK_DELTS]),
        'secondary_muscle_groups': set([UPPER_BACK]),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
}


#################
# Arms
#################

# Biceps
EXERCISES_FOR_BICEPS = {
    'dumbbell bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([TRAPS]),
        'machines': set([MACHINE_DUMBBELLS]),
        'variations': set(['together', 'alternating', 'reverse incline', 'incline']),
    },
    'cable bicep curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
        'variations': set(['vertical—bar', 'reverse incline—bar', 'vertical—handles', 'reverse incline—handles']),
    },
    'preacher curls': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_PREACHER_CURL_BENCH]),
        'variations': set(['regular bar', 'EZ bar']),
    },
    'bicep pullups': {
        'primary_muscle_groups': set([BICEPS]),
        'secondary_muscle_groups': set([FRONT_ABS, LATS]),
        'machines': set([MACHINE_PULLUP_BAR]),
    },
    # add hammer
}


# Triceps
EXERCISES_FOR_TRICEPS = {
    'cable triceps': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_SINGLE_CABLE, MACHINE_DOUBLE_CABLE]),
    },
    'dumbbell overhead tricep extension': {
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
    'barbell tricep extension': {
        'primary_muscle_groups': set([TRICEPS]),
        'secondary_muscle_groups': set(),
        'machines': set([MACHINE_BARBELLS]),
        'variations': set(['flat bench', 'incline bench', 'upright bench'])
    },
    # add kickback
}


EXERCISES = {
    # Excluding cardio because it's a separate thing / depends on energy levels
    # **EXERCISES_FOR_CARDIO,
    **EXERCISES_FOR_CALVES,
    **EXERCISES_FOR_QUADS,
    **EXERCISES_FOR_HAMSTRINGS,
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
}