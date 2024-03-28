test = {
    123: ["David", 56, 453.256],
    456: ["Mateo", 25, 955.552]
}

print(test.keys())
print(len(test.keys()))
print(test[123][0])


variable = test.keys()
print("Test:", variable)

print([*variable][0])