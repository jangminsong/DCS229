def is_even(num):
    return num % 2 == 0

def main():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True

main()