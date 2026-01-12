def categorized_distance(distance):
if distance<=5:
    return "Local"
elif 6<=distance<=20:
    return"city"
else:
    return"out of station"
distance=float("Enter delivery distance in km:")
