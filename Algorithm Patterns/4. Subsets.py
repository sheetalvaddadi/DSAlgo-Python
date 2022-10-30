# This is not permutations, only unique subsets are returned
# No duplicates in inputs
# Time n * 2^n
def no_duplicate_subsets(nums):
    result =[]
    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        # To add the element
        subset.append(nums[i])
        dfs(i + 1)

        # To add nothing []
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result

def possible_duplicates_subsets(nums):
        nums.sort()  # So duplicates remain in same places

        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Adding the element
            subset.append(nums[i])
            dfs(i + 1)

            # Adding nothing, []
            subset.pop()
            while (i + 1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1
            dfs(i + 1)

        dfs(0)
        return result

print(no_duplicate_subsets([1,2,3]))
print(possible_duplicates_subsets([1,2,5]))

'''
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
[[1, 2, 5], [1, 2], [1, 5], [1], [2, 5], [2], [5], []]
'''