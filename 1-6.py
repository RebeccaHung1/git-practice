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
# now we would like to try the push

#test delete

print("正在測試")


