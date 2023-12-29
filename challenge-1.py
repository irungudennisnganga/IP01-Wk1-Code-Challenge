
def Converting_12_hour_time_to_24_hou_time(hour,minutes,period):
    if period == "AM":
        if hour == 12:
            hour = 0
       
    else :
        if hour != 12:
            hour += 12
       
    return f"{hour}{minutes}"


print(Converting_12_hour_time_to_24_hou_time(8,20,"PM"))