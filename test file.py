import microbit

with open('datatest.txt', 'w') as my_file:
    for i in range(20):
        #x = str(microbit.accelerometer.get_values())
        my_file.write('hello\r\n')
        microbit.sleep(500)