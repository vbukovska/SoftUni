book_pages = int(input())
reading_speed = int(input())
time_limit = int(input())

tot_hours = book_pages / reading_speed
per_day = tot_hours / time_limit

print(per_day)

