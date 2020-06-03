#ID   :H20191030124
#Name :Geetika Joshi
 
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 
p = int(input('Enter a prime number p = ')) 
q = int(input('Enter a prime number q = ')) 
m = int(input('Enter plain text = ')) 
n = p*q 
phi = (p-1)*(q-1) 
#finding e(public key)
for e in range(2,phi): 
	if gcd(e,phi)== 1: 
		break
#finding d(private key)
eIn = modinv(e,phi)
d=eIn%phi

#ciphertext

ctt =pow(m,e) 
ct = ctt % n

#decyption
dtt = pow(ct,d) 
dt = dtt % n 

print('n = '+str(n))
print('phi ='+str(phi))
print('public key e ='+str(e))
print('private key d ='+str(d))
print('cipher text = '+str(ct)+' decrypted text = '+str(dt)) 

