
def print_list (num):
    num_list = range (1,num+1)
    for i in num_list:
        print(i, i ** 2, i ** 3) # ** is exponential

num = int(input("Enter a number: "))
print_list(num)