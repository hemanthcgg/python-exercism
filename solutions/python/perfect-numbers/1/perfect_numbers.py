def classify(number):
    if(number<1):
        raise ValueError("Classification is only possible for positive integers.")
        
    aliquot_sum = sum([x for x in range(1,number) if(number%x==0)])
    print(aliquot_sum)

    if(aliquot_sum == number):
        return "perfect"
    if(aliquot_sum > number):
        return "abundant"
    return "deficient"
