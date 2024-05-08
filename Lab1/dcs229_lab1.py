'''
Jangmin Song
Lab 1
1/19/24

Sources Used:
dictionary: https://runestone.academy/ns/books/published/thinkcspy/Dictionaries/toctree.html
dictionary items: https://www.programiz.com/python-programming/methods/dictionary/items
dictionary.zip(): https://realpython.com/python-zip-function/
dictionary.sorted(): https://realpython.com/sort-python-dictionary/
Combining two lists into a tuple: https://www.geeksforgeeks.org/python-merge-two-lists-into-list-of-tuples/
File: https://runestone.academy/ns/books/published/thinkcspy/Files/toctree.html
String allignment: https://www.geeksforgeeks.org/string-alignment-in-python-f-string/
'''

def readWords(fileName: str, use_dict: bool = False) -> tuple or dict:
    '''
    This function opens the file, splits all the sentences to words, and omits punctuations and 
    possesives. Addtionally, this function counts how many times each words were used. 
    Parameters:
        fileName: str = a string that contains the name of a file
        use_dict: bool = a boolean that determines which type of litings to use
    Returns:
        Returns either a tuple or a dictionary based on the boolean parameter
    '''
    file = open(fileName, "r") #opens a file
    words = [] #will contain list of words
    count = [] #will contain the counts of each words
    line = file.readline() #reads a line of a file
    while line: #while there exists lines
            wordList = line.lower().strip().split(" ") #makes the sentence into lowercase and single words
            for word in wordList: #for loop that goes through all the words in the list
                #omits punctuations and possesives
                onlyWord = word.replace('?','').replace(',', '').replace("!", '').replace("'s", '').replace(':', '').replace(';', '').replace('(', '').replace(')', '').replace('.','')
                if onlyWord in words: #check if the word "wordlist[i]" is in the list "words"
                    order = words.index(onlyWord) #find the order of that word in the list
                    count[order] += 1 #add the counter
                else:
                    words.append(onlyWord) #add the word to  wordsList
                    count.append(1) #add the counter of that word to the counting list
            line = file.readline() #read next line
    if use_dict == True: #if use dictionary is on
        dictionary = dict(zip(words, count)) #puts words and count together into a dictionary
        return dictionary 
    else:
        return (words, count,) #puts words and count together into a tuple

def writeTopK(dictionary: dict, fileName: str, k: int) -> None:
    '''
    This function writes the file that contains lists of words and the number of how many words appeared
    in the order of the frequency (Alphabetical order if the number is the same), and the number of words to be
    written can be controlled by the k parameter. If kth place contains multiple words, all of them shows up. 
    Parameters:
        dictionary: dict = a string that contains the name of a file
        fileName: str = a string that contains the name of a file that will be written
    Returns:
        Returns none
    '''
    sorted_alpha_dict = dict(sorted(dictionary.items())) #sorts the dictionary into alphabetical order
    sorted_num_dict = dict(sorted(sorted_alpha_dict.items(), key=lambda item: item[1], reverse = True)) #sorts the dictionary by high value to low balue
    dict_ = list(sorted_num_dict.items()) #put them in the list so that I can number them
    print(type(dict_))
    wordCounter = 0 #Word counter that counts how many words are written
    with open(fileName, 'w') as writingFile: #open new file and write
        for key, value in sorted_num_dict.items(): #for loop for the dictionary with writing key and value
            if wordCounter < k: #if wordCounter is less than the parameter k
                writingFile.write(f"{key:<20} {value:>4}\n") #write the output
            #else if word counter is the same as k (the word should stop printing, but all the other words that have same value as the last one should also print)
            elif wordCounter == k: 
                sameWordCounter = 1 #same word counter is the counter that counts until the word's value becomes different
                #while the k-1+samewordCounter is less than the entire length of the dictionary and the two word's value are the same
                while  k-1+sameWordCounter<len(sorted_num_dict.items()) and dict_[k-1][1] == dict_[k-1+sameWordCounter][1]: 
                    writingFile.write(f"{dict_[k-1+sameWordCounter][0] : <20} {dict_[k-1+sameWordCounter][1] : >4}\n") #write words to the file which have the same value
                    sameWordCounter += 1 #move to the next same word
                else: #Once words dont haev same value
                    break
            else: #if k is bigger than 0
                break
            wordCounter +=1 #move to the next word
        
def main():
    #test for readWords
    print(f"Test for readWords")
    print(f"  result: {readWords('wilco.txt', True)}")
    expected1 = {'are': 5, 'you': 14, 'under': 1, 'the': 5, 'impression': 1, 'this': 4, "isn't": 1, 'your': 5, 'life': 1, 'do': 1, 'dabble': 1, 'in': 3, 'depression': 1, 'is': 5, 'someone': 2, 'twisting': 2, 'a': 4, 'knife': 2, 'back': 2, 'being': 3, 'attacked': 2, 'oh': 20, 'fact': 2, 'that': 3, 'need': 2, 'to': 4, 'know': 2, 'wilco': 13, 'will': 4, 'love': 4, 'baby': 4, 'times': 1, 'getting': 1, 'tough': 1, 'roads': 1, 'travel': 1, 'rough': 1, 'have': 1, 'had': 1, 'enough': 1, 'of': 3, 'old': 1, 'tired': 1, 'exposed': 1, 'cold': 1, 'stare': 1, 'at': 1, 'stereo': 1, 'put': 1, 'on': 2, 'headphones': 1, 'before': 2, 'explode': 1, 'so': 1, 'many': 1, 'wars': 1, 'just': 1, "can't": 1, 'be': 1, 'won': 1, 'even': 1, 'battle': 1, 'begun': 1, 'all': 1, 'our': 1, 'arms': 1, 'open': 1, 'wide': 1, 'sonic': 1, 'shoulder': 1, 'for': 1, 'cry': 3} 
    print(f"expected: {expected1}")
    print(f"\n")
    print(f"  result: {readWords('test2.txt')}")
    expected2 = (['almost', 'heaven', 'west', 'virginia', 'blue', 'ridge', 'mountains', 'shenandoah', 'river', 'life', 'is', 'old', 'there', 'older', 'than', 'the', 'trees', 'younger', 'growing', 'like', 'a', 'breeze', 'country', 'roads', 'take', 'me', 'home', 'to', 'place', 'i', 'belong', 'mountain', 'mama', 'all', 'my', 'memories', 'gather', "'round", 'her', 'miner', 'lady', 'stranger', 'water', 'dark', 'and', 'dusty', 'painted', 'on', 'sky', 'misty', 'taste', 'of', 'moonshine', 'teardrop', 'in', 'eye', 'hear', 'voice', 'morning', 'hour', 'she', 'calls', 'radio', 'reminds', 'far', 'away', 'driving', 'down', 'road', 'get', 'feeling', 'that', "should've", 'been', 'yesterday'], [1, 1, 5, 5, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 10, 1, 1, 1, 1, 2, 1, 10, 10, 10, 12, 12, 5, 4, 7, 4, 4, 4, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2])
    print(f"expected: {expected2}")
    print(f"\n")
    print(f"  result: {readWords('test3.txt', True)}")
    expected3 = {'hi': 1, 'everyone': 1, '': 2, 'i': 3, 'hope': 1, 'you': 2, 'are': 1, 'enjoying': 1, 'the': 2, 'first': 1, 'weekend': 1, 'back': 1, 'from': 1, 'break!': 1, 'my': 1, 'name': 1, 'is': 1, 'jangmin': 1, 'and': 1, 'will': 2, 'be': 1, 'your': 1, 'course': 1, 'attached': 1, 'tutor': 1, 'for': 1, 'this': 1, 'semester.': 1, 'attend': 1, 'monday': 1, 'classes.': 1, 'feel': 1, 'free': 1, 'to': 1, 'ask': 1, 'me': 1, 'any': 1, 'questions': 1, 'have.': 1}
    print(f"expected: {expected3}")

    #test for readWords
    writeTopK(readWords('wilco.txt', True), "writeFile.txt", 12)
    writeTopK(readWords('test2.txt', True), "writeFile2.txt", 8)
    writeTopK(readWords('test3.txt', True), "writeFile3.txt", 5)

if __name__ == "__main__":
    main()