def classify(num):
    sum = 0
    num_list = range(1, num) # does not include num
    for i in num_list:
        if num % i is 0:
            sum += i
    if sum == num:
        return ("p")
    elif sum > num:
        return("a")
    else:
        return("d")

def main():
    num = -1
    while num < 1:
        try:
            num = int(input("Enter a number greater than -1: "))
        except ValueError:
            num = -1
    
    print(classify(num))

if __name__ == '__main__':
    main()