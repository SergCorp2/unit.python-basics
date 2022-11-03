# money = float(input("money"))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# a = list(map(float, per_cent.values()))
# b = a[0]
# c = a[1]
# d = a[2]
# e = a[3]
# d_a =int(money/100*b)
# d_b =int(money/100*c)
# d_c =int(money/100*d)
# d_d =int(money/100*e)
# deposit =[d_a, d_b, d_c, d_d]
# # print(deposit)
# max_d = max(deposit)
# print("Максимальная сумма, которую вы можете заработать —", max_d)

money = float(input("money:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = list(map(float, per_cent.values()))
c = 0
for i in a:
    d = int(money/100*i)
    if d > c:
       c = d
print("Максимальная сумма, которую вы можете заработать —", c)





