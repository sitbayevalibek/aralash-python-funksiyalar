def kv_kub_lambda(n):
    return lambda a: a ** n
while True:
    u = int(input("Butun son kiriting: "))

    kvadrat = kv_kub_lambda(2)
    kub = kv_kub_lambda(3)
    
    print(f"{u} ning kvadrati: {kvadrat(u)}")
    print(f"{u} ning kubi: {kub(u)}")
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break