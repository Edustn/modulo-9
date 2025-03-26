#!/usr/bin/env python3

import sys

def generate_hamming_code(data):
    data = list(data)
    m = len(data)
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    
    hamming_code = [None] * (m + r)
    j = 0
    for i in range(1, len(hamming_code) + 1):
        if i & (i - 1) == 0:
            hamming_code[i - 1] = 0
        else:
            hamming_code[i - 1] = int(data[j])
            j += 1
    
    for i in range(r):
        pos = 2**i - 1
        value = 0
        for j in range(pos, len(hamming_code), 2**(i+1)):
            value ^= sum(hamming_code[j:j + 2**i])
        hamming_code[pos] = value
    
    return ''.join(map(str, hamming_code))

def sender(payload):
    header = '1111'
    terminator = '0000'
    hamming_payload = generate_hamming_code(payload)
    frame = header + hamming_payload + terminator
    print(frame)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sender(sys.argv[1])
    else:
        print("Erro: Nenhum payload fornecido.")