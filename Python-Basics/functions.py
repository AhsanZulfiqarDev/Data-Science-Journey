import modules
from modules import checkIfNotNumeric

result = modules.addAllNumerics(10, 20, 30)
print(result)


def findMin(L, startIndx=0):
    if not L:
        raise ValueError("List cannot be empty")

    m = L[startIndx]
    idx = startIndx

    for i in range(startIndx + 1, len(L)):
        if L[i] < m:
            m = L[i]
            idx = i

    return m, idx


a, b = findMin([10, 20, 30, 5, 40], 0)
print(a, b)


def swapValues(L, idx1, idx2):
    L = list(L)
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


swappedList = swapValues([10, 20, 30, 5, 40], 0, 3)
print(swappedList)


def sortList(L):
    if not checkIfNotNumeric(*L):
        print("List contains non-numeric values. Cannot sort.")
        return None

    sorted_values = list(L)
    for c in range(len(sorted_values)):
        _, idx = findMin(sorted_values, c)
        sorted_values = swapValues(sorted_values, c, idx)

    return sorted_values


sortedList = sortList([10, 20, 30, 5, 40])
print(sortedList)

#"""LAMBDA FUNCTIONS"""
square = lambda number:number**2
print(square(5))


add =lambda a,b:a+b
print(add(10,20))


students=[
    ("Ali",73),
    ("ahsan",13),
    ("Ahmad",63),  
]

students.sort(key=lambda student:student[1])
print(students)



#traditional loop
numbers =[1,2,3,4,5]

square =[]
for number in numbers:
    square.append(number**2)
    
print(square)    

#maps
def square(number):
    return number**2
squares =map(square,numbers)
print(squares)

temperatures_celsius =[20,25,30,35]
temperatures_fahrenheit =list(
    map(
        lambda temperature:(temperature*9/5)+32,
        temperatures_celsius,
    )
)

print(temperatures_fahrenheit)




#filter() keeps elements for which a function returns true

numbers =[1,2,3,4,5,6]
#we only want even numbers

even_numbers=[]
for number in numbers:
    if number%2==0:
        even_numbers.append(number)
     
#using filter

def is_even(number):
    return number%2==0
even_numbers =list(filter(is_even,numbers))

print(even_numbers)

#data oriented example
sales=[1200,500,400,3400,800,2200]
high_sales =list(
    filter(lambda sale:sale>=2000,sales)
    
)

print(high_sales)




#zip( combines multiple iterables element by elemnt.)

names =["Ali","Sara","Ahmad"]
scores =[75,92,68]

combined =zip(names,scores)
print(list(combined))


names =["Ali","Sara","Ahmad"]
scores =[45,32,32]
for name,score in zip(names,scores):
      print(f"{name}: {score}")
          
#creating dictionary
student_scores=dict(zip(names,scores))
print(student_scores)
#enumerate()
# frequently be needing item and its position

students =["Ali","Sara","Ahmad"]
for i in range(len(students)):
    print(i,students[i])

for index,student in enumerate(students):
    print(index,student)
    
 ##list comprehensions
 
numbers = [1,2,3,4,5]
squares =[]
for number in numbers:
    squares.append(numbers**2)

square =[number**2 for number in numbers]

numbers =[1,2,3,4,5,6]
even_numbers = [
    number
    for number in numbersif number %2==0
]            

# transofrmation +filtering

squared_even_numbers =[
    number**2
    for number in numbers
    if number%2==0
]

#Iterable vs iterators
#A list is an iterable:

numbers =[10,20,30]

for number in numbers:
    print(number)
    
#other iterable list tuple string dictionary file range    


#generators

def get_number():
    return[1,2,3]

def generate_numbers():
    yield 1
    yield 2
    yield 3
    
numbers =generate_numbers()
print(numbers)
    
    

