def fact(f) :
 if (f == 1 or f==0) :
   a = 1
   return a
 else : 
   return f * fact(f-1)   
f = int(input("Enter the number of which the factorial is to be found: \n"))
print(fact(f))