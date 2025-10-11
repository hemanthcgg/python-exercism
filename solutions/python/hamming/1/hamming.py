def distance(strand_a, strand_b):
    hamming_distance = 0
    if(len(strand_a)!=len(strand_b)):
        raise ValueError("Strands must be of equal length.")
    for i in range(len(strand_a)):
        if(strand_a[i]!=strand_b[i]):
            hamming_distance+=1
            print(i, end=' ')
    return hamming_distance
