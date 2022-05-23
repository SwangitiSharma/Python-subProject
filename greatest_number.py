def greatNum():
  a=int(input("enter a number:"))
  b=int(input("enter a number:"))
  c=int(input("enter a number:"))
  gN=[]
  if(a>b and a>c):
        gN.append(a)
  elif(b>c and b>a):
         gN.append(b)
  else:
     gN.append(c)
  return gN
print(greatNum())