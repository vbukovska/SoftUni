min_walking = int(input())
num_walking = int(input())
calories_added = int(input())

calories_spent = num_walking * min_walking * 5
if calories_spent >= calories_added / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_spent}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_spent}.')