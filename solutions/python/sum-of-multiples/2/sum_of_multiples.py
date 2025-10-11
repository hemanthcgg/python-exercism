def sum_of_multiples(limit, multiples):
    return sum({x for m in multiples if m != 0 for x in range(m, limit, m)})
    #for x in range(m, limit, m) this expression gives us the factors directly
    #Ex: rang(3,16,3)=> 3,6,9,12,15 # multiples of 3 is generated using step addition