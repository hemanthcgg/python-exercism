def find(search_list, value):
    # if( value in search_list):
    #     return search_list.index(value)
    # raise ValueError("value not in array")
    low, high = 0, len(search_list)-1
    while(low<=high):
        mid = (low + high)//2
        if(search_list[mid]==value):
            return mid
        elif(search_list[mid]>value):
            high = mid-1
        else:
            low = mid+1
    raise ValueError("value not in array")
        
