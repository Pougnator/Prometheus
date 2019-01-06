import sched
import time



# test_build_order = {
#     12 : "spawn an overlord"
#     17 : "drone"
#     30 : "two more drones"
#     49 : "build a hatchery"
# }
test_build_order = [[0,"Spawn a drone"],[12,"Spawn an overlord"], \
 [17,"Spawn a drone"], [30,"Spawn two more drones"], [49,"Build a hatchery"] ]

def sayCommand(text, buildOrder):
    print('Rise event')
    print(text)
    #aiy.audio.say(text)
    buildOrder.pop(0)
    if len(buildOrder)>1:
        scheduleEvent(buildOrder)
    else:
        print("The End")
    

def scheduleEvent(buildOrder):
    stext = buildOrder[1][1]
    seconds = buildOrder[1][0] - buildOrder[0][0]
    scheduler = sched.scheduler(time.time, time.sleep)
    print ('Event scheduled in ', seconds, ' seconds')
    scheduler.enter(seconds, 1, sayCommand, (stext, buildOrder))
    scheduler.run()


if __name__ == '__main__':
    scheduleEvent(test_build_order)
