## QUIZ
def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n-1)
result = factorial(5)
print(result)