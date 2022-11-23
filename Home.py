import squat_module as sm
import sideLunge_module as slm
from matplotlib import pyplot as plt
import sys

class Home:
  
    def getChoice(choice):
        if choice == 0:
            choice = initialWelcome()
            return choice
        else:
            choice = menu()
        return choice
    
    def treatChoice(choice):
        if choice == 1:
            choice = str(input('---------- Quick Exercise ----------\nChoose your exercise:\n - Squat\n - Bench Press\n - Deadlift\n'))
            
            if choice == 'Squat':
                reps = int(input('Input target repetition amount: '))
                squat = sm.Squat(reps)
                dataList = []
                dataList.append(squat.doSquat())
                # print(dataList)
                plt.show()

            if choice == 'Side Lunge':
                reps = int(input('Input target repetition amount: '))
                squat = slm.sLunge(reps)
                dataList = []
                dataList.append(slm.dosLunge())
                # print(dataList)
                plt.show()

                
            

        if choice == 2:
            pass

        if choice == 3:
            pass

        if choice == 4:
            pass

        if choice == 5:
            sys.exit()

        return menu()
        


@staticmethod
def initialWelcome():
    choice = int(input("Hello! Welcome back to your Nowva 0.One! What would you wish to do?\n1. Quick Exercise\n2. My Progress\n3. Start A Workout Plan\n4. Initialization\n"))
    return choice

@staticmethod
def menu():
    choice = int(input("Main Menu:\n1. Quick Exercise\n2. My Progress\n3. Start A Workout Plan\n4. Initialization\n"))
    return Home.treatChoice(choice)


def main():
    choice = 0
    choice = Home.getChoice(choice)
    Home.treatChoice(choice)
    

if __name__ == '__main__':
    main()
