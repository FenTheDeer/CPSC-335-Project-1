from rich import print

def merge_two_sorted_lists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def timeScheduler(list_schedules: list, list_daily_acts: list, duration: int):
    duration = float(duration)/60
    
    #merge lists of schedules into one list
    while len(list_schedules) > 1:
        merged_lists = []
        for i in range(0, len(list_schedules), 2):
            if i + 1 < len(list_schedules):
                merged_lists.append(merge_two_sorted_lists(list_schedules[i], list_schedules[i + 1]))
            else:
                merged_lists.append(list_schedules[i])
        list_schedules = merged_lists
    list_schedules = list_schedules[0]
    
    # start is the max of a_login[0] and b_login[0]
    # end is the min of a_login[1] and b_login[1]
    start = max(act[0] for act in list_daily_acts)
    end = min(act[1] for act in list_daily_acts)
    
    #add final event to schedule at logoff time
    list_schedules.append([end, end])

    #create result list, and indexes for a_times and b_times
    result = []
    idx = 0

    while idx < len(list_schedules):
        # current a and b intervals are separated into a_start/b_start and a_end/b_end
        curr_start, curr_end = list_schedules[idx]

        # if a_end < start, then a interval is before the start
        if curr_start < start:
            idx += 1
            start = max(curr_end, start)
            continue
        
        # check if there is a big enough gap in the schedule
        if min(curr_start, end) - start >= duration:
            result.append([start, min(curr_start, end)])

        # update start to the end of the interval that ends first
        start = curr_end
        idx += 1
        
        #if we're past logoff time, then end the loop
        if curr_start > end:
            break
    
    return [[str(int(a[0])) + ":" + str(int((a[0] - int(a[0]))*60)).zfill(2), str(int(a[1])) + ":" + str(int((a[1] - int(a[1]))*60)).zfill(2)] for a in result]

def formatLists(schedules, dailyActs):
    print(schedules, dailyActs)
    schedules = [[[(lambda pair: int(pair[0]) + (int(pair[1]) / 60))(l.split(":")), (lambda pair: int(pair[0]) + (int(pair[1]) / 60))(r.split(":"))] for l, r in sched] for sched in schedules]
    dailyActs = [[float(time.split(':')[0]) + float(time.split(':')[1]) / 60 for time in sublist] for sublist in dailyActs]
    print(schedules, dailyActs)
    return schedules, dailyActs

#This is placed here to read the input file
#Will complete once we've determined how to account for more than 2 people.
input = open('input.txt', 'r')
Lines = input.readlines()


case1 = """
duration_of_meeting = 30
# person1_Schedule = [['7:00', '8:30'],  ['12:00', '13:00'],  ['16:00', '18:00']]
# person1_DailyAct = ['9:00', '19:00']

# person2_Schedule = [['9:00', '10:30'],  ['12:20', '13:30'],  ['14:00', '15:00'], ['16:00', '17:00' ]]
# person2_DailyAct = ['9:00', '18:30']

# person3_Schedule = [['8:00', '9:00'],  ['12:00', '13:00'],  ['16:00', '17:00']]
# person3_DailyAct = ['11:00', '18:00']
schedules = [[['7:00', '8:30'],  ['12:00', '13:00'],  ['16:00', '18:00']], [['9:00', '10:30'],  ['12:20', '13:30'],  ['14:00', '15:00'], ['16:00', '17:00']], [['8:00', '9:00'],  ['12:00', '13:00'],  ['16:00', '17:00']]]
dailyActs = [ ['9:00', '19:00'], ['9:00', '18:30'], ['11:00', '18:00'] ]
"""
print(input)

for line in case1.splitlines():
    exec(line)
    


# schedules = [person1_Schedule, person2_Schedule, person3_Schedule]
# dailyActs = [person1_DailyAct, person2_DailyAct, person3_DailyAct]
# duration_of_meeting = 30

schedules, dailyActs = formatLists(schedules, dailyActs)

print(timeScheduler(schedules, dailyActs, duration_of_meeting))