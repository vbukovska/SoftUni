length = int(input())
width = int(input())
height = int(input())
used_volume = float(input())
tot_volume = length * width * height
tot_liters = tot_volume * 0.001
free_volume = tot_liters * (1 - used_volume / 100)
print(free_volume)
