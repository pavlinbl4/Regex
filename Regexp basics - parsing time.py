import re

def to_seconds(time):
    if bool(re.match(r'^(\d\d)\:(([0-4]\d)|(5\d))\:(([0-4]\d)|(5\d))\Z', time)):
        time_list = (time.split(':'))
        return int(time_list[2]) + int(time_list[1]) * 60 + int(time_list[0])*3600
    return None



print(to_seconds('00:00:00\n'))