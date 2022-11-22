def sort1(n,nums):
    ans=[0 for i in range(n)]
    for index,num in enumerate(nums):
        for i in num:
            ans[index]+=int(i)

    for indexA in range(len(ans)):
        for indexB in range(indexA+1,len(ans)):
            if ans[indexB] < ans[indexA]:
                ans[indexB],ans[indexA]=ans[indexA],ans[indexB]
                nums[indexB],nums[indexA]=nums[indexA],nums[indexB]

    for indexA in range(len(nums)):
        x=ans[indexA]
        for indexB in range(indexA+1,len(nums)):
            if ans[indexB]==x and nums[indexB]<nums[indexA]:
                ans[indexB],x=x,ans[indexB]
                nums[indexB],nums[indexA]=nums[indexA],nums[indexB]
    return nums
n=int(input())
nums=input().split(' ')
print(sort1(n,nums))