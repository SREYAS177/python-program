n_terms=int(input("Enter the number of terms: "))
n1, n2 = 0, 1
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1, n2, end=" ")
    for _ in range(2, n_terms):
        nth = n1 + n2
        print(nth, end=" ")
        n1, n2 = n2, nth