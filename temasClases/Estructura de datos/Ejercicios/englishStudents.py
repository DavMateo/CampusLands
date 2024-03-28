n = int(input("English newspaper: "))
setEng = []
for i in range(n):
    setEng.append(input())


n = int(input("French newspaper: "))
setFrench = []
for i in range(n):
    setFrench.append(input())


result = set(setEng) - set(setFrench)
print("Student only English newspapers:", len(result))