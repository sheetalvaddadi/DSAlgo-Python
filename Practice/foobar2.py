def solution(xs):
    all_subsets = []
    products = []
    subset = []

    def dfs(i):
        if i >= len(xs):
            all_subsets.append(subset.copy())
            return
        subset.append(xs[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
    dfs(0)

    # products of all_subsets
    for x in all_subsets:
        product = 1
        for y in x:
            product *= y
        products.append(product)

    return str(max(products))

print(solution([-2, 0 , 1, 2]))





