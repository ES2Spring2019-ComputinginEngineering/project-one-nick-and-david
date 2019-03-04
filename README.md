# Project 1 - Pendulum

Short project description here

## Instructions

Describe how to use your code.

To run simulation data:

Run Spyder_code.py
Input length on line 6 as shown:
```
l = 1                                   #input length of pendulum here
```


To collect real world data from microbit:

Run Pendulum_Data_Collection.py on the microbit, pressing the B button on the microbit to start collecting data.
Data is collected while the center LED is on.
This data is save in a file called 'real_pendulum_data9.txt' where 9 is replaced by a random number.

Use Spyder_data_reader.py to graph the data collected by the microbit
ti use the correct file number, place that number in 'a' as shown below (example is if file name is 'real_pendulum_data9.txt')
```
a = 9                                                      
fin = open('real_pendulum_data' + str(a) + '.txt')
```
