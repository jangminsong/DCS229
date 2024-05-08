from MyList import *
from progress.bar import PixelBar
from time import perf_counter
import random

################################################################################
def oneExperiment(min_list_size: int, max_list_size: int) -> tuple[int, int, int]:
    ''' function to conduct one experiment by creating a MyList object,
        then appending a random number (between the given min and max values)
        of integers each chosen at random between 1 and 1000 inclusive
    Parameters:
        min_list_size: integer corresponding to the smallest possible MyList
        max_list_size: integer corresponding to the largest possible MyList
    Returns:
        a tuple of post-experiment stats, in order:
            - the length of the MyList (entries, not internal array capacity)
            - the number of array resizes required across all appends
            - the number of array-to-array elements copied across all appends
    '''
    testList = MyList()
    for i in range(random.randint(min_list_size, max_list_size)):
        testList.append(random.randint(1,1000))
    return (testList.__len__(), testList._resizes, testList._copies)

################################################################################
def main() -> None:
     # you will need to add more code throughout below

    random.seed(8675309)
    num_experiments = 30
    bar = PixelBar('Processing', max = num_experiments)
    entries = 0
    resizes = 0
    copies = 0
    time = 0

    for i in range(num_experiments):
        startTime = perf_counter()
        experiment = oneExperiment(100000,999999)
        endTime = perf_counter()
        time += endTime - startTime
        entries += experiment[0]
        resizes += experiment[1]
        copies += experiment[2]
        # conduct one experiment keeping track of the stats to print
        # averages later... remember to time each experiment
        bar.next()

    bar.finish()
    
    avgTime = time / num_experiments
    avgEntries = entries / num_experiments
    avgResizes = resizes / num_experiments
    avgCopies = copies / num_experiments
    
    print(f'  average entry: {avgEntries:.2f}')
    print(f'average resizes: {avgResizes:.2f}')
    print(f' average copies: {avgCopies:.2f}')
    print(f'   average time: {avgTime:.2f}sec')


if __name__ == "__main__":
    main()
