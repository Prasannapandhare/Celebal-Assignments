def upper_triangular(n):
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input("Enter the number of rows for the upper triangular pattern: "))
upper_triangular(n)
