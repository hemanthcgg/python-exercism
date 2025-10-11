def resistor_label(colors):
    DIGIT_MAP = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    TOLERANCE_MAP = {
        "brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1, 
        "grey": 0.05, "gold": 5, "silver": 10
    }

    clean_colors = [c.lower() for c in colors]
    num_bands = len(clean_colors)
    
    if num_bands == 1 and clean_colors[0] == "black":
        return "0 ohms"

    if num_bands == 4:
        digits = clean_colors[:2]
        multiplier_color = clean_colors[2]
        tolerance_color = clean_colors[3]
    elif num_bands == 5:
        digits = clean_colors[:3]
        multiplier_color = clean_colors[3]
        tolerance_color = clean_colors[4]
    else:
        raise ValueError("Unsupported number of bands for this expert calculator.")
    try:
        if num_bands == 4:
            base_value = DIGIT_MAP[digits[0]] * 10 + DIGIT_MAP[digits[1]]
        elif num_bands == 5:
            base_value = DIGIT_MAP[digits[0]] * 100 + DIGIT_MAP[digits[1]] * 10 + DIGIT_MAP[digits[2]]
        multiplier_exponent = DIGIT_MAP[multiplier_color]
    except KeyError as e:
        raise ValueError(f"Invalid color digit: {e}")
        
    ohms = base_value * (10 ** multiplier_exponent)
    if ohms >= 1_000_000_000:
        value = ohms / 1_000_000_000
        unit = "gigaohms"
    elif ohms >= 1_000_000:
        value = ohms / 1_000_000
        unit = "megaohms"
    elif ohms >= 1000:
        value = ohms / 1000
        unit = "kiloohms"
    else:
        value = ohms
        unit = "ohms"
        
    if value == int(value):
        resistance_str = f"{int(value)}"
    else:
        resistance_str = f"{value:g}"
    try:
        tolerance_value = TOLERANCE_MAP[tolerance_color.lower()]
    except KeyError as e:
        raise ValueError(f"Invalid color tolerance: {e}")
    return f"{resistance_str} {unit} ±{tolerance_value}%"