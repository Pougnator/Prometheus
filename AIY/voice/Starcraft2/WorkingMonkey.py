import sched
import time



# test_build_order = {
#     12 : "spawn an overlord"
#     17 : "drone"
#     30 : "two more drones"
#     49 : "build a hatchery"
# }
test_build_order = [[0,"Spawn a drone"],[12,"Spawn an overlord"], \
[17,"Spawn a drone"], [30,"Spawn two more drones"], [49,"Build a hatchery"], \
[52,"Spawn two drones"],[60,"Spawn a drone"],[70, "Build an extractor"],\
[75,"Build a Spawning Pool"],[78,"Hatch a drone"],[86,"Hatch two drones"],\
[109,"Spawn an Overlord"],[121, "Spawn two Queens"],[123, "Spawn two zerlings"],\
[130,"Upgrade Metablic Boost"],[160,"Build a Hatchery"],[166,"Spawn two zerlings"],\
[177,"Hatch an Overlord"],[179,"Spawn a Queen"],[195,"Overlord"],\
[208,"Overlord"],[220,"Queen"],[225,"Build a Spore Crawler"],\
[233,"Hatch four Zerglings"],[240,"Queen"],[250,"Another Spore Crawler"],\
[262,"Lair"],[264,"Two extractors"],[276,"Build a Spore Crawler"],\
[285,"Build a Roach Warren"],[291,"Two zerglings"],[304,"Extractor"],\
[325,"Seven Roaches"],[329,"Upgrade Gilal Reconstitution"],[354,"Extractor"],\
]

def sayCommand(text):
   
    #aiy.audio.say(text)
    #buildOrder.pop(0)
    #if len(buildOrder)>1:
    #    scheduleEvent(buildOrder)
    #else:
    #    print("The End")
    print('Rise event')
    print(text)

def scheduleEvent(buildOrder, scheduler):
    stext = buildOrder[1][1]
    seconds = buildOrder[1][0]
    
    print ('Event scheduled in ', seconds, ' seconds')
    scheduler.enter(seconds, 1, sayCommand, (stext,))
    
    print('Rise event')
    print(stext)

def monkey(buildOrder):
    myscheduler = sched.scheduler(time.time, time.sleep)
    i=0
    while i < len(buildOrder):
         
        if len(buildOrder)>1:
            scheduleEvent(buildOrder, myscheduler)
        else:
            print("The End")
        buildOrder.pop(0)
        i+=1
    myscheduler.run()

if __name__ == '__main__':
    monkey(test_build_order)
