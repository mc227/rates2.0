import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import requests
import json

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x_vals = []
y_vals_eth0 = []
y_vals_eth1 = []
y_vals_eth2 = []

def animate(i):
    response = requests.get('http://127.0.0.1:5000/api/data')
    data = json.loads(response.content)
    x_vals.append(time.time())  # add current time to x values
    y_vals_eth0.append(data['eth0']['bytesPerSec'])  # add bytesPerSec to y values for eth0
    y_vals_eth1.append(data['eth1']['bytesPerSec'])  # add bytesPerSec to y values for eth1
    y_vals_eth2.append(data['eth2']['bytesPerSec'])  # add bytesPerSec to y values for eth2
    ax1.clear()
    ax1.plot(x_vals, y_vals_eth0, label='eth0')
    ax1.plot(x_vals, y_vals_eth1, label='eth1')
    ax1.plot(x_vals, y_vals_eth2, label='eth2')
    ax1.legend()
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Bytes per second')
    ax1.set_title('eth0, eth1, and eth2 bytes per second over time')

ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
