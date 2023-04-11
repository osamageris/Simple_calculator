#enter numbers
n1=float(input("enter value of first number"))
n2=float(input("enter value secound number"))
#enter operation
op=input("select only one operation  add or sub or mul  or div ")

# functions
def add(n1,n2):
  result=n1+n2
  print("result:",result)
  
def sub(n1,n2):
  result=n1-n2
  print("result:",result)
  
def mul(n1,n2):
  result=n1*n2
  print("result:",result)
  
def div(n1,n2):
  result=n1/n2
  print("result:",result)

  #calling all functions
"""
add(n1,n2)
sub(n1,n2)
mul(n1,n2)
div(n1,n2)
"""
#calling entered function 

if op == 'add': 
    add(n1,n2)

elif op == "sub": 
    sub(n1,n2) 

elif op== "mul": 
    mul(n1,n2) 

else: 
   div(n1,n2) 
