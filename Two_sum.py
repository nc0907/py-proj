#Bruteforce approach
def brute2sum(nums, target):
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            num=target-nums[i]
            if num == nums[j]:
                return [i,j]
            
nums=[1,2,3,4,5,6,7]
target=9
print(brute2sum(nums,target))

#Optimized approach
def twoSum(nums, target):
    dict_of_x=dict()
    len_of_nums=len(nums)
    for i in range(len_of_nums):
        val= target - nums[i]
        if(val in dict_of_x):
            return [dict_of_x[val],i]
        dict_of_x[nums[i]]=i
        print (dict_of_x)
        i+=1
nums=[1,2,3,4,5,6,7]
target=9
print(twoSum(nums,target))
