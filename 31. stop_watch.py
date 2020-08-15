import time

laps = 0
input('Press Enter to start.')
initial_time = time.time()
while True:
    laps += 1
    time_1 = time.time()
    input('Press Enter.')
    time_2 = time.time()
    print(f'Number of laps: {str(laps)}')
    print(f'Lap time: {str(round(time_2 - time_1, 2))}')
    print(f'Total time: {str(round(time_2 - initial_time, 2))}')
    print()
    
