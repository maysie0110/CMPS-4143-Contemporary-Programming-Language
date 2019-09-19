def has_duplicate(list_num):
    new_list = sorted(set(list_num))
    # print(new_list)
    # print(list_num)
    if(len(new_list) < len(list_num)):
        return True
    return False


t = [3,4,2,6,7,7,8]
status = has_duplicate(t)
if (status):
    print("List has duplicates")
else:
    print("List does not have duplicates")