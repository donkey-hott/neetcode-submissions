class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0

        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                ans += 1
                l, r = l + 1, r - 1
            elif (limit - people[l]) > people[r]:
                ans += 1
                l += 1
            if (limit - people[r]) < people[l]:
                ans += 1
                r -= 1
        return ans

