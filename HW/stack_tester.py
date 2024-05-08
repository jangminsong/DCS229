from ArrayStack import *

def main() -> None:
    
    s = ArrayStack()
    print(f"len = {len(s)}")

    s.push(8)
    s.push(3)
    print(s)
    print('=' * 40)

    value = s.pop()
    print(f"Just popped {value}")
    print(s)
    print('=' * 40)

    s.push(2)
    s.push(5)
    print(s)
    print('=' * 40)

    value = s.pop()
    print(f"Just popped {value}")
    print(s)
    print('=' * 40)

    value = s.top()
    print(f"Top of stack is {value}")
    print(s)
    print('=' * 40)

    s.push(9)
    s.push(1)
    print(s)
    print('=' * 40)

    # clear out the stack
    while len(s) > 0: s.pop()

    # push some floats
    for i in range(100,105,1):
        s.push(i + 0.5)
    print(s)
    print('=' * 40)

    # clear out the stack
    while len(s) > 0: s.pop()

    # push some strings
    import random
    import string
    for i in range(5):
        # create a random string of length 15 consisting of ascii letters
        random_word = "".join(x for x in random.sample(string.ascii_letters, 15))
        s.push(random_word)
    print(s)


if __name__ == "__main__":
    main()









