
i = 0
n = int(input("State the number of terms: "))
n1, n2 = 0,1
print("Fibonacci Numbers")
while i<n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    i += 1
