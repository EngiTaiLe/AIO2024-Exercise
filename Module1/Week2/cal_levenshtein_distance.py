def create_distance_frame(source,target):
    distances = [[0]*(len(target)+1) for _ in range(len(source)+1)]

    for i in range(1,len(target)+1):
        distances[0][i] = i
    for i in range(1,len(source)+1):
        distances[i][0] = i

def cal_distance(source,target):
    distances = create_distance_frame(source,target)
    del_cost = 0 
    ins_cost = 0 
    sub_cost = 0
    
    for i in range(1,len(source)+1):
        for j in range(1,len(target)+1):
            if source[i-1] == target[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else: 
                del_cost = distances[i-1][j] + 1
                ins_cost = distances[i][j-1] + 1
                sub_cost = distances[i-1][j-1] + 1
                if (del_cost <= ins_cost) and (del_cost <= sub_cost):
                    distances[i][j] = del_cost 
                elif (ins_cost <= del_cost) and (ins_cost <= sub_cost):
                    distances[i][j] = ins_cost
                else:
                    distances[i][j] = sub_cost 
    distance = distances[-1][-1] 
    return distance

text1 = "halo"
text2 = "hello"
distance = cal_distance(text1,text2)
print(distance)