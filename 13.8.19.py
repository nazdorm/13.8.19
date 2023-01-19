kol_bil = int(input("Сколько билетов хотите приобрести?: "))
sum = 0
for x in range(kol_bil):
    print("Введите возраст", x + 1, "покупателя :")
    old = int(input())
    if old < 18:
        sum += 0
    elif old >= 18 and old < 25:
        sum += 990
    elif old > 25:
        sum += 1390
if kol_bil > 3:
    sum -= sum * 0.1
print("Сумма к оплате: ", sum,"руб.")