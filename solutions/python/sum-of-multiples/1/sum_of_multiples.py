def sum_of_multiples(limit, multiples):
    sets_list = []
    for i in multiples:
        if(i>0):
            sets_list.extend([j for j in range(1,limit) if j%i==0])
    return sum(list((set(sets_list))))