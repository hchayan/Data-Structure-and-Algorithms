def timeConversion(s):
    if int(s[:2]) == 12:
        s = '00' + s[2:]

    if s[len(s) - 2:] == 'PM':
        s = str(int(s[:2]) + 12) + s[2:]

    return s[:len(s)-2]

print(timeConversion('12:59:59AM'))