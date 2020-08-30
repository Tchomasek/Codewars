def format_duration(input):
    if input==0:
        return 'now'
    sim = 60 #seconds in a minute
    sih = 3600 #seconds in an hour
    sid = 86400 # seconds in a day
    siy = 31536000 #seconds in a year
    years=input//siy
    input-=years*siy
    days=input//sid
    input-=days*sid
    hours=input//sih
    input-=hours*sih
    minutes=input//sim
    input-=minutes*sim
    seconds=input
    print('years:', years,' days:',days,' hours:',hours,' minutes:',minutes,' seconds:', seconds)
    values=[years,days,hours,minutes,seconds]
    words=['year','day','hour','minute','second']
    result=''
    for i in range(len(values)):
        if values[i]:

            result+=str(values[i])+' '+words[i]
            if values[i]>1:
                result+='s'
            result+=', '
    result=result[:-2]

    return result



print(format_duration(3524687))






'''Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.'''
