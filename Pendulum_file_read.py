import math
g = 1000                                                    #Microbit gravity constant
a = 66      #Fill to find file number
fin = open('real_pendulum_data' + str(a) + '.txt')          #opening file

for line in fin:
    number = line.strip()
    theta = math.asin(int(number)/g)                        #Find theta by using gravity and y-acc
    print(theta*(180/(math.pi)))                            #Covert to degrees