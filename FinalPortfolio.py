def example(): 
    company = 'Apple'
    type = 'iPhone'
    name = 'iPhone13'
    production_year = '2021'
    print(f'Phone informaiton without class: \n Company: {company} \n Type: {type} \n Name: {name} \n Production Year: {production_year} \n')


class Technology:
    def __init__(self, name):
        self.name = name
    def usage(self):
        raise ValueError("Subclasses must implement this method")
class Phone(Technology):
    def __init__(self, name):
        self.name = name
    def usage(self):
        return f"{self.name} is used for communication"
class Laptop(Technology):
    def __init__(self, name):
        self.name = name
    def usage(self):
        return f"{self.name} is used for work, entertainment, and browsing"
class Car(Technology):
    def __init__(self, name):
        self.name = name
    def usage(self):
        return f"{self.name} is used for transportation"
# Polymorphism
def describe_usage(tech):
    return tech.usage()
# class Phone(Technology):
    def __init__(self, company, type, name, production_year, broken):
        self.company = company
        self.type = type
        self.name = name
        self.production_year = production_year
        self.broken = broken

    def getCompany(self) -> str:
        return self.company

    def getType(self) -> str:
        return self.type

    def getName(self) -> str:
        return self.name
    
    def getProductionYr(self) -> str:
        return self.production_year

    def Broken(self) -> str:
        if self.broken:
            return 'Broken'
        else:
            return 'Not broken'
            
    def __str__(self):
        return f"Phone informaiton with class: \n Company: {self.getCompany()} \n Type: {self.getType()} \n Name: {self.getType()} \n Production Year: {self.getProductionYr()} \n {self.Broken()}"


# def push(stack: list, item) -> list:
#     return stack.insert(0,item)
# def pop(stack) -> list:
    if len(stack) == 0:
        raise 'stack is empty'
    else:
        return stack.remove(stack[0])

def push(queue: list, item) -> list:
    return queue.append(item)
def pop(queue) -> list:
    if len(queue) == 0:
        raise 'queue is empty'
    else:
        return queue.remove(queue[0])

def push_right(deque: list, item) -> list:
    return deque.append(item)
def push_left(deque: list, item) -> list:
    return deque.insert(0, item)
def pop_left(deque) -> list:
    if len(deque) == 0:
        raise 'deque is empty'
    else:
        return deque.remove(deque[0])
def pop_right(deque) -> list:
    if len(deque) == 0:
        raise 'deque is empty'
    else:
        return deque.remove(deque[len(deque)-1])

def eat_fried_rice(amount):
    if amount <= 0:
        print("No fried rice left!")
        return
    else:
        print("Eating a scoop of fried rice")
        print(f'Amount left: {amount}')
        eat_fried_rice(amount - 1)
    
def main():
    # iPhone = Phone("iPhone")
    # macbook = Laptop("MacBook")
    # Toyota = Car("Toyota")

    # print(iPhone.usage())
    # print(macbook.usage())
    # print(Toyota.usage())

    # print(describe_usage(iPhone))  
    # print(describe_usage(macbook))  
    # print(describe_usage(Toyota))  

    # stack = []
    # push(stack,1)
    # print(stack)
    # push(stack,2)
    # print(stack)
    # push(stack,3)
    # print(stack)
    # push(stack,4)
    # print(stack)
    # push(stack,5)
    # print(stack)
    # pop(stack)
    # print(stack)
    # pop(stack)
    # print(stack)

    # queue = []
    # push(queue,1)
    # print(queue)
    # push(queue,2)
    # print(queue)
    # push(queue,3)
    # print(queue)
    # push(queue,4)
    # print(queue)
    # push(queue,5)
    # print(queue)
    # pop(queue)
    # print(queue)
    # pop(queue)
    # print(queue)

    # deque = []
    # push_right(deque, 1)
    # print(deque)
    # push_right(deque,2)
    # print(deque)
    # push_left(deque,3)
    # print(deque)
    # push_left(deque,4)
    # print(deque)
    # pop_right(deque)
    # print(deque)
    # pop_left(deque)
    # print(deque)
    # pop_right(deque)
    # print(deque)

    initial_amount = 10
    eat_fried_rice(initial_amount)

main()