class Matrix:

    def __init__(self, num_rows: int, num_cols: int, data: list[int]) -> None:
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._data: list[int] = data

def main() -> None:
    m1 = Matrix(2,3,[11,19,7,21,4,6])

if __name__ == "__main__":
    main()