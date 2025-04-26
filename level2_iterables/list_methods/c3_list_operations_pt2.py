print()
print("============================== Challenge 3: List Operations part 2 ================================")
print()

list1 = [4,2,7,1,9]
list2 = [11,5,8]
print(f"List1: {list1} List2: {list2}" )

print()

list1.sort()
print(f"Sorted list1: {list1}")

list2.reverse()
print(f"Reversed list2: {list2}")

list1.extend(list2)
print(f"Extended list1: {list1}")

print()
print("="*100)
print()