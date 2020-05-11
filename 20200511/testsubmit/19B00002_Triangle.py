def compute(a,b,c):
    T = (a + b + c) / 2
    area = (T * (T - a) * (T - b) * (T - c))**0.5
    return area

a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))
s1 = compute(a1, b1, c1)
print("area",s1)