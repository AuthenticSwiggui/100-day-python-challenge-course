scores = [2,5,4,3,5,4,1,2]

total_score = sum(scores)

print(total_score)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(max_score)


###Range (min, max, step [O sea, de cuanto en cuanto])
zuma = 0
for i in range(1, 101, 5):
    zuma += i
    print(zuma)


