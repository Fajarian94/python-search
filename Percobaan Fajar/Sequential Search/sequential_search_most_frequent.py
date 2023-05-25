def sequential_search_most_frequent(data) :
    count_dict = {}
    for item in count_dict :
        if item in count_dict :
            count_dict[item] += 1
        else :
            count_dict[item] += 1
    most_frequent = None
    max_count = 0
    for key in count_dict :
        if count_dict[key] > max_count :
            most_frequent = key
            max_count = count_dict[key]
    return most_frequent

mylist = [ 3, 7, 2, 5, 7, 3, 7, 2, 7]
frequent_elemen = sequential_search_most_frequent(mylist)
print(f"elemen yang paling sering muncul adalah {frequent_elemen}")
