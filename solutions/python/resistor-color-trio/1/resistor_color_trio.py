def label(colors):
    colors_list = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    [x,y,z, *rest] = colors
    base_value = (colors_list.index(x)*10 + colors_list.index(y))
    power = (10 ** colors_list.index(z))
    total = base_value * power
    
    if(total==0):
        return str(total)+" ohms"
    elif(total % (10 ** 9)==0):
        return str(total//(10 ** 9))+" gigaohms"
    elif(total % (10 ** 6)==0):
        return str(total//(10 ** 6))+" megaohms"
    elif(total % (10 ** 3)==0):
        return str(total//(10 ** 3))+" kiloohms"
    return str(total)+" ohms"
    
