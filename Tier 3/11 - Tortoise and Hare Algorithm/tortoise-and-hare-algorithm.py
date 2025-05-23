# HIGHLY ADVANCED. I SUGGEST YOU DO SOME RESEARCH ON THIS ONE
# FLOYD'S TORTOISE AND HARE CYCLE DETECTION ALGORITHM

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
      ptr1 = nums[ptr1]
      ptr2 = nums[ptr2]

    return ptr1

nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))