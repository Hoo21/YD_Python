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
