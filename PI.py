from numpy import random
import math
import matplotlib.pyplot as plt


######################## Graph Set-Up ########################
fig, (ax1, ax2) = plt.subplots(1, 2) 
plt.ion()

######################## graph1 = PI approximation ########################
itr_values = []
pi_aprox_values = []

best_approx = 0
best_approx_diff = math.inf


ax1.axhline(math.pi, color = 'r') 


fig.suptitle(best_approx)
  





######################## graph = Random dots over Circle inscribed in a Square ########################

Circle_x_values = []
Circle_y_values = []
not_Circle_x_values = []
not_Circle_y_values = []


circle = plt.Circle((0, 0), 1, color='black', fill=False)
square = plt.Rectangle((-1, -1), 2, 2, color='black', fill=False)
ax2.add_patch(circle)
ax2.add_patch(square)


plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)





######################## Main ########################
suc = 0 # success = in circle
n = 1 # number of guesses
i = 1 # itrator used to determine frame rate
frame_rate = int(input('enter frame rate (number of guesses claculated before draw)\n')) # draw after frame_rate guesses

while True:
    x = random.uniform(-1,1)   
    y = random.uniform(-1,1)      
    r = x * x + y * y
    if r <= 1: # inside the circle
        Circle_x_values.append(x)
        Circle_y_values.append(y)
        suc += 1
        diff = abs(math.pi - suc/n*4)
        if diff < best_approx_diff:
            best_approx = suc/n*4
            best_approx_diff = diff
            fig.suptitle(best_approx)
        itr_values.append(n)
        pi_aprox_values.append(suc/n*4)
    else: # not inside the circle
        not_Circle_x_values.append(x)
        not_Circle_y_values.append(y)
    ######################## Draw after frame_rate itr ########################
    if (i == frame_rate): 
        ax1.plot(itr_values,pi_aprox_values, color = 'blue')
        ax2.scatter(Circle_x_values, Circle_y_values, color = 'green', s = 0.1)
        ax2.scatter(not_Circle_x_values, not_Circle_y_values, color = 'red', s = 0.1)
        plt.draw()
        ax1.set_title(suc/n*4)
        plt.pause(0.001)
        i = 0
    n += 1
    i += 1
