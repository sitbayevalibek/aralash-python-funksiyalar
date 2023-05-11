def lambda_funksiya(n):
    return lambda a: a**n
kvadrat = lambda_funksiya(2)
kub = lambda_funksiya(3)
print(kvadrat(5))
print(kub(5))
