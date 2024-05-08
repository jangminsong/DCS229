from enum import Enum

class Majors(Enum):
    DCS = "DCS"
    BIO = "biology"
    ECON = "economics"
    PHIL = "philosophy"
    HIST = "history"

def main() -> None:
    list_of_majors = [Majors.BIO, Majors.DCS, Majors.ECON, Majors.PHIL, Majors.HIST]

    for major in list_of_majors:
        print(major)

if __name__ == "__main__":
    main()
