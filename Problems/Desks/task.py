# put your python code here

group_one = abs(int(input()))
group_two = abs(int(input()))
group_three = abs(int(input()))

desk_one = ((group_one // 2) + group_one % 2)
desk_two = ((group_two // 2) + group_two % 2)
desk_three = ((group_three) // 2 + group_three % 2)

print(desk_one + desk_two + desk_three)