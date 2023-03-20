# x=lambda mrng: mrng - 2
# print(x(-5))
# v=lambda sugar,salt, pepper: sugar*salt+pepper
# print(v(9,8,2))
def mrnglam(num):
    return lambda v: num+v
sum = mrnglam(8)
print(sum(6))