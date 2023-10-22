# Us = 15
# Rn1 = 10*10E6
# Rn2 = 500*10E3
# r1 = 200*10E3
# r2 = 51*10E3
# r1p = 1/(1/r1+1/Rn1)
# r1pp = 1/(1/r1+1/Rn2)
# u1 = Us*(r1p)/(r1p+r2)
# print(u1)
# u1p = Us*(r1pp)/(r1pp+r2)
# print(u1p)

# r2p = 1/(1/r2+1/Rn1)
# r2pp = 1/(1/r2+1/Rn2)
# u2 = Us*(r2p)/(r2p+r1)
# print(u2)
# u2p = Us*(r2pp)/(r2pp+r1)
# print(u2p)


ri = 5.1
r1 = 20
r2 = 2000
i = 19
r1p = r1+ri
r2p = r2+ri
def bing(r1,r2):
    return r1*r2/(r1+r2)
i1 = i*bing(r1,r1p)/r1p
i2 = i*bing(r2,r2p)/r2p
print(i1)
print(i2)