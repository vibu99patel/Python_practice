seconds = [5,15, 25, 30, 47,12]
count = 0
for i in range(0, len(seconds)):
    for j in range(i+1, len(seconds)):
        if seconds[j] - seconds[i] <= 10:
            count += 1

print(count)
