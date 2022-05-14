a = input()
a = int(a)

if a % 4 != 0:
    print("False")
elif a % 4 == 0 and a % 100 != 0:
    print("True")
elif a % 100 == 0 and a % 400 != 0:
    print("False")
elif a % 400 == 0:
    print("True")
else:
    print("False")

#這是第三版test after 3
#總之變更點我在介面上都沒顯示過啊 更不用說回復了
#從剛剛到現在都只能直接推