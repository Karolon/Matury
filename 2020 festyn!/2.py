a = 13
b = 21

mod_counter = 0

while b != 0:
    c = a%b
    mod_counter += 1
    a = b
    b = c

print(a, mod_counter)
#1,1,2,3,5,8,13,21,34,55

def NWD(a, b):
    zq