import random
import string

def randomWord(max_length: int) -> str:
    word = ""
    length = random.randint(1, max_length)
    for i in range(length):
        index = random.randint(0,len(string.ascii_letters)-1)
        word += string.ascii_letters[index]
    return word

def createList(num_words: int, max_word_length: int) -> list[str]:
    list_ = []
    for k in range(num_words):
        word = randomWord(max_word_length)
        list_.append(word)
    return list_


def main() -> None:
    random.seed(17) #seed
    # print("testing randomWord(6): ")
    # print(f"  result: {repr(randomWord(6))}")
    # print(f"expected: 'AZtxs'")

    # print("testing randomWord(6): ")
    # print(f"  result: {repr(randomWord(6))}")
    # print(f"expected: 'XT'")

    print("testing createList(4,6): ")
    print(f"  result: {repr(createList(4,6))}")
    print(f"expected: ['AZtxs', 'XT', 'IQrhbp', 'VAqG']")


if __name__ == "__main__":
    main()