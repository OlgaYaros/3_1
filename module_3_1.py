calls = 0

def count_calls():
    global calls
    calls += 1
    
def string_info(string):
    count_calls()
    A = [len(string), string.upper(), string.lower()]

    return A

def is_contains(string, List):
    count_calls()
    string = string.upper()
    k = 0
    for i in range(len(List)):
        List[i] = List[i].upper()
        if (string == List[i]):
            return True
            break
        else:
            k += 1
    if (k == len(List)):
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
