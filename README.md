# Project 1 - Pendulum

This project includes a simulated pendulum which outputs graphs of theta vs time, angular velocity vs time, and angular acceleration vs time, as well as calculating the period of the pendulum.

This project also includes a way to collect data from a real pendulum (with a micro:Bit attached) and graph the relationship between theta and time along with angular acceleration. It also calculates the period of oscillation of the pendulum.

There is also included code that will analyze the relationship between the periods of oscillation calculated between the simulated and collected data of pendulums at specific lengths: .447 m, .413 m, .346 m, .298 m, and .225 m.

This real-life data is included in the text files "real_pendulum_data#.txt".


## Instructions

To run simulation data:

Run Pendulum_Sim_Graphs.py

Input length on line 6 as shown:
```
l = 1                                   #input length of pendulum here
```


To collect real world data from microbit:

Run Pendulum_Data_Collection.py on the microbit, pressing the B button on the microbit to start collecting data.
Data is collected while the center LED is on.
This data is save in a file called 'real_pendulum_data9.txt' where 9 is replaced by a random number.

Use Spyder_Data_Reader.py to graph the data collected by the microbit
ti use the correct file number, place that number in 'a' as shown below (example is if file name is 'real_pendulum_data9.txt')
```
a = 9                                                      
fin = open('real_pendulum_data' + str(a) + '.txt')
```
