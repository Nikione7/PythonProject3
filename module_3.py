calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    upper_list = [s.lower() for s in list_to_search]
    if string in upper_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
