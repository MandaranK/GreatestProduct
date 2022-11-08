import random

def dataSet():

    file = open("DATA1.txt", "a")

    s = random.randint(2, 1000000)
    random.seed(s)
    file.write(str(s))
    file.write("\n")

    M = random.randint(2, 1000000)
    file.write(str(M))
    file.write("\n")

    n = random.randint(2, 100)
    file.write(str(n))
    file.write("\n")

    listN = []

    i = 0
    while i < n:
        num = random.randint(1, M)
        listN.append(num)
        file.write(str(num))
        file.write("\n")
        i = i + 1

    file.close()


    list1 = [0]
    list2 = [0]
    list3 = [0]
    list4 = [0]
    list5 = [0]

    if len(listN) < 4:
        print("Invalid (Not enough numbers)")

    j = 0
    while j <= n - 4:
        a = listN[j] * listN[j+1] * listN[j+2] * listN[j+3]
        list1.append(a)

        b = (listN[j])
        list2.append(b)

        c = (listN[j+1])
        list3.append(c)

        d = (listN[j+2])
        list4.append(d)

        e = (listN[j+3])
        list5.append(e)

        j = j + 1
        a = 0

    if list1.count(max(list1)) > 1:
        k = 0
        while k < len(list1):
            if list1.index(max(list1)) == k:
                print(str(list2[k])+"*"+str(list3[k])+"*"+str(list4[k])+"*"+str(list4[k])+"="+str(max(list1)))

                list2.pop(k)
                list3.pop(k)
                list4.pop(k)
                list5.pop(k)

            k = k + 1

    else:
        l = 0
        while l < len(list1):
            if list1.index(max(list1)) == l:
                print(str(list2[l])+"*"+str(list3[l])+"*"+str(list4[l])+"*"+str(list5[l])+"="+str(max(list1)))

            l = l + 1



i = 0
while i < 10:
    print(dataSet())
    i = i + 1