import squat_module as sm
from matplotlib import pyplot as plt

choice = int(input("Hello! Welcome back to your Nowva 0.One! What would you wish to do?\n1. Quick Exercise\n2. My Progress\n3. Start A Workout Plan\n4. Initialization\n"))
if choice == 1:
    choice = str(input('---------- Quick Exercise ----------\nChoose your exercise:\n - Squat\n - Bench Press\n - Deadlift\n'))
    if choice == 'Squat':
        reps = int(input('Input target repetition amount: '))
        squat = sm.Squat(reps)
        dataList = []

        dataList.append(squat.doSquat())
        # print(dataList)
        plt.show()







# Greeting

# Pick exercise
    #Add data to database

# Ask for another exercise

