ticket = int(input("введите количество билетов:"))
age = input("введите возраст:\n")
normals = []
positives = []
zeros = []
while age != "":
    num = int(age)
    if num < 18:
        zeros.append(num)
    elif num >= 25:
        positives.append(num)
    else:
        normals.append(num)
    age = input()
ticket_price = len(normals) * 990 + len(positives) * 1390
if len(normals) + len(positives) + len(zeros) > 3:
    ticket_price = ticket_price - ticket_price * 0.1
print("сумма к оплате:", ticket_price)