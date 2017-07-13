#!/usr/bin/env python
f = open ("basha1.txt")
print("\nLoop directly over file")
print("-" * 60)
##for line in f:
  print(line.strip())
print("-" *60)

f.seek(0)
my_content = f.readlines()
print("\nUse readlines method")
print("-" * 60)
for line in my_content:
    print(line.strip())
print("-" * 60)


open("basha1.txt") as f:
    print("\nUse with and loop over file")
    print("-" * 60)
    for line in f:
        print(line.strip())
print("-" * 60)



print("\nWriting file.")
f = open("basha1.txt", "w")
f.write('whatever2\n')
f.close()



print("\nAppending file.")
with open("basha1.txt", "a") as f:
    f.write('something else\n')
print()
