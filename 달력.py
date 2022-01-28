
m=int(input("월 입력:"))

if m in [1,3,5,7,8,10,12]:
    print("31일 까지")
elif m==2:
    print("28일 혹은 29일까지")
elif m in [4,6,9,11]:
    print("30일까지")
else:
    print("입력오류!")
