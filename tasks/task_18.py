# Definitions

message = bytearray.fromhex('6c73d5240a948c86981bc294814d')
clear = bytearray('attack at dawn', 'utf-8')
new = bytearray('attack at dusk', 'utf-8')

def mod(a, b):
    c = bytearray()
    for i, j in zip(a, b):
        i, j = bin(i)[2:], bin(j)[2:]
        while len(i) < 8:
            i = '0' + i
        while len(j) < 8:
            j = '0' + j
        k = '0b' + ''.join(str((int(m) + int(n)) % 2) for m, n in zip(i, j))
        k = int(k, 2)
        c.append(k)
    return c

def hexstring(a):
    b = ''
    for i in a:
        i = hex(i)[2:]
        while len(i) < 2:
            i = '0' + i
        b = b + i
    return b

# Execution

if __name__ == '__main__':
    diff = mod(clear, new)
    modif = mod(message, diff)
    if mod(diff, modif) == message:
        print('Trafficking achieved.')
        print(hexstring(modif))