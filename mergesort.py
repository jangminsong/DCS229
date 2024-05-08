def merge(a_list: list[int], b_list: list[int]) -> list[int]:
    new_list = []
    a = 0 #index into a_list
    b = 0 #index into b_list
    while a<len(a_list) and b<len(b_list):
        if a_list[a] < b_list[b]:
            new_list.append(a_list[a])
            a+=1
        else:
            new_list.append(b_list[b])
            b+=1
    
    if b == len(b_list):
        new_list.extend(a_list[a:])
    else:
        new_list.extend(b_list[b:])

    return new_list

def mergeSort(my_list: list[int]):
    if len(my_list) <= 1:
        return my_list
    else:
        mid = len(my_list)//2
        a_list = mergeSort(my_list[0:mid])
        b_list = mergeSort(my_list[mid:])
        return merge(a_list,b_list)

def main() -> None:
    a_list = [2,6,9,10,13]
    b_list = [3,4,30,12]
    c_list = merge(a_list, b_list)
    print(c_list)

    print(mergeSort(c_list))
    

main()