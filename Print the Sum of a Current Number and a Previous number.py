total = 0

for i in range(10):
    if i == 0:
        total = i+i
        print(f"current number {i} previous number {i} sum {total}")
    else:
        total = i + i-1
        print(f"current number {i} previous number {i-1} sum {total}")

