print("Hello World"); 
print("A+B");
print(5);
#this is use to add the single line comment in the program.
#ctrl+/ is use to comment and un-comment multiple lines at a same time by selecting all those lines.
print("output") #will  print 
'''
to move any line in the multi-level;
we can use the triple-single quotes 
or triple-double quotes

and to move any line up in the VS Code
use shortcut Alt+ arrow.......
'''
print("My name is \"Sarthak\"\nand my surname is Choudhary.");
print("Hey",6,7);
print("Hey",6,7,sep="-",end="009")
print("Hello")
print("Hey",6,7,sep="-",end="009\n")
print("Hello")
a=complex(2,3)
b="Sarthak"
c=True
d=None
e=False
print(a,b,c,d,e,sep="\n");
print(type(a),type(b),type(c),type(d),type(e))
list=[1,2,3,[4,5],"S","A","#"]
print(list)
tuple=(1,2,3,(4,5),"S","A","#")
print(tuple)
dict={1:"S",2:"A","R":3}
print(dict)

#Operators
#1st is arithmetic operator
print(15+6)
print(15-6)
print(15*6)
print(15/6) #division 
print(15%6)  #Modulus or remainder
print(15//6)  #Floor Division  or quotient 
print(2**4) #Exponential

#TypeCasting 
D1="1"
D2="3"
print(D1+D2)
print(int(D1)+int(D2))
#explicit type conversion 
string="15"
number=7
string_number=int(string)
sum=number+string_number
print("The sum of both the numbers is",sum)
#implicit type conversion 
c=1.6
d=8
print(c+d)  #data type is float automatically... to higher order data type

#Day 10 Taking user input in python
a=input("Enter name:")
print("My name is",a)

a=input("Enter Number1:")  #string type data
b=input("Enter Number2:")  #string type data
print(a+b)  #concatenate 


