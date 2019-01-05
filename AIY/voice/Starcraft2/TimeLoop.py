import time
def MyTimer():
    t=10
    print('Time to next action\n')
    while t >= 0:
        print(t, end='..\r')
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')

if __name__ == '__main__':
    MyTimer()