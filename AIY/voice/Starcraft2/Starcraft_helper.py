#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import sched
import time
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import aiy.i18n
import aiy.audio


CONFIRM_SOUND_PATH = '/home/pi/Music/R2D2/R2_Understood.wav'
CONFUSED_SOUND_PATH = '/home/pi/Music/R2D2/R2_Confused.wav'
UNRECOGNISED_SOUND_PATH = '/home/pi/Music/R2D2/R2_FastBip.wav'

test_build_order = [[0,"Spawn a drone"],[12,"Spawn an overlord"], \
[17,"Spawn a drone"], [30,"Spawn two more drones"], [49,"Build a hatchery"] ]

def sayCommand(text, buildOrder):
    print('Rise event')
    print(text)
    aiy.audio.say(text)
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



# def EventMonkey(seconds):
#     scheduler = sched.scheduler(time.time, time.sleep)
#     print ('START:', time.time())
#     scheduler.enter(seconds, 1, aiy.audio.say('Ho Ho Ho! I am your mama'))

def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    scheduler = sched.scheduler(time.time, time.sleep)
    
    aiy.i18n.set_language_code("en-GB")
    recognizer = aiy.cloudspeech.get_recognizer()
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    aiy.audio.say('Hello mother fucker!')
    
    status_ui.status('ready')
    print('Press the button to start')
    aiy.audio.say('Press the button to start!')
    button.wait_for_press()
    aiy.voicehat.get_status_ui().set_trigger_sound_wave('/home/pi/Music/R2D2/R2_Understood.wav')
    aiy.audio.say('All right bitch let us start')
    aiy.audio.say("Build that first drone")
    scheduleEvent(test_build_order)

if __name__ == '__main__':
    main()
