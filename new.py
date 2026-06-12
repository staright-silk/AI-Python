n=int(input("Enter number of elements: "))
nums=[]
for _ in range(n):
    num=float(input("Enter a number: "))
    if 1<=num<=1000:
        nums.append(num)
    else:
        print("Number out of range. Skipping.")
if not nums:
    print("The list is empty.")
else:
    largest=nums[0]
    smallest=nums[0]
    for num in nums[1:]:
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    print(f"largest number: {largest}")
    print(f"smallest number: {smallest}")
