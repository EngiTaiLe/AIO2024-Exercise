def compute_evaluation_metrics(tp,fp,fn):
    if not isinstance(tp,int):
        print('tp must be int')
        return
    elif not isinstance(fp,int):
        print('fp must be int')
        return
    elif not isinstance(fn,int):
        print('fn must be int')
        return
    if (tp < 1) or (fp < 1) or (fn < 1):
        print('tp and fp and fn must be greater than zero')
        return
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*(precision*recall)/(precision+recall)
    print(f'Precision, Recall and F1-Score is {precision}, {recall}, and {f1}')