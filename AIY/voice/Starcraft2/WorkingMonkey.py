import sched
import time
from TimeLoop import MyTimer


scheduler = sched.scheduler(time.time, time.sleep)

def event():
    print ('BEGIN EVENT :', time.time())
    #aiy.audio.say('What up bitch?')
   

print ('START:', time.time())
seconds =  5
scheduler.enter(seconds, 1, MyTimer)


if __name__ == '__main__':
    scheduler.run()
