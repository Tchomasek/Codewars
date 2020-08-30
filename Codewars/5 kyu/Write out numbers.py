def number2words(n):
    num_str=str(n)
    list_ones=['zero','one','two','three','four','five','six','seven','eight','nine']
    list_teens=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    list_tens=['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n<1:
        return 'zero'
    if n<10:
        return list_ones[n]

    result=''
    mod=False
    for i in range(len(num_str)):
        if mod:
            mod=False
            continue
        else:
            x=num_str[i:]
        if x[0]=='0':
            print('*')
            continue
        num=int(x)
        print(num)
        if num<1:
            result+='zero'
        elif num<10:
            if num_str[-2] != '0':
                result+='-'
            result+=list_ones[num]

        elif num<20:
            result+=list_teens[int(x[1])]
            break
        elif num<100:
            sub_result=''
            sub_result+=list_tens[int(x[0])-2]
            result+=sub_result
        elif num<1000:
            sub_result=list_ones[int(x[0])]
            result+=sub_result+' '+'hundred'+" "
        elif num<10000:
            result+=list_ones[int(x[0])]+" "+"thousand"+ " "
        elif num<20000:
            result+=list_teens[int(x[1])]+" thousand"+ " "
            mod=True
        elif num<100000:
            if num_str[1] != '0':
                result+=list_tens[int(x[0])-2]+"-"
            else:
                result+=list_tens[int(x[0])-2]+" thousand"+ " "
        elif num<110000:
            if num_str[1] == '0' and num_str[2] == '0':
                result+=list_ones[int(x[0])]+" hundred thousand "
            else:
                result+=list_ones[int(x[0])]+" hundred "
        elif num<1000000:
            result+=list_ones[int(x[0])]+" hundred "


    return result







print(number2words(520944))


'''Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.

Examples
number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
number2words(9)  ==>  "nine"
number2words(10)  ==>  "ten"
number2words(17)  ==>  "seventeen"
number2words(20)  ==>  "twenty"
number2words(21)  ==>  "twenty-one"
number2words(45)  ==>  "forty-five"
number2words(80)  ==>  "eighty"
number2words(99)  ==>  "ninety-nine"
number2words(100)  ==>  "one hundred"
number2words(301)  ==>  "three hundred one"
number2words(799)  ==>  "seven hundred ninety-nine"
number2words(800)  ==>  "eight hundred"
number2words(950)  ==>  "nine hundred fifty"
number2words(1000)  ==>  "one thousand"
number2words(1002)  ==>  "one thousand two"
number2words(3051)  ==>  "three thousand fifty-one"
number2words(7200)  ==>  "seven thousand two hundred"
number2words(7219)  ==>  "seven thousand two hundred nineteen"
number2words(8330)  ==>  "eight thousand three hundred thirty"
number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"'''
