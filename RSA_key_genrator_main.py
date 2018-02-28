from prime_num_generator import generate_prime
from lcm import lcm
import random

ranges = [[30000,20000],[80000,70000],[130000,100000]]
index = 0
#change range of prime here & index ^, larger primes the better, but slower
#index 0, 30k - 20k, ~5s
#index 1, 70k - 80k, ~30s
#index 2, 130k - 100k, ~1.5 min

upper_limit = ranges[index][0] 
lower_limit = ranges[index][1]

#get 2 unique primes in range
prime_list = generate_prime(upper_limit,lower_limit)
p1 = random.choice(prime_list)
prime_list.pop(prime_list.index(p1))
p2 = random.choice(prime_list)
print("prime 1: " + str(p1))
print("prime 2: " + str(p2))

#generate shared key
shared_key = p1 * p2
print("shared key: " + str(shared_key))

#generate euler, then generate public key with euler
Euler = lcm(p1-1, p2-1)
euler = Euler
print("euler: " + str(euler))
while euler > upper_limit:
    euler /= 10
euler = int(euler)
public_key = random.choice(generate_prime(euler,int(lower_limit/20)))
print("public key: " + str(public_key))

#generate private key with public key and euler
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
private_key = int(MMI(public_key,Euler))
print("private key: " + str(private_key))

##index = 123 #TEMPORARY index to encrypt
##encrypted_index = pow(index,public_key,shared_key)
##decrypted_index = pow(encrypted_index,private_key,shared_key)
##if decrypted_index == index:
##    print('true')
##else:
##    print('false') #to test if generation works, true if it does

f_private = open("private_key.txt", 'w')
f_private.write(str(shared_key) + " " + str(private_key))
f_private.close()

f_public = open("public_key.txt", 'w')
f_public.write(str(shared_key) + " " + str(public_key))
f_public.close()
