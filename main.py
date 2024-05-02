def getHoursMinutesSeconds(totalSeconds):
    hours = 0
    minutes = 0

    if totalSeconds == 0:
        return "0s"

    if totalSeconds >= 3600:
        # division to get the integer part that corresponds to the hours
        hours = totalSeconds // 3600
        totalSeconds = totalSeconds % 3600

    if totalSeconds >= 60:
        minutes = totalSeconds // 60
        totalSeconds = totalSeconds % 60

    seconds = totalSeconds

    conversion = []

    if hours > 0:
        conversion.append(str(hours) + "h")

    if minutes > 0:
        conversion.append(str(minutes) + "m")

    if seconds > 0:
        conversion.append(str(seconds) + "s")

    return ' '.join(conversion)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
