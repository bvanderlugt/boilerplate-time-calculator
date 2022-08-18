days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]


def add_time(start, duration, *day):
    sm = _convert_to_minutes(start)
    dm = _convert_to_minutes(duration)
    tm = sm + dm

    # get the number of days and the remaining minutes
    i = divmod(tm, 60*24)
    new_time_str = _convert_to_twelvehour(i[1])
    ret = f"{new_time_str}"

    if len(day) > 0:
        cap_day = day[0].capitalize()
        new_day_index = (days.index(cap_day) + i[0]) % 7
        ret += f", {days[new_day_index]}"

    if i[0] >= 1 and i[0] < 2:
        ret += " (next day)"
    elif i[0] >= 2:
        ret += f" ({i[0]} days later)"

    return ret


def _convert_to_twelvehour(m):
    '''
    takes minutes (int) and returns time of day (string) in format "12:01 PM"
    '''
    if m > 60*24:
        raise ValueError(f"m cannot exceed maximum minutes in a day ({60*24}) \
                got: {m}")
    t = divmod(m, 60)
    minute = t[1]
    hour = t[0] % 12
    hour = 12 if hour == 0 else hour
    phase = "PM" if t[0] > 11 else "AM"
    return f"{hour}:{minute:0>2} {phase}"


def _convert_to_minutes(t):
    '''
    takes a time in 12 hour format (string) and gives minutes in day (int)
    '''
    parts = _split_twelve_hour(t)
    if parts[2] is None:
        return int(parts[0])*60 + int(parts[1])

    hours = int(parts[0]) if parts[2] == "AM" else int(parts[0]) + 12
    return hours*60 + int(parts[1])


def _split_twelve_hour(t):
    '''
    splits twelve hour time and returns tuple [hour, minute, phase]
    input: "12:01 PM"
    returns: tuple ("12", "01", "PM")
    '''
    if "AM" in t or "PM" in t:
        a = t.split()
        b = a[0].split(':')
        b.append(a[1])
        return tuple(b)
    else:
        a = t.split(':')
        a.append(None)
        return tuple(a)
