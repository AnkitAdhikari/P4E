# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).


def computepay(hrs, rate):
    if hrs > 40:
        return (hrs - 40) * 1.5 * rate + 40 * rate
    return hrs * rate


try:
    hours = int(input("Enter hours: "))
    rate = int(input("Enter rate: "))

    print(computepay(hours, rate))
except:
    print("Enter numeric value")
