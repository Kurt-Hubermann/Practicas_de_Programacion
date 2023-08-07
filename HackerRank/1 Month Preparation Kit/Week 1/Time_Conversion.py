def timeConversion(s):
    # Write your code here
    hour = s[:2]
    min = s[3:5]
    sec = s[6:8]
    format = s[8:10]
    if format == 'AM':
        if hour == '12':
            hour = '00'
        return(hour + ':' + min + ':' + sec)
    elif format == 'PM':
        if int(hour) < 12:
            hour = str((int(hour) + 12))
        return(hour + ':' + min + ':' + sec)

if __name__ == '__main__':
    s = '12:01:00AM'
    res = timeConversion(s)
    print(res)