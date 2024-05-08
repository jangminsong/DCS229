class Student:
    __slots__ = ('_name')
    def __init__(self, name: str) -> None:
        self._name = name
    def __str__(self) -> str:
        return self._name
    def changeName(self, name: str) -> None:
        if len(self._name) == 0:
            raise ValueError('cannot have an empty name')
        self._name = name

def main() -> None:
    s1 = Student("Luke")
    s2 = Student("Annie")
    s3 = Student("Aldair")
    s4 = Student("Liz")
    print(s1)
    s1.changeName("Zach")
    print(s1)

    list1 = [s1, s2, s3, s4]
    list2 =list1[1:]
    for s in list1: 
        print(s, " ", end = "")
    print()
    for s in list2: 
        print(s, " ", end = "")
    print()

    list1[0].changeName("Adrian")
    print(list1[0])

    # print(id(list1))
    # print(id(list2))

    # print("ids in list 1: ", end = "")
    # for obj in list1:
    #     print(id(obj), " ", end = "")
main()