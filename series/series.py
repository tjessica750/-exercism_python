def slices(series, length):
    ls = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if len(series)==0:
        raise ValueError("series cannot be empty")
    if length <0:
        raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    
    else:
        for i,c in enumerate(series):
            # ls.append(series[i])
            sub = series[i:i+length]
            if len(sub) == length:
                ls.append(series[i:i+length])
        return ls