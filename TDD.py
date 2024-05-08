def findIndex(list_: list[int], item: int) -> int:
    if item in list_:
        return item
    return -1

def testEmptyItemList() -> None:
    index = findIndex([0,0], 0)
    if index == -1:
        print("fail")

######################################################################

def find_item(list_: list[list], item: int) -> bool: 
    if item in list_: 
        return True
    return False

def find_first_item() -> None: 
    assert(find_item([3,4,5], 3) == True)

def find_last_item() -> None: 
    assert(find_item([3,4,5], 5) == True)

def test_find_item_not_inlist() -> None:
    assert(find_item([3,4,5], 0) == False)

def main() -> None:
    testEmptyItemList()

if __name__ == "__main__":
    main()
