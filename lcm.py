##i am aware there is a built in function for this but im just doing this for fun :)

from prime_num_generator import generate_prime

def lcm(n1, n2):
    if n1 > n2: #assign smaller/larger num
        larger = n1
        smaller = n2
    else:
        larger = n2
        smaller = n1

    prime_list = generate_prime(larger)
    
    larger_list = [0] #generate prime factor of larger num
    index = 0
    while larger != 1:
        prime_hold = prime_list[index]
        if larger % prime_hold == 0:
            larger /= prime_hold
            larger_list[index] += 1
        else:
            index += 1
            larger_list.append(0)

    smaller_list = [0] #generate prime factor of smaller num
    index = 0
    while smaller != 1:
        prime_hold = prime_list[index]
        if smaller % prime_hold == 0:
            smaller /= prime_hold
            smaller_list[index] += 1
        else:
            index += 1
            smaller_list.append(0)

    if len(smaller_list) > len(larger_list): #length is the length of lcm list, up length of shorter one to match
        length = len(smaller_list)
        while len(larger_list) != len(smaller_list):
            larger_list.append(0)
    else:
        length = len(larger_list)
        while len(larger_list) != len(smaller_list):
            smaller_list.append(0)        

    lcm_list = [] #generate prime factor of lcm in list
    for a in range(length):
        if smaller_list[a] > larger_list[a]:
            lcm_list.append(smaller_list[a])
        else:
            lcm_list.append(larger_list[a])

    lcm = 1 #generate lcm frm list
    for b in range(length):
        lcm *= prime_list[b]**lcm_list[b]

    return(lcm)
#end
