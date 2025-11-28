class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        benchmark = max(candies)
        arr = []
        for i in candies:
            if i+extraCandies >= benchmark:
                arr.append(True)
            else:
                arr.append(False)

        return arr
