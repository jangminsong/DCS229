
def hello(name: str) -> None:
    '''
    Prints hello to the given name
    Paramtemters:
        name: the name of a really ugly person
    Returns:
        None
    '''
    print(f"hey {name}!")
    

def hola(name: str):
    return f"Hola {name}!"

def main():
    hello("Albert")
    print(hola("Albert"))
    hello(print(hola("Albert")))


if __name__ == "__main__":
    main()