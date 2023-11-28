import matplotlib.pyplot as plt
import numpy as np
import os
import ast
import shutil
import gzip

def graph():
    rate = 250
    
    print("readings")
    # to navigate inside the readings directory
    os.chdir('readings/')
    
    for file in os.scandir():
        # Check whether file is in text format or not
        if file.name.endswith(".txt.gz"):
            # Read data from file
            with gzip.open(file.path, 'rb') as f:
                
                stationname = f.readline().rstrip().decode('utf-8')
                print(stationname)
                datatype = f.readline().rstrip().decode('utf-8')
                date = f.readline().rstrip().decode('utf-8')
                pressure = f.read().decode('utf-8')
                pressure = ast.literal_eval(pressure)
                pressure = np.array([float(x) for x in pressure])

                # print(pressure)
                # pressure = ast.literal_eval(pressure)
            # Calculate time array
            duration = len(pressure) / rate
            time = np.arange(0, duration, 1 / rate)
            # # print("time")
            # Plot data
            plt.figure(figsize=(18, 6))
            plt.plot(time, pressure)
            plt.xlabel('Time(s)')
            plt.ylabel('Pressure')
            # print("time")
            timestamp = date[0:10]+'_'+date[11:13]+date[14:16]+date[17:26]
            plt.title(f'{stationname}\n{datatype}\non {date}')
            # print("save")
            plt.savefig(f'images/pressure_data_{stationname}_{timestamp}.jpeg', bbox_inches='tight', dpi=100)
            # print("time")
            print("success")
            plt.close()
            
            #move files to another folder once the graphs are generated        
            try:
                if file.name.endswith(".txt.gz"):
                    file_path = os.path.abspath(file)
                    print(file_path)  
                    target = 'generatedgraph/'
                    shutil.move(file_path,target)
                    
            except: 
                print("Error! Can not move files")

graph()