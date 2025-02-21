import hashlib
import itertools

# 크래킹할 MD5 해시값 (예: "password"의 MD5 해시)
target_hash = "81dc9bdb52d04dc20036dbd8313ed055"

# rockyou.txt 경로 (파일이 있는 폴더에 맞게 변경)
rockyou_path = "./dataset/rockyou.txt"

try:
    with open(rockyou_path, "r", encoding="latin-1") as file:
        for line in file:
            word = line.strip()  # 개행 문자 제거
            hash_attempt = hashlib.md5(word.encode()).hexdigest()  # 단어를 MD5 해시로 변환
            if hash_attempt == target_hash:
                print(f"[+] 해시 복호화 성공! 원본 값: {word}")
                break
            else:
                print(hash_attempt, " => X")
        else:
            print("[-] 사전에서 찾을 수 없습니다.")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {rockyou_path}")



# 6자리 모든 조합 생성 시 아래 항목 주석 해제
# charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
# for candidate in itertools.product(charset, repeat=6):
#     password = "".join(candidate)
#     hash_attempt = hashlib.md5(password.encode()).hexdigest()
#
#     if hash_attempt == target_hash:
#         print(f"[+] 해시 복호화 성공! 원본 값: {password}")
#         break
#     else:
#         print(f"{password} => x")
# else:
#     print("[-] 찾을 수 없습니다.")


# Brute Force Attack을 사용하는 경우, Jon the ripper나 hashcat 사용 권고