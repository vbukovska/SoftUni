categories = input().split(', ')
storage = {category: {} for category in categories}
n = int(input())
for _ in range(n):
    cat, item, data = input().split(' - ')
    data = {feature[0]: feature[1] for feature in [features.split(':') for features in data.split(';')]}
    storage[cat][item] = data

count_elements = sum([int(dictionary['quantity']) for items_d in storage.values() for dictionary in items_d.values()])
quality_sum = sum([int(dictionary['quality']) for items_d in storage.values() for dictionary in items_d.values()])
categories_count = len(storage)
average_quality = quality_sum / categories_count

print(f'Count of items: {count_elements}')
print(f'Average quality: {average_quality:.2f}')
[print(f"{cat} -> {', '.join(storage[cat].keys())}") for cat in storage.keys()]

