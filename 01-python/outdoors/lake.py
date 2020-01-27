def draw_lake():
    if (width < 0 or length < 0):
        raise ValueError("invalid width or length")
    for i in range(width):
        for j in range(length):
            print("~",end="")
        print() 
    return
