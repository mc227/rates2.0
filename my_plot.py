import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import requests
import json

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x_vals = []
y_vals = {}

def animate(i):
    response = requests.get('http://127.0.0.1:5000/api/data')
    data = json.loads(response.content)
    x_vals.append(time.time())  # add current time to x values
    
    for interface, interface_data in data.items():
        if interface not in y_vals:
            y_vals[interface] = []
        y_vals[interface].append(interface_data['bytesPerSec'])  # add bytesPerSec to y values for the interface
    
    ax1.clear()
    for interface, y_vals_interface in y_vals.items():
        ax1.plot(x_vals, y_vals_interface, label=interface)
    ax1.legend()
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Bytes per second')
    ax1.set_title('Bytes per second over time for all interfaces')

ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
