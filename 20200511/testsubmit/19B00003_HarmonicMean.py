sc = [ 81, 68, 72, 87, 93, 84]
inv_total = 0
for i in sc:
    inv_total = inv_total + 1/i    
inv_mean = inv_total / len(sc)
harm_mean = 1/inv_mean
print(round(harm_mean,3))