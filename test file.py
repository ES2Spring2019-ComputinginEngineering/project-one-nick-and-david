import microbit
import random
a = str(random.randint(0, 1000))

with open('test' + a + '.txt', 'w') as my_file:
    for i in range(200):
        microbit.display.set_pixel(2, 2, 9) #indicator that it is recording
#        t0 = microbit.running_time()
        microbit.sleep(100)
#      t1 = microbit.running_time()
#     dt = str(t1-t0)
        x = str(microbit.accelerometer.get_values())
        my_file.write(x + '\r\n')
microbit.display.set_pixel(2, 2, 0) #not recording