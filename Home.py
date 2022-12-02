
import squat_module as sm
import sideLunge_module as slm
from matplotlib import pyplot as plt
import sys
from user import User

class Home(User):
    def __init__(self):
        super().__init__(self, first, last)
  
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
                print(dataList)
                plt.show()

            if choice == 'Side Lunge':
                reps = int(input('Input target repetition amount: '))
                squat = slm.sLunge(reps)
                dataList = []
                dataList.append(slm.sLunge.dosLunge())
                # print(dataList)
                plt.show()             

        if choice == 2:
            from programModule import Program
            Program.greeting()

        if choice == 3:
            pass

        if choice == 4:
            pass

        if choice == 5:
            print("Until next time!")
            sys.exit()

        return menu()
        


@staticmethod
def initialWelcome():
    choice = int(input("\n---------- Hello, welcome back to your Nowva 0.One! ----------\n\n1. Quick Exercise\n2. My Progress\n3. Start A Workout Plan\n4. Initialization\n5. Exit\n"))
    return choice

@staticmethod
def menu():
    choice = int(input("\nMain Menu:\n1. Quick Exercise\n2. My Progress\n3. Start A Workout Plan\n4. Initialization\n5. Exit\n"))
    return Home.treatChoice(choice)


def main():
    user = User()
    choice = 0
    choice = Home.getChoice(choice)
    Home.treatChoice(choice)

    

if __name__ == '__main__':
    main()
