def count_character_in_file(file):
    a_file = open(file,'r')
    data = a_file.read()
    a_file.close()
    words = data.lower().split()
    result = {}
    for i in words:
        if i in result.keys():
            continue
        result[i] = words.count(i)
    sorted_result = {key:result[key] for key in sorted(result)}
    return sorted_result

def read_file(file):
    with open(file,"r") as file:
        a_file = file.read()
        file.close()
    return a_file
def text_preprocessing(file):
    file = file.lower()
    file = file.replace(",","")
    file = file.replace(".","")
    return file.split()
def count_char_in_file(file):
    file = read_file(file)
    words = text_preprocessing(file)
    result = {}
    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    sorted_result = {i:result[i] for i in sorted(result)}
    return sorted_result 

print(count_char_in_file('/Users/macbook/downloads/data.txt'))
print(count_character_in_file('/Users/macbook/downloads/data.txt'))