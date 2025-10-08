def steps(number):
    step_count = 0
    if(number <= 0):
        raise ValueError("Only positive integers are allowed")
    while(number!=1):
        if(number%2!=0):
            number = (number*3) + 1
        else:
            number = number//2
        step_count+=1
    return step_count
