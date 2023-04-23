import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

time_passing_cars = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
speed = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# make a polynomial model
model = numpy.poly1d(numpy.polyfit(time_passing_cars, speed, 3))

# predict the speed of a car that passes ot 17.00
predicted_speed = model(17)
print(predicted_speed)

# get the relationship score
# related = r2_score(speed, model(time_passing_cars))
# print(related)

# line display, start at 1 and end at 22
# line = numpy.linspace(1, 22, 200)

# plt.scatter(time_passing_cars, speed)
# draw the ploynomial line
# plt.plot(line, model(line))
# plt.show()