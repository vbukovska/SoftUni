percent_completed = int(input())


def loading_bar(loaded):
    if loaded == 100:
        return f'{loaded}% ' + 'Complete!' + '\n' + '[' + (loaded // 10) * '%' + (10-(loaded // 10)) * '.' + ']'
    else:
        return f'{loaded}% ' + '[' + (loaded // 10) * '%' + (10-(loaded // 10)) * '.' + ']' + '\n' + 'Still loading...'


text_to_print = loading_bar(percent_completed)
print(text_to_print)