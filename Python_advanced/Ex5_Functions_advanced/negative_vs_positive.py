nums = [int(n) for n in input().split()]

negative_nums = list(filter(lambda x: x < 0, nums))
sum_negatives = sum(negative_nums)
positive_nums = list(filter(lambda x: x >= 0, nums))
sum_positives = sum(positive_nums)
abs_sum_negatives = abs(sum_negatives)

print(f"{sum_negatives}")
print(f"{sum_positives}")

if abs_sum_negatives > sum_positives:
    print(f"The negatives are stronger than the positives")
elif abs_sum_negatives < sum_positives:
    print(f"The positives are stronger than the negatives")