class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        动态演示双指针移动零的过程。
        """
        print(f"初始数组: {nums}")
        pos = 0
        for i in range(len(nums)):
            print(f"遍历到下标 {i}, 元素 {nums[i]}")
            if nums[i] != 0:
                print(f"  非零，nums[{pos}] <- {nums[i]}")
                nums[pos] = nums[i]
                pos += 1
            else:
                print(f"  是零，跳过")
            print(f"  当前数组: {nums}, pos={pos}")
        for i in range(pos, len(nums)):
            print(f"将下标 {i} 位置填 0")
            nums[i] = 0
            print(f"  当前数组: {nums}")
        print(f"最终结果: {nums}")

nums = [0, 1, 0, 3, 12]
T1 = Solution()
T1.moveZeroes(nums)
print(f"最终输出: {nums}")