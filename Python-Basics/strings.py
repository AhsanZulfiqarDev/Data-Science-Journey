s="this is python basics"
t="good morning"
print(s)
print(t)
v =s+ "  "+t
print(v)
price=12
a ="the price of this book"
q=a+ ' is:  ' +str(price)
print(q)
#multiple line string
m = """this is a multiple line string
        i AM LEARNING DATA SCIENCE
        i AM LEARNING PYTHON"""
print(m)

#indexing and slicing 
s ="How are you and who are you"
print(s[5])
type(s[5])
print(s[0:10])
print(s[-12:-3])
print(s[0:12:2])
#replacing
a = "this is a string"
b=a.replace("string","list")
print(b)
d ="I am learning python and python is easy"
e=d.replace("python","java")
print(e)
f=" abcsdd;def;ghij;klmn;opqr;stuv"
#split them with a splitter
L=f.split(";")
print(L)
print(L[1])
print(a.capitalize())
print('we are learning "sting"  manipulation')
print()