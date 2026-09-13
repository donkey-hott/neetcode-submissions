class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr, start, end):
            l, r =  start, end

            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
        
        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
