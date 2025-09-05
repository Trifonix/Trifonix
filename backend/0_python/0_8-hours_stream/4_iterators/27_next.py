myiter = iter([12,13,14])
print(myiter.__next__())
print(next(myiter))
print(myiter.__next__())
# print(myiter.__next__()) : error
print(myiter)

# myiter = iter('helloworld')
