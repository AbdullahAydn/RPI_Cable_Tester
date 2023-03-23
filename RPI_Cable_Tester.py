import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# Define pin numbers
output_pins = [2, 3, 4, 14, 15, 18]
input_pins_1 = [17, 27, 22, 23, 24, 10]
input_pins_2 = [9, 11, 5, 6, 13, 19]

# Set up green LED
GREEN_LED = 20
GPIO.setup(GREEN_LED, GPIO.OUT)

# Set up switches
SWITCH_1 = 25
SWITCH_2 = 8
SWITCH_3 = 7
GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Wait for all switches to be turned on
while not (GPIO.input(SWITCH_1) and GPIO.input(SWITCH_2) and GPIO.input(SWITCH_3)):
    time.sleep(0.1)

# Set output pins to HIGH one at a time and check input pins
all_tests_passed = True
for i, output_pin in enumerate(output_pins):
    # Set output pin to HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(output_pin, GPIO.HIGH)
    
    # Check input pins for connector 1
    for j, input_pin in enumerate(input_pins_1):
        if j == i:
            # Corresponding pin should be HIGH
            if GPIO.input(input_pin) != GPIO.HIGH:
                all_tests_passed = False
                break
        else:
            # Non-corresponding pins should be LOW
            if GPIO.input(input_pin) != GPIO.LOW:
                all_tests_passed = False
                break
    
    # Check input pins for connector 2
    for j, input_pin in enumerate(input_pins_2):
        if j == i:
            # Corresponding pin should be HIGH
            if GPIO.input(input_pin) != GPIO.HIGH:
                all_tests_passed = False
                break
        else:
            # Non-corresponding pins should be LOW
            if GPIO.input(input_pin) != GPIO.LOW:
                all_tests_passed = False
                break
    
    # Set output pin back to LOW
    GPIO.output(output_pin, GPIO.LOW)

# Set green LED based on test results
if all_tests_passed:
    GPIO.output(GREEN_LED, GPIO.HIGH)
else:
    GPIO.output(GREEN_LED, GPIO.LOW)
    
# Clean up GPIO pins
GPIO.cleanup()
