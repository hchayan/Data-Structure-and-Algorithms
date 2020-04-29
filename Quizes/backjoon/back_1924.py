import time

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = input().split()

print(days[int(time.strftime('%j', time.strptime('2017-'+m+'-'+d, "%Y-%m-%d")))%7])
