from typing import List 


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        self.nums = nums
        self.N = len(nums)
        for i in range(self.N):
            slow = i # 快慢指针
            fast = self.next_pos(i)
            while nums[fast] * nums[slow] > 0 and nums[self.next_pos(fast)] * nums[slow] > 0:
                if fast == slow:
                    if slow == self.next_pos(slow):
                        break
                    return True
                slow = self.next_pos(slow)
                fast = self.next_pos(self.next_pos(fast))
            self.nums[i] = 0
        return False

    def next_pos(self, index):
        return (index + self.nums[index]) % self.N


if __name__ == "__main__":
    s = Solution()
    print(s.circularArrayLoop([1]))