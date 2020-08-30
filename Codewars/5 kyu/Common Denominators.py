def convertFracts(lst):
    nums = []
    denoms = []
    denom_primes = []
    for pair in lst:
        nums.append(pair[0])
        denoms.append(pair[1])
    for num in denoms:
        denom_primes.append(primeFactors(num))
    denom_set = []
    for list in denom_primes:
        denom_set.extend(list)
    denom_set = sorted(set(denom_set))
    list_dict = []
    for list in denom_primes:
        dict = {}
        for num in list:
            dict[num] = dict.get(num,0)+1
        list_dict.append(dict)
    result = {}

    for dict in list_dict:
        for value,count in dict.items():
            if count > result.get(value,0):
                result[value] = count
    sum = 1
    for value,count in result.items():
        sum*= value**count
    result = []
    for i in range(len(nums)):
        x = int((sum/denoms[i]))
        y = x*nums[i]
        result.append([y,sum])
    return result

def primeFactors(n):
    result = []
    i = 2
    while i<=n:
        if n%i == 0:
            result.append(i)
            n/=i
        else:
            i+=1
    return result



[[77033412951888080, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
[[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
 #77033412951888085



a = [[27115, 5262], [87546, 11111111], [43216, 255689]]
print(convertFracts(a))

#[[1480, 2775], [175, 2775], [444, 2775]]


















'''
Common denominators

You will have a list of rationals in the form

 { {numer_1, denom_1} , ... {numer_n, denom_n} }

or

 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]

or

 [ (numer_1, denom_1) , ... (numer_n, denom_n) ]

where all numbers are positive ints.

You have to produce a result in the form

 (N_1, D) ... (N_n, D)

or

 [ [N_1, D] ... [N_n, D] ]

or

 [ (N_1', D) , ... (N_n, D) ]

or

{{N_1, D} ... {N_n, D}}

or

"(N_1, D) ... (N_n, D)"

depending on the language (See Example tests)

in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

Note:

Due to the fact that first translations were written long ago - more than 4 years - these translations have only irreducible fractions. Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.
Note for Bash:

input is a string, e.g "2,4,2,6,2,8"

output is then "6 12 4 12 3 12"
'''
