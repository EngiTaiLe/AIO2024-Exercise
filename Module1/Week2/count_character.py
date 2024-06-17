def check_text(data):
    try:
        data/2
    except TypeError:
        return True
    return False

def count_character(text):
    if not check_text(text):
        print("Your input must be a string")
        return
    result = {}
    for i in text:
        if i in result.keys():
            continue
        result[i] = text.count(i)
    sorted_result = {key:result[key] for key in sorted(result)}
    return sorted_result 

def count_character1(text):
    text = str(text)
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    sorted_result = {i:result[i] for i in sorted(result)}
    return sorted_result 

text = "Hello Vietnam" 
print(count_character(text))
print(count_character1(text))
