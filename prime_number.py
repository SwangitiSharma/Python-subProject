notPrime="The number is not prime number"
inp=int(input("enter a number:"))
if inp == 0 or 1:
  print(notPrime)
if inp !=0 or 1:
  for i in range(2,inp):
    if(inp % i) == 0:
        print(notPrime)
        break
else:
        print(inp,"This is prme number")

