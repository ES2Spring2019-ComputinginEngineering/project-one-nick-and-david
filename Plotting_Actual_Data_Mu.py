import math

theta_list = []
angular_acc_list = []
cut = 0

g = -1000                                                    #Microbit gravity constant
a = 66                                                       #Fill to find file number
fin = open('real_pendulum_data' + str(a) + '.txt')

for line in fin:
    number = line.strip()
    angular_acc_list.append(int(number))
    theta = math.asin(int(number)/g)                        #Find theta by using gravity and y-acc
    theta_list.append(theta*(180/(math.pi)))


x = 0
for item in angular_acc_list:
    acc = (angular_acc_list[x])/100
    print((acc, theta_list[x]))
    x = x + 1