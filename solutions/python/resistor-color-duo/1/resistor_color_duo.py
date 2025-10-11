def value(colors):
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
    x, y, *rest = colors
    return (colors_list.index(x)*10 + colors_list.index(y))
    
