# put your python code here

hour_one = (int(input()) * 3600)
minute_one = (int(input()) * 60)
second_one = int(input())

time_one = hour_one + minute_one + second_one

hour_two = (int(input()) * 3600)
minute_two = (int(input()) * 60)
second_two = int(input())

time_two = hour_two + minute_two + second_two

difference = abs(time_one - time_two)


print(difference)