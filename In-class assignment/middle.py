def middle(list_num):
    new_list = []
    for i in range(1,len(list_num)-1):
        new_list.append(list_num[i])
    print(new_list)

input_str = input("Enter a list of numbers: ")
# list_num = [int(x) for x in nums.split(",")]
list_num = list(map(int,input_str.split(",")))
middle(list_num)