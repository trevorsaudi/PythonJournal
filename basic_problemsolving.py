# finding the average of n numbers
num = int(input("How many numbers? "))
total_sum =  0

for n in range (num):
    numbers = float(input("Enter any number"))
    total_sum += numbers

print(total_sum/num)