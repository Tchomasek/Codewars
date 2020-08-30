def max_sequence(arr):
    negative=0
    positive=0
    for i in arr:
        if i<0:
            negative+=1
        else:
            positive+=1
    if negative==0:
        return sum(arr)
    elif positive==0:
        return 0
    else:
        arr1=arr
        result=[]
        x=[]
        for i in range(len(arr1)):
            for i in range(len(arr1)+1):
                x=arr1[:i]
                if sum(x)>sum(result):
                    result=x
            arr1=arr1[1:]

        for i in range(len(arr)):
            for i in range(len(arr)+1):
                arr=arr[:-1]
                if sum(x)>sum(result):
                    result=x
            arr=arr[:-1]

    return sum(result)







print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])) #155

'''The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.'''
