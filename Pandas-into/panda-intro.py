import pandas as pd
A =pd.Series([2,3,4,5],index=['a','b','c','d'])
print(type(A.values))

print(A.index)

A['a':'c']


grads_dict ={'A':4,'B':3.5,'C':3,'D':2.5}
grads =pd.Series(grads_dict)

print(grads_dict)

marks_dict={'A':85,'B':75,'C':65,'D':55}
marks =pd.Series(marks_dict)



print(marks[0:2])


D =pd.DataFrame({'Marks':marks,'Grades':grads})
print(D)

print(D.values[2,0])


D['ScaledMarks']=100*(D['Marks']/90)
print(D)


#you want to pick data fram such that marks are greater than lets say 70

G=D[D['Marks']>70]
print(G)

#missing values data 


A=pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])
print(A)
A.fillna(0)

A=pd.Series(['a','b','c'],index=[1,3,5])
print(A.iloc[1:3])
print(A.loc[1:3])

print(D.iloc[2,:])
print(D.iloc[::-1,:])
