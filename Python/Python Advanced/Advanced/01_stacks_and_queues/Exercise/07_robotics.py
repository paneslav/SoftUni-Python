from collections import deque
import datetime

def convert_time(seconds):
    a=seconds//3600
    b=(seconds%3600)//60
    c=(seconds%3600)%60
    d=f'{a:02d}:{b:02d}:{c:02d}'
    return d


rbts = [x.split('-') for x in input().split(';')]
time = input().split(':')

hours = int(time[0])
minutes = int(time[1])
seconds = int(time[-1])
starting_time_secs = (hours * 3600) + (minutes * 60) + seconds
robots_info = {}
free_robots = [x[0] for x in rbts]
recharging_robots = {}
products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

for robot in rbts:
    robot_name = robot[0]
    downtime = int(robot[-1])
    robots_info[robot_name] = downtime

while products:
    if starting_time_secs < 86399:
        starting_time_secs += 1
    else:
        starting_time_secs = 0

    current_product = products.popleft()

    for key, value in list(recharging_robots.items()):
        recharging_robots[key] -= 1

        if recharging_robots[key] <= 0:
            recharging_robots.pop(key)

    for robot in free_robots:
        if robot not in recharging_robots:
            print(f"{robot} - {current_product} [{convert_time(starting_time_secs)}]")
            recharging_robots[robot] = robots_info[robot]
            break
    else:
        products.append(current_product)




    # if recharging_robots:
    #     for key, value in list(recharging_robots.items()):
    #         recharging_robots[key] -= 1
    #         if recharging_robots[key] <= 0:
    #             free_robots.append(key)
    #             recharging_robots.pop(f'{key}')
    #
    # if free_robots:
    #     print(f"{free_robots[0]} - {products.popleft()} [{str(datetime.timedelta(seconds=starting_time_secs)).zfill(8)}]")
    #     recharging_robots[free_robots[0]] = robots_info[free_robots[0]]
    #     free_robots.pop(0)
    # else:
    #     products.append(products.popleft())
