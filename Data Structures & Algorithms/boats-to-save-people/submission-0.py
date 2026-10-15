class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            sm = people[l] + people[r]

            if sm <= limit:
                l += 1  # Lightest person gets on the boat

            r -= 1      # Heaviest person gets on the boat
            boats += 1

        return boats
        