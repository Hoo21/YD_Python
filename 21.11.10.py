
point = 0
sum = 0
while (sum < 20):
    point = int(input("다트 점수를 입력하세요: "))
    print("이번 점수는 ", point)
    sum += point
print("합계 점수는 ", sum)
print()


#===============================================

for i in range(1, 16):
    print("i = " + str(i))
    
    
print()

sum = 0
for i in range(1, 16):
    if(i%2 != 0):
        sum += i
print("홀수의 합 = " + str(sum))