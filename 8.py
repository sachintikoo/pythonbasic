from re import I


a = int(input("Enter the number of which multiplication is to be found\n"))
print("The table of" , a , "is given as")
i = 15
while (i <= 10): 
   b = (a*i)
   i = i + 1
   print(a, "x" , i-1 , "=" , b)
