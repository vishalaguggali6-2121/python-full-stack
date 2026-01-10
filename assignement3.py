visitors=[120,150,80,40,200,130,90]
highest_traffic=max(visitors)
highest_day=visitors.index(highest_traffic)+1
lowest_traffic=min(visitors)
lowest_day=visitors.index(lowest_traffic)
print("Highest traffic day:",highest_day,"wiht",highest_traffic,"visitors")
print("lowest traffic day :",lowest_day,"with",lowest_traffic,"visitors")
