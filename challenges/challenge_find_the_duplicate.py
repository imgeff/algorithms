def find_duplicate(nums):
    if len(nums) > 1:
        numbers_ordered = sort_by_pivot(nums)
        for index, num in enumerate(numbers_ordered):
            if (
                index == len(nums) - 1 or type(num) != int
                    or type(numbers_ordered[index + 1]) != int or num < 0):
                return False
            if num == numbers_ordered[index + 1]:
                return num
    return False


def sort_by_pivot(nums):
    pivot = nums[-1]
    index_pivot = len(nums) - 1
    index = 0
    change = 0
    while True:
        num = nums[index]
        if num > pivot:
            nums[index_pivot], nums[index] = num, pivot
            pivot = nums[index_pivot]
            change += 1
        if len(nums[:index_pivot + 1]) - index == 1:
            if change == 0:
                break
            index_pivot -= 1
            pivot = nums[index_pivot]
            index = 0
            change = 0
        else:
            index += 1
    return nums


# if __name__ == "__main__":
#     nums = [1, 1]
#     print(find_duplicate(nums))
