list_1 = [1,3,2,4,5,6,9,7,8,10]
list_1.sort()
first = 0
last = len(list_1) - 1
mid = (first + last) // 2
item = int(input("Enter a number to be searched : "))
count = 0
found = False
while (first <= last and not found):
    count += 1
    mid = (first + last) // 2
    if list_1[mid] == item:
        print(f"Found at location {mid} in {count} iteration(s)")
        found = True
    else:
        if item < list_1[mid]:
            last = mid -1
        else:
            first = mid + 1
if found == False:
    print("Number not found.")