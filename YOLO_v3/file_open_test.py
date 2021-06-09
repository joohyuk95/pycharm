classesFile = './coco.names'

with open(classesFile, 'rt') as f:
    classNames1 = f.read().rstrip('\n').split('\n')     # useless

with open(classesFile, 'rt') as f:          # this is cool
    classNames2 = f.read().split('\n')

with open(classesFile, 'rt') as f:
    classNames3 = f.read().rstrip('\n')

print(classNames1)
print(classNames2)
