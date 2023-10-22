import random

results = []
streak_number = 0

results.append(random.randint(0,1))
sam = 1
i=1
while i<10000:
    new = random.choice([-1,1])
    results.append(new)
    old = results[i-1]
    if sam == 6:
        if new*old >0 and i!=9999:
            continue
        else:
            streak_number+=1
    if new*old<0:
        sam = 1
    else:
        sam +=1
    i+=1




# i = 0
# while i<10_000:
#     right = i + 3
#     if results[right] == results[i]:
#         judge = True
#         for po in results[i:i+6]:
#             if po != results[i]:
#                 False
#     else:
#         i = right
print(streak_number)