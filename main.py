k = 0
while True:
    a = int(input())
    if a % 5 == 0 or a % 9 == 0:
        k += 1
    if a == 0:
        print(k-1)
        break
   
