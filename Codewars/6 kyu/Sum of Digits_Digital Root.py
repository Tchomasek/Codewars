def digital_root(n):
    while True:
        if n > 9:
            n_str=str(n)
            n=0
            for num in n_str:
                n+=int(num)
        else:
            return n

print(digital_root(456))
