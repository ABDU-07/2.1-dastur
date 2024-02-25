import os

ls = [1,2,3,4,5]
while 1:
    os.system("cls")
    print("1- qoshish")
    print("2- ochirish")
    a = int(input())
    if a == 1:
        print("1- append")
        print("2- inser")
        b = int(input())
        if b == 1:
            b = int(input("qoshashish 'int': "))
            ls.append(b)
            print(ls,end='\n\n')
            print("\n1- Qaytadan boshlash: ")
            print("2- Tugatish: ")
            b = int(input())
            if b == 1:
                print()
            elif b == 2:
                exit()
            a = int(input())
        elif b == 2:
            b = int(input("Nechani indexga qoshasiz: "))
            a = input("qoshashish : ")
            ls.insert(b,a)
            print(ls)
            print("\n1- Qaytadan boshlash: ")
            print("2- Tugatish: ")
            d = int(input())
            if d == 1:
                pass
            elif d == 2:
                exit()
    elif a == 2:
        print("1- pop")
        print("2- removf")
        print("3- clear")
        b = int(input())
        sum = sum(ls)
        if sum == 0:
            print("List bosh")
            print("\n1- Qaytadan boshlash: ")
            print("2- Tugatish: ")
            b = int(input())
            if b == 1:
                print()  
            elif b == 2:
                exit()
        if b == 1:
            print("1- Indexdan ochirish")
            print("2- ohiridan ochirish")
            b = int(input())
            if b == 1:
            
                b = int(input("Nechini index: "))
                ls.pop(b)
                print(ls)
                print("\n1- Qaytadan boshlash: ")
                print("2- Tugatish: ")
                b = int(input())
                if b == 1:
                    print()
                elif b == 2:
                    exit()
                elif b == 2:
                    ls.pop()
                    print(ls)
        elif b == 2:
            print("Nmani ochirasiz")
            print(ls)
            b = input()
            ls.remove('b')
            print(ls)
            print("\n1- Qaytadan boshlash: ")
            print("2- Tugatish: ")
            b = int(input())
            if b == 1:
                print()
            elif b == 2:
                exit()
        elif b == 3:
            ls.clear()
            print(ls)
            print("\n1- Qaytadan boshlash: ")
            print("2- Tugatish: ")
            b = int(input())
            if b == 1:
                print()
            elif b == 2:
                exit()