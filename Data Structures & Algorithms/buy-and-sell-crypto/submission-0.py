class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given int arr of prices 
        # a single day to buy, and diff day to sell in future 
        # ret max profit, can also make no transactions -> 0

        # track max, and iterate from 2 pointers on both sides?
        # ALWAYS L-R

        # two pointers, track from beginning 0, 1 
        # if left number less than right number, calculate right - left 
        # want the main condition to be: buy LOW, sell HIGH 
        # otherwise, iterate -> move left to the right, move right + 1 
        # if profitable, store max of profit/max, still iterate r, moving r forward 

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                res = max((prices[r] - prices[l]), res)
            else:
                l = r
            r += 1
        return res
