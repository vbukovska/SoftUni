number = float(input())
input_metric = str(input())
result_metric = str(input())
output_number = 0

if input_metric == "m":
    output_number = number * 1000
elif input_metric == "cm":
    output_number = number * 10
else:
    output_number = number

if result_metric == "m":
    output_number = output_number / 1000
elif result_metric == "cm":
    output_number = output_number / 10

print(f'{output_number:.3f}')

