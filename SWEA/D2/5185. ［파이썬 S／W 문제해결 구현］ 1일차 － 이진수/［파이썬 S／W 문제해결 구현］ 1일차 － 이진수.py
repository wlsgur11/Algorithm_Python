T = int(input())
for i in range(1, T+1):
    N, nums = input().split()
    N = int(N)
    binary = bin(int(nums, 16))[2:]  # 2진수 변환 (앞에 '0b' 제거)
    binary = binary.zfill(N * 4)      # (N * 4)자리수로 0 채워주기
    print(f"#{i} {binary}")