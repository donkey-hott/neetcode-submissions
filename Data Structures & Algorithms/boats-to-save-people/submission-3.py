class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0

        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                ans += 1
                l, r = l + 1, r - 1
                continue
            if (limit - people[l]) > people[r]:
                ans += 1
                l += 1
            if (limit - people[r]) < people[l]:
                ans += 1
                r -= 1
        return ans
# [1,3,2,3,2]
# [1,2,2,3,3], l = 3

# [5,1,4,2], l = 6
# [1,2,4,5]

# [3,5,3,4], l = 5
# [3,3,4,4]

# [3,3,2,1], l = 3
# [1,2,2,3]

# [5,1,4,2], l = 10
# [1,2,4,5]
