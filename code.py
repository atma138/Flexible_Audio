import RPi.GPIO as GPIO
import time
import os

# Configuration: Map each GPIO pin to a specific .wav file
pin_sound_map = {
    21: "boomerang.wav",
    20: "clap.wav",
    16: "cowbell.wav",
    12: "highhat.wav",
    26: "kickdrum.wav",
    19: "rimshot.wav",
    13: "snare.wav",
    5: "stab.wav",
    6: "synth.wav"
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
                print(f"Pin {pin} HIGH → Playing {sound_file}")
                os.system(f"aplay {sound_file}")
                time.sleep(0.5)  # Debounce delay

        time.sleep(0.1)  # Polling delay

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
