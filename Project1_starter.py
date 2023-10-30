def timeScheduler(a_schedule, b_schedule, a_login: list, b_login: list, duration: int):
    duration = float(duration)/60
    a_times = []
    for start, end in a_schedule:
        start = start.split(":")
        start = float(start[0]) + float(start[1])/60
        end = end.split(":")
        end = float(end[0]) + float(end[1])/60
        a_times.append([start, end])
    
    b_times = []
    for start, end in b_schedule:
        start = start.split(":")
        start = float(start[0]) + float(start[1])/60
        end = end.split(":")
        end = float(end[0]) + float(end[1])/60
        b_times.append([start, end])
    
    a_login = [float(int(hour) + int(minutes)/60) for hour, minutes in [a.split(":") for a in a_login]]
    b_login = [float(int(hour) + int(minutes)/60) for hour, minutes in [b.split(":") for b in b_login]]
    
    #add final event to schedule at logoff time
    a_times.append([a_login[1], a_login[1]])
    b_times.append([b_login[1], b_login[1]])

    # start is the max of a_login[0] and b_login[0]
    # end is the min of a_login[1] and b_login[1]
    start = max(a_login[0], b_login[0])
    end = min(a_login[1], b_login[1])

    #create result list, and indexes for a_times and b_times
    result = []
    idx_a = 0
    idx_b = 0

    while idx_a < len(a_times) and idx_b < len(b_times):
        # current a and b intervals are separated into a_start/b_start and a_end/b_end
        a_start, a_end = a_times[idx_a]
        b_start, b_end = b_times[idx_b]

        # if a_end < start, then a interval is before the start
        if a_end < start:
            idx_a += 1
            continue

        # if b_end < start, then b interval is before the start
        if b_end < start:
            idx_b += 1
            continue
        
        # check if there is a big enough gap in the schedule
        if min(a_start, b_start, end)-start >= duration:
            result.append([start, min(a_start, b_start, end)])
        
        # update start to the end of the interval that ends first
        if a_end < b_end:
            start = a_end
            idx_a += 1
        else:
            start = b_end
            idx_b += 1
        
        #if we're past logoff time, then end the loop
        if a_start > end or b_start > end:
            break
    
    return result




person1_Schedule = [['7:00', '8:30'],  ['12:00', '13:00'],  ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']

person2_Schedule = [['9:00', '10:30'],  ['12:20', '13:30'],  ['14:00', '15:00'], ['16:00', '17:00' ]]
person2_DailyAct = ['9:00', '18:30']
duration_of_meeting = 30

print(timeScheduler(person1_Schedule, person2_Schedule, person1_DailyAct, person2_DailyAct, duration_of_meeting))