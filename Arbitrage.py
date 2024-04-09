from collections import defaultdict

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

graph = defaultdict(dict)
for (token_from, token_to), (reserve_from, reserve_to) in liquidity.items():
    graph[token_from][token_to] = (reserve_from, reserve_to)
    graph[token_to][token_from] = (reserve_to, reserve_from)  # For reverse trade

def calculate_amount_out(amount_in, reserve_in, reserve_out):
    fee = 0.003  # 0.3% trading fee
    amount_in_with_fee = amount_in * (1 - fee)
    amount_out = (amount_in_with_fee * reserve_out) / (reserve_in + amount_in_with_fee)
    return round(amount_out, 6)  # Round to 6 decimal places

def find_profitable_path(graph, start_token, starting_amount=5.0, max_depth=4):
    # Stores the paths and their corresponding profits [(profit, path)]
    profitable_paths = []
    
    def dfs(current_token, current_amount, path, depth):
        if depth > max_depth:
            return
        for next_token, (reserve_in, reserve_out) in graph[current_token].items():
            next_amount = calculate_amount_out(current_amount, reserve_in, reserve_out)
            if next_token == start_token and next_amount > starting_amount:
                profitable_paths.append((next_amount, path + [next_token]))
                continue
            if next_token not in path:
                dfs(next_token, next_amount, path + [next_token], depth + 1)
    
    dfs(start_token, starting_amount, [start_token], 0)
    
    if profitable_paths:
        profitable_paths.sort(reverse=True)  # Sort paths by profit in descending order
        best_profit, best_path = profitable_paths[0]
        return f"path: {'->'.join(best_path)}, {start_token} balance={round(best_profit, 6)}"  # Round to 6 decimal places
    return "No profitable path found."

result = find_profitable_path(graph, "tokenB")
print(result)
