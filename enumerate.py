def numbered_list(list):
    for i,item in enumerate(list, start=1):
        print(f"{i}. {item}")


print(numbered_list(["apple", "banana", "cherry"]))