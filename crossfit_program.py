import random
#Lists of all applicable data
weeks = [1,2,3]
days = [1,2,3,4,5,6,7]
modality_combinations = ['M','GW','MGW','MG','W','G','MW']
gymnastics_exercises = ['Air Squats','Pull Ups','Push Ups', 'Dips', 'Handstand Push Ups','Rope Climbs',
'Muscle Ups', 'Sit Ups', 'Box Jumps', 'Burpees', 'Lunges']
metabolic_conditioning_exercises = ['Run', 'Bike', 'Row', 'Jump Rope']
weightlifting_exercises = ['Deadlifts','Cleans','Overhead Press','Push Press','Bench Press',
'Snatch','Clean and Jerk','Kettlebell Swing','Front Squat','Back Squat']
set_structures = {'Time':[10,12,15,20,25,30,45] ,
'Rounds':[3,4,5]}
reps = list(range(3,30,3))
motivational_quotes = ['Today I will do what others won’t, so tomorrow I can accomplish what others can’t. — Jerry Rice',
'Do something today that your future self will thank you for.', 'We are what we repeatedly do. Excellence then is not an act but a habit.'
'No matter how slow you go, you are still lapping everybody on the couch', 'You miss 100% of the shots you don’t take']
#function to determine what modality/modality combo depending on the week and day

def get_modality(week, day):
    if week == 1:
        modality_combo = dict(zip(days[0:5],modality_combinations[0:5]))
    elif week == 2:
        modality_combo = dict(zip(days[0:5], modality_combinations[5:7]+modality_combinations[2::-1]))
    elif week == 3:
        modality_combo = dict(zip(days[0:5], modality_combinations[4:1:-1] + modality_combinations[6:4:-1]))
    modality = modality_combo.get(day)
    if day == 6 or day ==7:
        modality = 'Rest Day'
    return modality

#function to generate a random execise depending on the modality
def get_exercise(modality):
    if modality == 'M':
        exercise = random.choice(metabolic_conditioning_exercises)
    elif modality == 'G':
        exercise = random.choice(gymnastics_exercises)
    elif modality == 'W':
        exercise = random.choice(weightlifting_exercises)
    elif modality == 'MG':
        exercise = [random.choice(metabolic_conditioning_exercises), random.choice(gymnastics_exercises)]
    elif modality == 'GW':
        exercise = [random.choice(gymnastics_exercises), random.choice(weightlifting_exercises)]
    elif modality == 'MW':
        exercise = [random.choice(metabolic_conditioning_exercises), random.choice(weightlifting_exercises)]
    elif modality == 'MGW':
        exercise = [random.choice(metabolic_conditioning_exercises), random.choice(gymnastics_exercises), random.choice(weightlifting_exercises)]
    else:
        exercise = 'Rest Day'
    return exercise

#don't forget the G case
def get_set_structure(modality):
    if modality == 'M':
        set_structure = random.choice([30,35,40,45,50,55,60])
    elif modality == 'W':
        set_structure = [random.choice(range(1,6)), random.choice(range(1,6))]
    elif modality == 'G':
        set_structure = 'Spend some time practicing for 45 minutes'
    elif modality == 'MG' or modality == 'GW' or modality == 'MW':
        set_structure = random.choice(set_structures['Rounds'])
    elif modality == 'MGW':
        set_structure = random.choice(set_structures['Time'])
    else:
        set_structure = 'Rest Day'
    return set_structure

print(random.choice(motivational_quotes))
week = int(input('What week are you on? '))
day = int(input('What day are you on? '))

modality = get_modality(week, day)
exercise = get_exercise(modality)
set_structure = get_set_structure(modality)


def get_meters_cal_reps(exercise):
    if modality == 'MG' or modality == 'MW' or modality == 'MGW':
        if exercise[0] == 'Run':
            meters_cal_reps = ['200m','400m','800m']
        elif exercise[0] == 'Row':
            meters_cal_reps = ['250m', '500m', '1000m', '20 cal', '30 cal', '40 cal']
        elif exercise[0] == 'Bike':
            meters_cal_reps = ['10 cal', '15 cal', '20 cal' , '25 cal']
        elif exercise[0] == 'Jump Rope':
            meters_cal_reps = [20,30,40,50,60]
        return random.choice(meters_cal_reps)

meters_cal_reps = get_meters_cal_reps(exercise)

def get_WOD(modality, set_structure):

    if modality == 'M':
        print('The Workout of the Day is: {time} minute {exercise}'.format(time=set_structure, exercise=exercise))
    elif modality == 'W':
        print('The Workout of the Day is: {sets}x{reps} {exercise}'.format(sets = set_structure[0], reps = set_structure[1], exercise = exercise))
    elif modality == 'G':
        print('The Workout of the Day is: {exercise}. {set_structure}'.format(exercise = exercise, set_structure=set_structure))
    elif modality == 'GW':
        reps1 = random.choice(reps)
        reps2 = random.choice(reps)
        print('The Workout of the Day is: {rounds} Rounds for time of {reps1} {exercise1}, {reps2} {exercise2}'.format(rounds = set_structure,
        reps1 = reps1, exercise1 = exercise[0], reps2 = reps2, exercise2 = exercise[1]))
    elif modality == 'MG' or modality == 'MW':
        reps1 = meters_cal_reps
        reps2 = random.choice(reps)
        reps3 = random.choice(reps)
        print('The Workout of the Day is: {rounds} Rounds for time of {reps1} {exercise1}, {reps2} {exercise2}'.format(rounds = set_structure,
        reps1 = meters_cal_reps, exercise1 = exercise[0], reps2 = reps2, exercise2 = exercise[1]))
    elif modality == 'MGW':
        reps1 = meters_cal_reps
        reps2 = random.choice(reps)
        reps3 = random.choice(reps)
        print('The Workout of the Day is: {time} minute AMRAP, {reps1} {exercise1}, {reps2} {exercise2}, {reps3} {exercise3}'.format(
        time = set_structure, reps1 = meters_cal_reps, exercise1 = exercise[0], reps2 = reps2, exercise2 = exercise[1],
        reps3 = reps3, exercise3 = exercise[2]))
    else:
        print('Rest Day.')

get_WOD(modality, set_structure)
