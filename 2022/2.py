def trzycifrowe_dwypierwsze():
    l_dwupierwsze = []
    l_pierwsze_jednocyfrowe = [2,3,5,7]
    for n in range(10, 100):
        flag = True
        for i in range(2,n):
            if n%i == 0:
                flag = False
        if flag:
            for i in range(4):
                l_dwupierwsze.append(n//10*100+l_pierwsze_jednocyfrowe[i]*10+n%10)
    
    return l_dwupierwsze
 
    
print(trzycifrowe_dwypierwsze())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def czy_dwupierwsza(n):
    parzyste = 0
    nieparzyste = 0
    licznik_pozycji = 1
    mnożnik = 1
    while n > 0:
        if licznik_pozycji % 2 == 1:
            nieparzyste += (n % 10) * mnożnik
        else:
            parzyste += (n % 10) * mnożnik
            mnożnik *= 10
        n //= 10
        licznik_pozycji += 1
    return ["NIE", "TAK"][isPrime(nieparzyste) and isPrime(parzyste)]
    
    
print(czy_dwupierwsza(1213))