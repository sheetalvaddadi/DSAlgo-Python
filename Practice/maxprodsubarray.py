def maxSubarrayProduct(xs):
    result = xs[0]

    for i in range(len(xs)):

        product = xs[i]
        for j in range(i + 1, len(xs)):
            result = max(result, product)
            product *= xs[j]
        result = max(result, product)

    return str(result)

print(maxSubarrayProduct([2, 0, 2, 2, 0]))