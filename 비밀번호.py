pw = "0000"
count =0

while pw != "1234" and count <3:
    pw = input("비밀번호 입력:")
    count +=1

if count >= 3:
    print("입력 오류 3번발생")
else:
    print("문이 열립니다.")
