from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
from gpiozero import CPUTemperature
import csv

plt.style.use('fivethirtyeight')

# Initialize data lists for CPU and RAM usage
x_vals = [i for i in range(100)]
y_cpu_vals = [0] * 100
y_ram_vals = [0] * 100

# Initialize data lists for CPU temperature
y_temp_vals = [0] * 100

# Count for x-axis (not used in this version)
index = count()

# CSV file path
file_path = 'cpu_ram_temp_usage.csv'

def animate(i):
    global y_cpu_vals, y_ram_vals, y_temp_vals
    
    # Get CPU and RAM usage
    cpu_percent = psutil.cpu_percent(interval=0.001)
    ram_percent = psutil.virtual_memory().percent
    
    # Get CPU temperature
    cpu_temperature = CPUTemperature().temperature
    
    # Update CPU and RAM data lists
    y_cpu_vals.append(cpu_percent)
    y_cpu_vals = y_cpu_vals[1:]  # Keep fixed length
    y_ram_vals.append(ram_percent)
    y_ram_vals = y_ram_vals[1:]  # Keep fixed length
    
    # Update CPU temperature data list
    y_temp_vals.append(cpu_temperature)
    y_temp_vals = y_temp_vals[1:]  # Keep fixed length
    
    # Write data to CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cpu_percent, ram_percent, cpu_temperature])

    # Clear previous plots
    plt.clf()
    
    # Create subplot for CPU and RAM usage
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
    plt.plot(x_vals, y_cpu_vals, label='CPU')
    plt.plot(x_vals, y_ram_vals, label='RAM')
    plt.ylim(0, 100)  # Set y-axis limits from 0 to 100
    plt.legend()  # Show legend
    
    # Create subplot for CPU temperature
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
    plt.plot(x_vals, y_temp_vals, label='CPU Temp', linestyle='--', color='red')
    plt.ylim(0, 100)  # Set y-axis limits for temperature plot
    plt.legend()  # Show legend

# Create animation
ani = FuncAnimation(plt.gcf(), animate, interval=100)

# Set plot title, labels, and layout
plt.suptitle("CPU/RAM Usage and CPU Temperature Over Time")
plt.xlabel("Time (ticks)")
plt.ylabel("Percentage (%)")
plt.tight_layout()

# Display plot
plt.show()
