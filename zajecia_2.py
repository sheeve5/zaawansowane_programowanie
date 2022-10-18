def hello(name: str, surname: str) -> str:
    return "Cześć {} {}!".format(name, surname)


def multiply(x: int, y: int) -> int:
    return x * y


def isEven(x: int) -> bool:
    return x % 2 == 0


def checkSum(x: int, y: int, z: int) -> bool:
    return x + y >= z


def listContains(list: list, x: int) -> bool:
    for i in list:
        if i == x:
            return True
    return False

def listCube(list1: list, list2: list) -> list:
    list_combined =[]
    for i in list1:
        if not listContains(list_combined, i**3):
            list_combined.append(i**3)
    for i in list2:
        if not listContains(list_combined, i ** 3):
            list_combined.append(i ** 3)
    return list_combined

print("\nzadanie 1")
text = hello("Jan", "Kowalski")
print(text)

print("\nzadanie 2")
x = 2
y = 7
print("{}*{}={}".format(x, y, multiply(x, y)))

print("\nzadanie 3")
x = 19
print("liczba: {}".format(x))
even = isEven(x)
if even:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")

print("\nzadanie 4")
x = 2
y = 8
z = 20
print("Czy  {} + {} >= {} ?".format(x, y, z))
print(checkSum(x, y, z))

print("\nzadanie 5")
list = [1, 2, 5, 7]
x = 6
print("lista: {}, wartość poszukiwana: {}".format(list, x))
print(listContains(list, x))

print("\nzadanie 6")
list1 = [1, 2, 5, 7, 3, 1]
list2 = [1, 2, 5, 7, 8]
print("lista 1: {}\nlista 2: {}\nwynik dzialania funkcji: {}".format(list1,list2,listCube(list1,list2)))