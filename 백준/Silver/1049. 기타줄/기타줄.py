n, m = map(int, input().split())

package_prices = []
single_prices = []

for _ in range(m):
    package_price, single_price = map(int, input().split())
    package_prices.append(package_price)
    single_prices.append(single_price)

min_package_price = min(package_prices)
min_single_price = min(single_prices)

total_cost = 0

if min_package_price < min_single_price * 6:
    total_cost = (n // 6) * min_package_price
    if min_package_price < (n % 6) * min_single_price:
        total_cost += min_package_price
    else:
        total_cost += (n % 6) * min_single_price
else:
    total_cost = n * min_single_price

print(total_cost)
