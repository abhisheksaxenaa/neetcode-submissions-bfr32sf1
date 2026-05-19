class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coin change
        # C(n) = 1 + min(C(n-i))
        coin_store = {}
        queue = []
        coin_store[0] = 0

        for coin in coins:
            coin_store[coin] = 1
        
        # print(coin_store)
        
        def change(amount: int) -> int:
            # print(f'Amount: {amount}')
            if amount in coin_store:
                return coin_store.get(amount)
            if amount < 0:
                return 2**31
            for coin in coins:
                total = change(amount - coin)
                # print(f'total : {total}')
                coin_store[amount] = min(coin_store.get(amount, 2**31), 1 + total)
            return coin_store[amount]

        change(amount)
        # print(coin_store)
        total = coin_store.get(amount)
        return total if total < 2**31 else -1