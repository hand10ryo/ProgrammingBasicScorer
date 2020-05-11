def compute(r):
    pi = 3.14159265358979
    circumference = 2 * pi * r
    area = pi * r * r
    return circumference, area

r1 = float(input("radius1 = "))
l1,s1 = compute(r1)
print("radius",r1,"circumfence",l1,"area",s1)

r2 = float(input("radius2 = "))
l2,s2 = compute(r2)
print("radius",r2,"circumfence",l2,"area",s2)

r3 = float(input("radius3 = "))
l3,s3 = compute(r3)
print("radius",r3,"circumfence",l3,"area",s3)


