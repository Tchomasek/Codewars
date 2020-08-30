def combs(comb1, comb2):
    comb1_list = []
    comb2_list = []
    for pos in comb1:
        if pos == '*':
            comb1_list.append(1)
        else:
            comb1_list.append(0)
    #print(comb1_list)
    for pos in comb2:
        if pos == '*':
            comb2_list.append(1)
        else:
            comb2_list.append(0)
    #print(comb2_list)
    longer = max(len(comb1),len(comb2))
    #print(longer)
    for step in range(len(comb1)+len(comb2)):














combs("*..*","*.*")













'''Task

Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.

    Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be 5

Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.

Input/Output

    [input] string comb1

    A comb is represented as a string. If there is an asterisk ('*') in the ith position, there is a tooth there. Otherwise there is a dot ('.'), which means there is a missing tooth on the comb.

    Constraints: 1 ≤ comb1.length ≤ 10.

    [input] string comb2

    The second comb is represented in the same way as the first one.

    Constraints: 1 ≤ comb2.length ≤ 10.

    [output] an integer

    The minimum length of a purse Miss X needs.

'''
