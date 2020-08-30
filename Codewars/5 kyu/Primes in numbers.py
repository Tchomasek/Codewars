def primeFactors(n):
    result = []
    i = 2
    while i<=n:
        if n%i == 0:
            result.append(i)
            n/=i
        else:
            i+=1
    print(result)
    result_set = sorted(list(set(result)))
    counts = []
    for i in range(len(set(result))):
        x = result.count(result_set[i])
        counts.append(x)
    print("denominators :", result_set)
    print("denominators count :", counts)
    result = ""
    for i in range(len(result_set)):
        if counts[i] == 1:
            result+="({})".format(result_set[i])
        else:
            result+="({}**{})".format(result_set[i],counts[i])
    return result




print(primeFactors(86240))






'''
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''

"""
def primeFactors(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret
"""
