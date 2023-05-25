def sequential_search(data, key) :
    for item in data :
        if item ==key :
            return True
    return False

mylist = [3, 6, 2, 9, 4, 7]
key = 6
found = sequential_search(mylist, key) 
if found : 
    print (" elemen ditemukan = ", key)
else :
    print("elemen tidak ditemukan")
