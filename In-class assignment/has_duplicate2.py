def has_duplicate (list_num):
    new_list = []
    for item in list_num:
        if item in new_list:
            return True
        else:
            new_list.append(item)
    return new_list

t = [3,5,4,2,7,7,4]
status = has_duplicate(t)
if status is True:
    print("List has duplicates")
else:
    print(status)