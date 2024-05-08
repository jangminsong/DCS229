class C:
    __slots__ = ('_value')

    class_var = 0        # a class-level variable, not an instance variable
    _num_Cs_created = 0  # class-level variable to track # of C objects created

    def __init__(self, value: int) -> None:
        self._value = value
        C._num_Cs_created += 1

    def __str__(self) -> str:
        return str(self._value)

    # example of a class method
    @classmethod
    def getNumObjects(cls) -> int:
        return cls._num_Cs_created


def main() -> None:
    
    c1 = C(99)
    c2 = C(88)
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")

    C.class_var = 77

    print(f"class_var = {C.class_var}   {id(C.class_var)}")
    print(f"class_var = {c1.class_var}   {id(c1.class_var)}")
    print(f"class_var = {c2.class_var}   {id(c2.class_var)}")

    #c1.class_var = 66  # if __slots__ is defined, not allowed;
                        # if __slots__ is not defined, Python
                        # creates a new instance variable inside
                        # c1 having the same name as the class-level
                        # variable

    C.class_var = 66

    print(f"class_var = {C.class_var}   {id(C.class_var)}")
    print(f"class_var = {c1.class_var}   {id(c1.class_var)}")
    print(f"class_var = {c2.class_var}   {id(c2.class_var)}")

    print(f"# of objects created = {C.getNumObjects()}")
    c3 = C(44)
    print(f"# of objects created = {C.getNumObjects()}")



main()


