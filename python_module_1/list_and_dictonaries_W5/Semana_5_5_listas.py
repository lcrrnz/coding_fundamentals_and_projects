#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

#86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

counter = 1

expected_numbers = int(input("how many numbers are you adding?"))

my_list = []

highest = 0

while counter <= expected_numbers:
    my_list.append(int(input(f'Add value #{counter}: ')))
    counter += 1

print(my_list)

for number in my_list:
    if number > highest:
        highest = number

print(f'The highest number is {highest}')

#another, another way
expected_numbers = int(input("how many items are you adding?"))
my_bike_list = []

counter = 1

while counter <= expected_numbers:
    my_bike_list.append(input(f'Add bike #{counter}: '))
    counter += 1
print(f'This my list of the best bikes {my_bike_list}')

my_bike_list[0],my_bike_list [-1] = my_bike_list [-1], my_bike_list [0]

print(f'The new list is {my_bike_list}')