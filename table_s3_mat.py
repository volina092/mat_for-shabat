def operation(line_01, line_02): # однократна€ операци€ дл€ двух конкретных эл-тов
    act = ''
    for i in range(3):
        act += s3[line_01][int(s3[line_02][i]) - 1]
    #print(act) где act Ч результат операции дл€ двух конкретных эл-тов
    return ctrl_s3[act]

def table(): # "печать" таблицы с результатами операций дл€ всех пар эл-тов
    x_row, y_row = sorted(s3.keys()), sorted(s3.keys())
    print('', *x_row, sep='\t')
    for y in y_row:
        line = y +'\t'
        for x in x_row:
            line += operation(y, x) + '\t'
        print(line)
    return None

s3 = {'1': '123',
      'c': '132',
      'd': '213',
      'a': '231',
      'b': '312',
      'e': '321'} # "алфавит"
ctrl_s3 = {} # "обратный алфавит": от значени€ к символу
for i in s3.keys(): ctrl_s3[s3[i]] = i 

table()

#print(operation('a', 'a'))
