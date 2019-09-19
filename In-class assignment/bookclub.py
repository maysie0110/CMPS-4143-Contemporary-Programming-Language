r_dict = {
        "0": "0",
        "1": "5",
        "2": "15",
        "3": "30",
        "4": "60"
        }
books = input("Enter the number of books you purchased.\n")
if int(books) > 4 :
    print("60 points")
else:
    print(r_dict[books] + " points")


