import hash

def printHash(element):
    print(element, "=>", hash.hash(element))


testList=["","a","abc","message digest","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","12345678901234567890123456789012345678901234567890123456789012345678901234567890""The quick brown fox jumps over the lazy dog"]

for element in testList :
    printHash(element)


