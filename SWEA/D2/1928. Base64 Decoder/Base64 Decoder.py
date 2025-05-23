T = int(input())

# Base64 표준 문자 매핑
base64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for tc in range(1, T+1):
    encoded = input()
    
    # 패딩 문자 제거
    padding_count = encoded.count('=')
    encoded = encoded.rstrip('=')
    
    # 이진수로 변환
    binary = ''
    for char in encoded:
        if char in base64_chars:
            binary += bin(base64_chars.index(char))[2:].zfill(6)
    
    # 패딩 비트 제거
    if padding_count > 0:
        binary = binary[:-padding_count*2]
    
    # 8비트씩 묶어서 ASCII 문자로 변환
    result = ''
    for i in range(0, len(binary), 8):
        if i + 8 <= len(binary):
            byte = binary[i:i+8]
            result += chr(int(byte, 2))
    
    print(f"#{tc} {result}")
