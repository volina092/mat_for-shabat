def right_symbols(line):
    global add_only
    global multi_only
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    line = line.replace(' ', '')
    for letter in line:
        if not letter in ['1', '0', 'x', '\'', '=', '*', '(', ')', '+']:
            return 'error'
    if line[0] == '=' or line[-1] == '=': return 'error'
    if not line.count('=') and not line.count('*') and line.count('+'): add_only = True
    elif not line.count('=') and not line.count('+') and line.count('*'): multi_only = True
    #print(line)
    return line   

def simplier(line):
    find_streak = False
    parts = []
    for i in range(len(line)):
        if line[i] == '\'' and not find_streak:
            return 'error'
        if find_streak and (line[i] != "\'" or i == (len(line) - 1)):
            parts.append('x')
            find_streak = False
        elif line[i] == 'x':
            find_streak = True
        if line[i] == '0': parts.append('1')
        elif line[i] == '*': parts.append('+')
        elif line[i] != '\'' and line[i] != 'x': parts.append(line[i])
    if line[-1] == 'x': parts.append('x')
    new_line = ''.join(parts)
    #print(new_line)
    for i in range(len(new_line)-1):
        if new_line[i] == new_line[i+1] and new_line[i] not in ['(', ')']:
            return 'error'
        if new_line[i] == '1' and new_line[i+1] == 'x': return 'error'
        if new_line[i] == 'x' and new_line[i+1] == '1': return 'error' 
    return new_line

def brackets(line):
    if not '(' in line and not ')' in line: return line
    if line.count('(') != line.count(')'):
       # print('error brackets!!!')
        return 'error'
    for i in range(len(line)):
        if line[i] == '(': 
            if (i != 0 and line[i-1] not in ['=', '+', '(']) or line[i+1] not in ['1', 'x', '(']:
                #print('error brackets!!')
                return 'error' 
        if line[i] == ')': 
            if (line[i-1] not in ['1', ')', 'x']) or ((i != len(line) - 1) and line[i+1] not in ['+', ')', '=']):
                #print('error brackets!')
                return 'error' 
    return line

def brackets_right(line):
    only_brackets_and_equal = []
    only_brackets = ''
    for i in line:
        if i in ['(', ')']: only_brackets += i
        elif i == '=':
            only_brackets_and_equal.append(only_brackets)
            only_brackets = ''
    only_brackets_and_equal.append(only_brackets)
    for part in only_brackets_and_equal:
        for i in range(len(part)//2):
            if not part.count('()'): return 'error'
            part = part.replace('()', '', 1)
    return line
    
def equivalence(line):
    global kind_of
    if line.count('=') == 0:
        kind_of = 'term'
        return line
    
    for i in range(len(line)):
        if line[i] != '=': continue
        elif line[i-1] not in ['1', 'x', ')'] or line[i+1] not in ['1', 'x', '(']:
            return 'error'
        elif line[i] == '=':
            kind_of = 'formula'
    return line

line = ''
while line != 'end':
    line = input('Please, write the phrase you want to check.\nIf you\'d like to finish, write the word \"end\"\n')
    if line == 'end': break
    else:
        kind_of = 'out of syntax'
        add_only, multi_only = False, False
        line = right_symbols(line)
        if line != 'error': line = simplier(line)
        if line != 'error': line = brackets(line)
        if line != 'error': line = equivalence(line)
        if line != 'error': line = brackets_right(line)
        
        if line == '1': kind_of = 'constant'
        elif line == 'x': kind_of = 'variable'
        elif kind_of != 'formula' and line != 'error':
            kind_of = 'compound term'
            if add_only: kind_of += ' (sum of simple terms)'
            elif multi_only: kind_of += ' (multiplication of simple terms)'
        print('That is ' + kind_of)