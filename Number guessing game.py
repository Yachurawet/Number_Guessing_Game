import random

target = random.randint(1,10)
count = 0

while True:
    if count < 3:
        number = int(input())
        if number > target:
            print("เลขอาจจะมากไป ลองทายใหม่ดูสิ")
            print("*******************************")
            count += 1

        elif number < target:
            print("เลขอาจจะน้อยไป ลองทายใหม่ดูสิ")
            print("***********************************")
            count += 1
        else:
            print()
            print(" ** คุณนี้คือพระเจ้าชัดๆ **")
            break
    else:
        print("คุณได้ลองทายครบเเล้ว")
        print("คำตอบก็คือ %d" % target)
        print("***********************************")
        break
