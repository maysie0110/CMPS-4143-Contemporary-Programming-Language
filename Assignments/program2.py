# May Trinh
# CMPS 4143 - Contemporary Programming Language
# This program will open a file with decimal number, -1 is the sentinel value that will end the program
# It will call a recursive function to convert the decimal number to binary number. 

#recursive function that returns the binary of a decimal number as a string
def recursive_base_2(num):
    # Binary number of 0 and 1 is itself
    if num < 2 :
        binary = num
    else: 
       binary = str(recursive_base_2(num//2)) + str(num%2) #call function recursively with integer division
    return binary


def main():
    print("""May Trinh
CMPS 4143 - Contemporary Programming Language
This program will open a file with decimal number, -1 is the sentinel value that will end the program
It will call a recursive function to convert the decimal number to binary number.""")
    
    fileName = input("Enter a file name: ")
    with open(fileName) as file: #with open does not require .close(). It will close automatically
        data = file.read()
        nums = list(map(int,(data.split()))) # read numbers in as a list

        item = 0
        x = nums[item]

        #read number from the file until -1 is found
        while x is not -1:
            binary = recursive_base_2(x)
            print("{0} = {1}".format(x,binary))
            item += 1
            x = nums[item]

if __name__ == '__main__':
    main()






