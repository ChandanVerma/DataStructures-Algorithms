## Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
n = int(input())
odd_list = [val for val in range(1, n) if (val % 2 !=0)]
print(odd_list)