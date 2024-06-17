def find_max_num(data,k):
    max_nums = []
    for i in range(len(data)):
        if (i + k) == len(data) + 1:
            return max_nums
        current_list = data[i:i+k]
        max_num = max(current_list)
        max_nums.append(max_num) 

def find_max_num1(data,k):
    max_nums = []
    start = range(len(data)-k+1)
    end = range(k,len(data)+1)
    for start_i, end_i in zip(start,end):
        current_list = data[start_i:end_i]
        max_num = max(current_list)
        max_nums.append(max_num)
    return max_nums

data = [3,4,5,1,-44,5,10,12,33,1]
print(find_max_num(data,3))
print(find_max_num1(data,3))