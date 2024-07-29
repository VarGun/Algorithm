n = input().strip()
parts = n.split('-')

def calculate_sum(expression):
    return sum(map(int, expression.split('+')))

initial_sum = calculate_sum(parts[0])
if n[0] == '-':
    answer = -initial_sum
else:
    answer = initial_sum

for part in parts[1:]:
    answer -= calculate_sum(part)

print(answer)
