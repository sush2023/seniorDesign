import csv
import sys
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

iteration = 0
while True:
    inp = input("Press Enter to Start")
    serial_trigger = '89'
    #match arduino baud rate and set COM port
    serialport = serial.Serial('COM3', 115200, timeout=1)
    temp = []
    #number of samples should be equal to arduino code
    tim = list(range(50000))
    serialport.write(serial_trigger.encode())
    while True:
        try:
            # Read data from the serial port
            data = serialport.readline().decode('utf-8', errors='replace').strip()
            print(data)
            #only append voltage values
            if(data.isnumeric()):
                temp.append(float(data))
                print(data)
            #reached end of transmission
            if "Complete" in data:
                print("Done")
                break

        except UnicodeDecodeError as e:
            print(f"Error decoding data: {e}")

        # Add a delay to control the data capture rate
        #time.sleep(0.25)

    serialport.close()
    print(tim[-1]-tim[0])
    print(temp)

    plt.plot(tim, temp)
    plt.show()
    plt.close()

    # Specify the file path
    csv_file_path = f"output{iteration}.csv"

    # Writing to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for i, val in enumerate(temp):
            csv_writer.writerow([i, val])

    iteration += 1
    print(f"Done writing CSV file: {csv_file_path}")

