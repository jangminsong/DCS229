'''
Jangmin Song
stack HW
'''

from ArrayStack import *
import sys

def readFile(fileName: str) -> str:
    ''' This function opens and reads a file. Function may raise a FileNotFoundException
    Parameters:
        fileName: name of the file in string
    Returns:
        text: the inside text of the file in string
    '''
    with open(fileName, "r") as file:
        text = file.read().strip()
        file.close()
    return text

def parseHTML(text: str) -> bool:
    '''This function tests if the HTML is listed correctly or not. 
    Parameters: 
        text: text of the file in string that was obtained in readFile()
    Returns: 
        a boolean whether the format of the HTML was listed correctly or not. 
    '''
    stack = ArrayStack()

    #replaces all the brackets with spaces before and end of the bracket. 
    text = text.replace('<', ' <')
    text = text.replace('>', '> ')
    
    textSplit = text.split()
    for i in range(len(textSplit)): #run the entire text
        if '<' in textSplit[i]: #dividing between tags and normal words
            if '/' not in textSplit[i]: #if the tag does not contaion /: i.e. dividing between non / tags and / tags
                stack.push(textSplit[i][1:-1]) #push the non / tags ex: <html>, not </html>
            else: #when / tags appear
                if stack.is_empty() == True: #if the pushed stack is empty and there is nothing to match
                    print(f'unmatched tag: {textSplit[i]}.')
                    return False
                if stack.top() != textSplit[i][2:-1]: #if the top of stack does not match with the text
                    print(f'mismatched <{stack.pop()}> to {textSplit[i]}.')
                    return False
                stack.pop() #pop to go the next tag
    if stack.is_empty(): #if the stack is empty: (everything was matched)
        return True
    else:
        unmatched_string = f'unmatched: '
        while stack.is_empty() == False: #if the stack is not empty after checking all the / tags: i.e. there are non matched non / tags
            unmatched_string += f'<{stack.pop()}>' #make a list of unmatched
        print(unmatched_string)
        return False
            
def main() -> None:
    print(f"sys.argv = {sys.argv}")
    print(f"name of program = {sys.argv[0]}")
    try:    
        readFile(sys.argv[1])
        parseHTML(readFile(sys.argv[1]))
    except IndexError:
        print(f"Please handle the index correctly. {sys.exit(2)}")
    except FileNotFoundError:
        print(f"File not found. {sys.exit(1)}")
    
if __name__ == "__main__":
    main()
