n = int(input("Enter the length of the sequence: ")) # Do not change this line
number_1 = 0
number_2 = 1
number_3 = 0
number_sum = 0
for i in range(n):
    number_sum = number_1 + number_2 + number_3
    number_1 = number_2
    number_2 = number_3
    number_3 = number_sum
    print(number_sum)
