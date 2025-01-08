def avg_speed(distance, time):
    return distance / time

distance = float(input("Distance in km: "))
time = float(input("Time in hours: "))

speed = avg_speed(distance, time)
print("Speed:", speed, "km/h")
