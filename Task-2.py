#ID   :H20191030124
#Name :Geetika Joshi

e=7 #public key of BOB
n=55
result=''
def Alice():
  x=4
  
  m1=39
  C=(m1**e)% n #encrypting based on the public key of BOB
  c1=C-x
  print("c1 is",c1)
  Z,num=Bob(c1) #Alice sends c1 to Bob
 
  
  k=Z[x-1]
  print("k= ",k)
 
  if((k%num)!=m1%num): #checking modular congruency of xth value of the recieved Z and the recieved prime number
   result="Alice"
   print("x>y")        #if not congruent then it is concluded that Alice is richer
   
  else:
   result="Bob"
   print("y>x ")       #if congruent then it is concluded that Bob is richer
  print(result)



def Bob(val):

  y=1
  e=7
  n=55
  d=23
  m2=[]
  Z=[]
  
  
  P=31
  for i in range(1,5):
      k=((val+i)**d)% n
      z=k%P
      m2.append(k)
      Z.append(z)
  print("m2 is",m2)
  print("Z is",Z)
  for i in range(y,len(Z)):
      Z[i]+=1
  print("Z is sent as",Z)
  return(Z,P)

Alice()