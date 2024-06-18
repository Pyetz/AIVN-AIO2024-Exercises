def calc_f1_score(tp, fp, fn):
    if type(tp) is not int:
        return 'tp must be int'
    if type(fp) is not int:
        return 'fp must be int'
    if type(fn) is not int:
        return 'fn must be int'
    if tp <= 0 or fp <= 0 or fn <= 0:
        return 'tp and fp and fn must be greater than zero'

    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f'precision is {precision}\nrecall is {recall}\nf1-score is {f1_score}'

if __name__ == '__main__':
    print(calc_f1_score(tp=2, fp=3, fn=4))
    print(calc_f1_score(tp='a', fp=3, fn=4))
    print(calc_f1_score(tp=2, fp='a', fn=4))
    print(calc_f1_score(tp=2, fp=3, fn='a'))
    print(calc_f1_score(tp=2, fp=3, fn=0))
    print(calc_f1_score(tp=2.1, fp=3, fn=0))
