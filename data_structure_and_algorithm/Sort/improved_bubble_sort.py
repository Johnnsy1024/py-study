class ImproveBubbleSort:
    def improve_bubble_sort(self, nums):
        for i in range(len(nums) - 1):
            swapped = False   # set swapped to False at the beginning of each loop
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums

s = ImproveBubbleSort()
arr = [1, 2, 4, 3, 6, 5]
s.improve_bubble_sort(arr)
print(arr)