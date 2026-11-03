file = open('Dane/konta.txt')

data = []

for f in file:
    f = f.strip()
    f = f.split()
    data.append(f)
    
#1
konta = set()
for d in data:
    konta.add(d[0])
    
print(len(konta))

#2
obserwacje = []

for d in data:
    obserwacje.append(d[1])

fejk_konta = list(konta-set(obserwacje))

print(*fejk_konta)

#3

licznik = 0
for i,d in enumerate(data):
    if d[::-1] in data[i:]:
        licznik += 1
        
print(licznik)

#4
max_konto = ["", 0]

konta_powtarzanie = []

for d in data:
    konta_powtarzanie.append(d[0])

for k in list(konta):
    t = konta_powtarzanie.count(k)
    if t > max_konto[1]:
        max_konto = k, t
        
print(max_konto)


#5
data_bez_fejk = []

max_obserwacji = ["", 0]

for d in data:
    if d[0] not in fejk_konta:
        data_bez_fejk.append(d)
        
for k in list(konta):
    t = data_bez_fejk.count(k)
    if t > max_obserwacji[1]:
        max_obserwacji = k, t
        
print(max_konto)



