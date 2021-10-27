'''
x = 17
y = 20
t = x   # t = 17
x = y   # x = 20
y = t   # y = 17

print(x, y, t)
print()

#==============================

a = 7
b = 6
c = a*b
b = c-a
a = (c%b)+(c-b)
print (a, b, c)
print()

#==============================

height = input("키(cm): ")
weight = input("몸무게(kg): ")

height = int(height)
weight = int(weight)
bmi = (weight/(height*height)) * 10000

print("체질량 지수 = ", bmi)
print()

#==============================

sum = 0
f = open("input.txt", "r") # r means read
lines = f.readlines() # read all lines

for i in range(len(lines)): # 0~
    num = int(lines[i])
    print(num)
    sum = sum + num;

print("합계 : ", sum)
f.close()

f = open("output.txt", "w") # w means write
f.write("합계 : " + str(sum)) # str(...) function need
f.close()

print()
'''

#==============================

pay = 14000
age = int(input("나이를 입력하세요: "))

if (age >= 60):
    print("30% 할인 대상입니다.\n찜질방 이용 요금: {}원".format(int(pay*0.7)))
elif (age <= 10):
    print("20% 할인 대상입니다.\n찜질방 이용 요금: {}원".format(int(pay*0.8)))
else:
    print("할인 대상이 아닙니다.\n찜질방 이용 요금: {}원".format(int(pay)))

