import board

# Example to demonstrate interrupt handling.
# This particular example requires gpiozero or another GPIO library.

from signal import pause
from gpiozero import Button
from adafruit_cap1188.i2c import CAP1188_I2C

# GPIO pin for interrupt
INT_PIN = 22

i2c = board.I2C()
cap = CAP1188_I2C(i2c)

# Set alert polarity to active low/open drain
cap.alert_polarity = True
# Do not interrupt on release
cap.interrupt_on_release = False

for i in range (1, 9):
    # enable interrupts
    cap[i].interrupt_enabled = True
    # do not trigger repeat interrupts
    cap[i].interrupt_repeat = False

# Clear any pending interrupts
cap.clear_interrupt()

def callback():
    # Code to handle interrupts goes here
    pins = cap.touched_pins
    print(f"Interrupt: {pins}")

# You can reverse the direction of current by changing both cap.alert_polarity and pull_up to False.
cap_int = Button(INT_PIN, pull_up=True)
# Tie the callback to interrupt pin
cap_int.when_pressed = callback

print("Waiting for interrupts...")
pause()

# Here you can resume the program flow
