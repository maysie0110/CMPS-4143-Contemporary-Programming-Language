def nested_sum(list_num):
    sum = 0
    for item in list_num:
        for i in item:
            sum += i
    print(sum)

#list_num = list(int(input("Enter a list of lists of integers: ")))
list_num = [[1,2],[3],[4,6,6]]
# nums = input("Enter a list of lists of numbers: ")
# list_num = list(map(int,input.split(",")))
nested_sum(list_num)
