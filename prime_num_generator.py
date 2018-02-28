##i am aware there is a built in function for this but im just doing this for fun :)

def generate_prime(max_num, min_num = 2):
    list_all_num_in_range = list(range(2,max_num+1))
    list_prime_num = []
    while len(list_all_num_in_range) > 0:
        prime_num_hold = list_all_num_in_range[0]
        list_all_num_in_range.pop(0)
        list_prime_num.append(prime_num_hold)
        length_all = len(list_all_num_in_range)-1
        for a in range(length_all):
            index = length_all - a
            if list_all_num_in_range[index] % prime_num_hold == 0:
                list_all_num_in_range.pop(index)

    while list_prime_num[0] < min_num:
        list_prime_num.pop(0)
    return list_prime_num
#end
