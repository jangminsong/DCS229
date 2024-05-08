class Binary:
    def __init__(self, bits: str) -> None:
        if bits.count('0') + bits.count('1') != len(bits):
        self._bits = bits  #instance variable
    
    def __str__(self) -> str:
        print(f"self = {id(self)}")
        return self._bits
    
    def __eq__(self: 'Binary', other: 'Binary') -> bool:
        return self._bits == other._bits
        

def main() -> None:
    b1 = Binary("111")
    print(f"{b1}    {type(b1)}")
    b2 = Binary("111")
    print(f"{b2}    {type(b2)}")
    print(b1 == b2)


    
if __name__ == "__main__":
    main()

    # variable holds the memory address
    # Object of class classtype
    # Instance variable
    # int//int meaning 
