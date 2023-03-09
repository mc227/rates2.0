"""
prototype of live line chart made with matplotlib
"""
import time
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
x_vals = []
y_vals_bytes = {}
y_vals_packets = {}

def animate(i):
    response = requests.get('http://127.0.0.1:5000/api/data')
    data = json.loads(response.content)
    x_vals.append(time.time())  # add current time to x values
    
    for interface, interface_data in data.items():
        if interface not in y_vals_bytes:
            y_vals_bytes[interface] = []
            y_vals_packets[interface] = []
        y_vals_bytes[interface].append(interface_data['bytesPerSec'])  # add bytesPerSec to y values for the interface
        y_vals_packets[interface].append(interface_data['packetsPerSec'])  # add packetsPerSec to y values for the interface
    
    ax1.clear()
    ax2.clear()
    for interface, y_vals_interface in y_vals_bytes.items():
        ax1.plot(x_vals, y_vals_interface, label=interface)
    for interface, y_vals_interface in y_vals_packets.items():
        ax2.plot(x_vals, y_vals_interface, label=interface)
    ax1.legend()
    ax2.legend()
    ax1.set_xlabel('Time (s)')
    ax2.set_xlabel('Time (s)')
    ax1.set_ylabel('Bytes per second')
    ax2.set_ylabel('Packets per second')
    ax1.set_title('Bytes per second over time for all interfaces')
    ax2.set_title('Packets per second over time for all interfaces')

ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
