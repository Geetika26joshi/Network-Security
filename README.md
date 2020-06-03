# Network-Security
Question 1 : RSA

The file is named as :rsa.py

We select 2 prime numbers p and q and calculate n as p*q and phi as (p-1)*(q-1)
we then find public and private keys e and d
e is the co prime of phi and d is calculated as de is modular congruent to phi.For this we calculate the e inverse.
enpcryption is done as:
cipher text=(plain text**public key)mod n
decryption is done as:
plain text=(cipher text**private key)mod n

Question 2 : Implementation of the protocol "secure two party computation"

The file is named as : Task-2.py

1<=x,y<=4
2 parties Alice and Bob have to compare their secret x and y  and disclose which is greater.
here Alice has x=4 .Alice selects a large number m1=39.It then encrypts m1 using the public key of Bob and calculates C and c1
C=(m1**e)%n
c1=C-x
Alice then sends this c1 to Bob

Bob recieves c1 from Alice.
Bob has y=6 and private keys of Bob are d=23 and n=55.
Bob selects a prime number P=31
We have 2 list m2 and Z for i 1 to 10
m2 is filled with values such that  k=((val+i)**d)% n
and Z has values z=k%P
Bob sends this Z and P to Alice
Alice checks the modular congruency of xth value of the recieved Z and the recieved prime number.
If they are not congruent then it is concluded that Alice is richer else Bob is richer.This result is reflected in global variable result so that Bob also knows the result.

