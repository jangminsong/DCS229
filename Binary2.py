from Binary import *

def main() -> None:
    try:
        b1 = Binary("01011")
    except ValueError as error:
        print(f"ValueError: {error}")
    except IndexError as error:
        print(f"IndexError: {error}")
    except TypeError as error:
        print(f"TypeError: {error}")
    except Exception as error:
        print(f"exception: {error}")
    else: 
        print(b1)

main()