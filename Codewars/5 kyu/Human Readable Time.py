def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_new = seconds - (hours * 3600 + minutes * 60)
    return "{0:02}:{1:02}:{2:02}".format(hours,minutes,seconds_new)

print(make_readable(1))
