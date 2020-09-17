
import matplotlib.pyplot as plt
import random


arrows_x_origin = []
for index in range(0, 10):
    arrows_x_origin.append(0)

arrows_y_origin = []
for index in range(0, 10):
    arrows_y_origin.append(0)

arrows_x_tip = []
for index in range(0, 10):
    if bool(random.getrandbits(1)):
        arrows_x_tip.append(-random.uniform(1, 10))
    else:
        arrows_x_tip.append(random.uniform(1, 10))

arrows_y_tip = []
for index in range(0, 10):
    if bool(random.getrandbits(1)):
        arrows_y_tip.append(-random.uniform(1, 10))
    else:
        arrows_y_tip.append(random.uniform(1, 10))

plt.quiver(arrows_x_origin, arrows_y_origin, arrows_x_tip, arrows_y_tip,
           angles='xy', scale_units='xy', scale=1, color=['r', 'g', 'b'])
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()