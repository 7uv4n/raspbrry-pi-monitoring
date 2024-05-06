from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil

plt.style.use('fivethirtyeight')

x_vals = [i for i in range(0, 100)]
y_cpu_vals = [0 for _ in range(0, 100)]
y_ram_vals = [0 for _ in range(0, 100)]

index = count()


def animate(i):
    global y_cpu_vals, y_ram_vals
    
    cpu_percent = psutil.cpu_percent(interval=0.001)
    ram_percent = psutil.virtual_memory().percent
    
    y_cpu_vals.append(cpu_percent)
    y_cpu_vals = y_cpu_vals[1:]  # Truncate CPU list to keep fixed length
    
    y_ram_vals.append(ram_percent)
    y_ram_vals = y_ram_vals[1:]  # Truncate RAM list to keep fixed length
    
    plt.cla()  # Clear previous plot
    plt.plot(x_vals, y_cpu_vals, label='CPU')
    plt.plot(x_vals, y_ram_vals, label='RAM')
    plt.ylim(0, 100)  # Set y-axis limits from 0 to 100
    plt.legend()  # Show legend


ani = FuncAnimation(plt.gcf(), animate, interval=100, cache_frame_data=False)
plt.title("CPU and RAM Usage Over Time")
plt.xlabel("Time (ms)")
plt.ylabel("Percentage (%)")

plt.tight_layout()
plt.show()
