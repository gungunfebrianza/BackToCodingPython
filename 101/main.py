iniint = 3
print(iniint)
print(type(iniint))

inistr = "5"
print(inistr)
print(type(inistr))

inifloat = 3.7
print(inifloat)
print(type(inifloat))

print(type(3.7 + 8))  # become float
print(type(3 + 8))  # become int
print(type(3 + 8.0))  # become float
print(type(3.7 + 8.0))  # become float

nama = "gun, febrianza"
print(nama)
print(type(nama))
print(nama[0])  # g
print(nama[1])  # u
print(nama[2])  # n
print(nama[0:3])  # gun

name = nama.split(",")
print(name)  # ['gun', ' febrianza']
print(name[0])  # gun
print(name[1])  #  febrianza
print(type(name))  # <class 'list'>
print(name[0].capitalize())  # Gun
print(name[1].capitalize())  #  Febrianza
print(nama.capitalize())  # Gun,  Febrianza
print(nama.upper())  # GUN, FEBRIANZA
print(nama.lower())  # gun, febrianza

print(int(inifloat))  # become int 3.7 become 3
print(float(iniint))  # become float 3 become 3.0
print(str(iniint))  # become str 3 become '3'
print(str(inifloat))  # become str 3.7 become '3.7'
print(float(inistr))  # become float '5' become 5.0
print(int(inistr))  # become int '5' become 5

print(iniint / 2)  # become float 3/2 = 1.5
print(inifloat / 2)  # become float 3.7/2 = 1.85

myIntList = [1, 2, 3, 4, 5]
print(myIntList)
print(type(myIntList))  # <class 'list'>
print(myIntList[0])  # 1
print(myIntList[1])  # 2
print(myIntList[0:3])  # [1, 2, 3]
print(myIntList[0:3][2])  # 3

myMultList = [1, 2, 3, 4, 5] * 3
print(myMultList)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

myHeterogeneousList = [1, 2.5, "3", True]
print(myHeterogeneousList)  # [1, 2.5, '3', True]
print(type(myHeterogeneousList))  # <class 'list'>
