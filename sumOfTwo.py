import time, sys, random

if len(sys.argv) !=3:
    print("Usage: python3 sumOfTwo.py <list size> <target>, target between 0 and 2000")
    sys.exit()

def twoSum1(nums, target):
    i={}
    for a in range(len(nums)):
        if (target-nums[a]) in i:
            if a < i[target-nums[a]]:
                return [a, i[target-a]]
            else:
                return [i[target-nums[a]], a]
        else:
            i[nums[a]]=a


def twoSum2(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]+nums[j]==target:
                return [i, j]


nums=[0]*int(sys.argv[1])
for i in range(int(sys.argv[1])):
    nums[i]=random.randint(0, 1000)
target=int(sys.argv[2])
start1 = time.time()
twoSum1(nums, target)
end1=time.time()
start2=time.time()
twoSum2(nums,target)
end2=time.time()

print("Naive way to calculate: %s \nOptimized way: %s" % (end2-start2, end1-start1))






