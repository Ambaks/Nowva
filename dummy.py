def func():
    i = int(input('1 or 2\n'))
    return i, func2(i)

def func2(int):
    if int == 1:
        print('You passed')
        return func()
    else:
        print('You lost')
        
        

func()