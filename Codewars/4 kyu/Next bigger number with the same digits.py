def next_bigger(n):
    digits=[]
    result=-1
    max=0
    for char in str(n):
        digits.append(int(char))

    index=0
    curr=[]
    unchanged=[]
    for i in range(2,len(digits)+1):
        curr=digits[-i:]
        if curr[0]<curr[1]:
            index=i
            break
    else:
        return -1
    unchanged=digits[:-index]
    next=[]
    first=curr[0]
    for i in sorted(curr):
        if i>first:
            next.append(i)
            break
    curr.remove(next[0])

    result_list=unchanged+next+sorted(curr)
    result_string=''
    for i in result_list:
        result_string+=str(i)
    result=int(result_string)

    return result




print(next_bigger(9876543210))




2017





'''Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil'''
