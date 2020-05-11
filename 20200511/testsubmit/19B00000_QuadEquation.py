def QuadEquation(a,b,c):
    if a == 0:
        return -(c / b)
    
    else:
        if b**2 - 4 * a * c < 0:
            print("no solutions")

        elif b**2 - 4 * a * c == 0:
            return -b  / (2 * a)

        else:
            return (-b + (b**2 - 4 * a * c)**0.5) / (2 * a), (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
        