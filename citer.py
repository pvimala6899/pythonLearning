class mrng:
    def __iter__(num):
        num.v = 1
        return num
    
    def __next__(num):
        y = num.v
        num.v +=1
        return y
soft = mrng()
itermrng = iter(soft)


print(next(itermrng))

