#!/usr/bin/env python3

import sys

def extract_data_from_hamming(hamming_code):
    n = len(hamming_code)
    r = 0
    while (2**r) < (n + 1):
        r += 1
    
    error_pos = 0
    for i in range(r):
        pos = 2**i - 1
        value = 0
        for j in range(pos, n, 2**(i+1)):
            value ^= sum(int(b) for b in hamming_code[j:j + 2**i])
        if value:
            error_pos += pos + 1
    
    if error_pos:
        hamming_code = list(hamming_code)
        hamming_code[error_pos - 1] = '0' if hamming_code[error_pos - 1] == '1' else '1'
        hamming_code = ''.join(hamming_code)
    
    data = ''
    for i in range(n):
        if not (i & (i + 1)):
            continue
        data += hamming_code[i]
    
    return data

def receiver(frame):
    if not frame.startswith('1111') or not frame.endswith('0000'):
        print("Erro: Frame inválido")
        return
    hamming_payload = frame[4:-4]
    decoded_data = extract_data_from_hamming(hamming_payload)
    print(decoded_data)

if __name__ == "__main__":
    frame = sys.stdin.read().strip()
    receiver(frame)