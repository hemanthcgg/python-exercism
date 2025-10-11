def commands(binary_str):
    action = ["", "wink", "double blink", "close your eyes", "jump"]
    length = len(binary_str)
    result = []
    idx = 1
    while(length):
        if(int(binary_str[length-1])):
            if(idx!=5):
                result.append(action[idx])
            else:
                result.reverse()
        length-=1
        idx+=1

    return result
        
        
        