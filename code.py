import RPi.GPIO as GPIO
import time
import os
# import pygame  # Uncomment if using pygame for audio

# Configuration
INPUT_PIN = 17  # Change this to your GPIO pin
WAV_FILE = "/home/pi/sound.wav"  # Update this path

# List of all GPIO pins (BCM mode) on Raspberry Pi (adjust if needed for your board)
ALL_GPIO_PINS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27]

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

# Set all pins to output and LOW
for pin in ALL_GPIO_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Then set the INPUT_PIN back to input mode
GPIO.setup(INPUT_PIN, GPIO.IN)

# Optional: pygame setup (if you prefer pygame)
# pygame.mixer.init()
# pygame.mixer.music.load(WAV_FILE)

print("Monitoring GPIO pin", INPUT_PIN)

try:
    while True:
        input_state = GPIO.input(INPUT_PIN)
        if input_state == GPIO.HIGH:
            print("HIGH voltage detected!")
            # Option 1: Using aplay
            os.system(f"aplay {WAV_FILE}")

            # Option 2: Using pygame
            # if not pygame.mixer.music.get_busy():
            #     pygame.mixer.music.play()

        else:
            print("LOW voltage detected.")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
