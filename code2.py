#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

# Configuration: Map each GPIO pin to a specific .wav file
pin_sound_map = {
    21: "/home/pi/Desktop/flex/boomerang.wav",
    20: "/home/pi/Desktop/flex/clap.wav",
    16: "/home/pi/Desktop/flex/cowbell.wav",
    12: "/home/pi/Desktop/flex/highhat.wav",
    26: "/home/pi/Desktop/flex/kickdrum.wav",
    19: "/home/pi/Desktop/flex/rimshot.wav",
    13: "/home/pi/Desktop/flex/snare.wav",
    5: "/home/pi/Desktop/flex/stab.wav",
    6: "/home/pi/Desktop/flex/synth.wav"
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

# Set each pin in the map as input
for pin in pin_sound_map:
    GPIO.setup(pin, GPIO.IN)

print("Monitoring pins:", list(pin_sound_map.keys()))

try:
    while True:
        for pin, sound_file in pin_sound_map.items():
            if GPIO.input(pin) == GPIO.HIGH:
                print(" Pin {} HIGH ==> Playing {}".format(pin,sound_file))
                os.system("paplay {}".format(sound_file))
                time.sleep(0.25)  # Debounce delay

        time.sleep(0.05)  # Polling delay

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()

