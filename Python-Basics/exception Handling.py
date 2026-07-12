try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
    
try:
    number =int(int(input("enter a number:")))
    result =100/number
except ValueError:
    print("Input must be numeric.")
    
except ZeroDivisionError:
    print("Number cannot be zero.")    
    
   #else block run only when try block succeeds without an exception
    
try:
    number =int(input(" Enter number: "))
except ValueError:
    print("Input must be numeric.")
else:
    print("conversion successful.")
    print(number)


try:
    number=int(input("Enter a number:"))  
except ValueError:
    print("Input must be numeric.")
else:
    print(number)
finally:
    print("Program execution completed.")            
 #access the exception object
try:
    number = int("hello")

except ValueError as error:
    print(error)
    
#raise valuable with ML
def validate_accuracy(accuracy:float) -> None:
    if accuracy <0.0 or accuracy>1.0:
        raise ValueError("Accuracy must be between 0 and 1.")

validate_accuracy(1.5)       
   