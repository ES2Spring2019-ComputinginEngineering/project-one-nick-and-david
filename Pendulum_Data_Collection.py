import microbit
import random

a = str(random.randint(1, 100))

while True:
    if microbit.button_a.was_pressed() == True:                         # waits for button_a pressed
        microbit.sleep(3000)                                            # 3 second delay
        with open('real_pendulum_data' + a + '.txt', 'w') as my_file:   # makes file 1 to 100
            for i in range(400):                                        # 400 * .025 seconds = 10 seconds (close!)
                microbit.display.set_pixel(2, 2, 9)                     # indicator that it is recording
                microbit.sleep(25)                                      # sleep at 25 milliseconds
                y = str(microbit.accelerometer.get_y())                 # writes data in folder (only y)
                my_file.write(y + '\n')                                 # new lines
    microbit.display.set_pixel(2, 2, 0)                                 # not recording