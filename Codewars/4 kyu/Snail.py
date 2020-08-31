def snail(arr):
    result=[]
    a=len(arr)
    repeats=a*2-1
    dir_list=['right','down','left','up']
    dir=''
    for line in range(repeats):
        dir=dir_list[line%len(dir_list)]
        if dir=="right":
            for i in range(len(arr[0])):
                result.append(arr[0].pop(0))
                if not arr[0]:
                    del arr[0]

        if dir=="down":
            for i in range(len(arr)):
                result.append(arr[i].pop(-1))

        if dir=="left":
            for i in range(len(arr[-1])):
                result.append(arr[-1].pop(-1))
                if not arr[-1]:
                    del arr[-1]

        if dir=="up":
            for i in range(len(arr)):
                result.append(arr[-i-1].pop(0))





    return result








arr =  [[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
print(snail(arr))



'''Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].'''
