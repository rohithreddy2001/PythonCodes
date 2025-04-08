class Searching:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

if __name__ == "__main__":
    nums = [[3, 4, 5, 6, 7, 8, 0, 1, 2], [5, 6, 7, 0, 1, 2, 3, 4], [1]]
    target = 0
    c = Searching()
    for test_case in nums:
        print(f"Found at index: {c.search(test_case, target)}")
