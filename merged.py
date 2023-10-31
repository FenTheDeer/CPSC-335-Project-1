def timeScheduler(list_schedules, list_daily_acts, duration: int):
    duration = float(duration)/60

    schedules = []
    
    while list_schedules:
        min_vals = [lst[0] for lst in list_schedules]
        min_index = min(range(len(min_vals)), key=min_vals.__getitem__)
        schedules.append(list_schedules[min_index].pop(0))
        
        if not list_schedules[min_index]:
            list_schedules.pop(min_index)
    

# Example usage:
    print(schedules)

    for start, end in list_schedules:
        start = start.split(":")
        start = float(start[0]) + float(start[1])/60
        end = end.split(":")
        end = float(end[0]) + float(end[1])/60
        schedules.append([start, end])
    print (schedules)
    print(list_daily_acts)
    
    list_daily_acts = [[float(time.split(':')[0]) + float(time.split(':')[1]) / 60 for time in sublist] for sublist in list_daily_acts]
    print(list_daily_acts)


    # start is the max of a_login[0] and b_login[0]
    # end is the min of a_login[1] and b_login[1]
    start = max(act[0] for act in list_daily_acts)
    end = min(act[1] for act in list_daily_acts)

    #add final event to schedule at logoff time
    schedules.append([end, end])

    #create result list, and indexes for a_times and b_times
    result = []
    idx = 0


    while idx < len(schedules):
        # current a and b intervals are separated into a_start/b_start and a_end/b_end
        curr_start, curr_end = schedules[idx]
        

        # if a_end < start, then a interval is before the start
        if curr_end < start:
            idx += 1
            continue
        
        # check if there is a big enough gap in the schedule
        if min(curr_start, end)-start >= duration:
            result.append([start, min(curr_start, end)])
        
        # update start to the end of the interval that ends first
        idx += 1
        
        #if we're past logoff time, then end the loop
        if curr_start > end:
            break
    
    return [[str(int(a[0])) + ":" + str(int((a[0] - int(a[0]))*60)).zfill(2), str(int(a[1])) + ":" + str(int((a[1] - int(a[1]))*60)).zfill(2)] for a in result]


#This is placed here to read the input file
#Will complete once we've determined how to account for more than 2 people.
input = open('input.txt', 'r')
Lines = input.readlines()

person1_Schedule = [['7:00', '8:30'],  ['12:00', '13:00'],  ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']

person2_Schedule = [['9:00', '10:30'],  ['12:20', '13:30'],  ['14:00', '15:00'], ['16:00', '17:00' ]]
person2_DailyAct = ['9:00', '18:30']

duration_of_meeting = 30


schedules = [person1_Schedule, person2_Schedule]
list_schedules = [lst for lst in schedules]

dailyActs = [person1_DailyAct, person2_DailyAct]
list_dailyActs = [act for act in dailyActs]

#print(list_dailyActs)


print(timeScheduler(list_schedules, list_dailyActs, duration_of_meeting))