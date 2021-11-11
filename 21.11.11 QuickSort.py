import numpy as np

arrNum = np.array([54, 34, 31, 89, 67, 16, 52, 23], int)

#___처리
#피봇_필요
def partition(arr, left, right):
    low = left + 1
    high = right 
    pivot = arr[left]
    print("pivot값: {}, low값: {}, high값: {}"
          .format(pivot, arr[low], arr[high]))
    print("low인덱스: {}, high인덱스: {}"
          .format(low, high))
    
    print()
    while(low <= high):
        while low <= right and arr[low] < pivot:
            low += 1
            print("LOW카운트: [{}]".format(low))
        while high >= left and arr[high] > pivot:
            high -= 1
            print("HIGH카운트: [{}]".format(high))
            
        if low < high:
            print("교환 전~: {}".format(arrNum))
            arr[low], arr[high] = arr[high], arr[low]
            print("교환 후~: {}".format(arrNum))
    
    print()
    arr[left], arr[high] =arr[high], arr[left]
    print("파티션 결과: {}".format(arrNum))


def sortQuick(arr, left, right):
    if left < right:
        print("파티션 진행. . . . .")
        partition(arr, left, right)
        
 

#___출력
print("기본데이터: {}".format(arrNum))
print("======================")

sortQuick(arrNum, 0, len(arrNum)-1)

print("----------------------")

