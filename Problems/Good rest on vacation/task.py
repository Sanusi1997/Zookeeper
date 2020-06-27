# put your python code here

duration_in_days = int(input())
total_food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

expenses = (duration_in_days * total_food_cost) + (flight_cost * 2) + ((duration_in_days - 1) * hotel_cost)

print(expenses)