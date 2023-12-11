import string

# initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                  'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                  'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23','q24']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# space before input string
transition_table['q0', ' '] = 'q0'

# update the transition table for the following token : if
transition_table['q0', 'i'] = 'q1'
transition_table['q1', 'f'] = 'q2'
transition_table['q2', '#'] = 'accept'
transition_table['q2', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : else
transition_table['q0', 'e'] = 'q3'
transition_table['q3', 'l'] = 'q4'
transition_table['q4', 's'] = 'q5'
transition_table['q5', 'e'] = 'q6'
transition_table['q6', '#'] = 'accept'
transition_table['q6', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : true
transition_table['q0', 't'] = 'q7'
transition_table['q7', 'r'] = 'q8'
transition_table['q8', 'u'] = 'q9'
transition_table['q9', 'e'] = 'q10'
transition_table['q10', '#'] = 'accept'
transition_table['q10', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : false
transition_table['q0', 'f'] = 'q11'
transition_table['q11', 'a'] = 'q12'
transition_table['q12', 'l'] = 'q13'
transition_table['q13', 's'] = 'q14'
transition_table['q14', 'e'] = 'q15'
transition_table['q15', '#'] = 'accept'
transition_table['q15', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : variabel X
transition_table['q0', 'x'] = 'q16'
transition_table['q16', '#'] = 'accept'
transition_table['q16', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : variabel Y
transition_table['q0', 'x'] = 'q17'
transition_table['q17', '#'] = 'accept'
transition_table['q17', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : [ : ] Colon Symbol
transition_table['q0', ':'] = 'q18'
transition_table['q18', '#'] = 'accept'
transition_table['q18', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : [ : ] Colon Symbol
transition_table['q0', '>'] = 'q19'
transition_table['q19', '='] = 'q20'
transition_table['q20', '#'] = 'accept'
transition_table['q20', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : [ : ] Colon Symbol
transition_table['q0', '<'] = 'q21'
transition_table['q21', '='] = 'q22'
transition_table['q22', '#'] = 'accept'
transition_table['q22', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'

# update the transition table for the following token : [ : ] Colon Symbol
transition_table['q0', '='] = 'q23'
transition_table['q23', '#'] = 'accept'
transition_table['q23', ' '] = 'q24'
transition_table['q24', '#'] = 'accept'


# transition for new token
transition_table['q24', ' '] = 'q22'
transition_table['q24', 'i'] = 'q1'
transition_table['q24', 'e'] = 'q3'
transition_table['q24', 't'] = 'q7'
transition_table['q24', 'f'] = 'q11'
transition_table['q24', 'x'] = 'q16'
transition_table['q24', 'y'] = 'q17'
transition_table['q24', ':'] = 'q18'
transition_table['q24', '>'] = 'q19'
transition_table['q24', '<'] = 'q21'
transition_table['q24', '='] = 'q23'

# Input Kalimat
print('\n  TUGAS BESAR TEORI BAHASA DAN AUTOMATA | KELOMPOK CAKOREX | IF-45-12')
print(' ')


print('==========================================================================')
print('||           Welcome, Please do a conditional if-else in python         ||')
print('||               Here are the string that have been studied             ||')
print('||======================================================================||')
print('|| Input     : <if> <kondisi> : <aksi> else <aksi>                      ||')
print('|| Var       : x, y                                                     ||')
print('|| Operator  : >= | <=                                                  ||')
print('==========================================================================')
kalimat = input("INPUT TOKEN :")
input_string = kalimat.lower()+'#'

# lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    # print('current token :',current_token,', valid')
    if state == 'q24':
        print('CURRENT TOKEN :',current_token,'     [ VALID ]')
        current_token = ''
    if state == 'error':
        print('CURRENT TOKEN :',current_token,'       [ INVALID ]')
        print('GIVEN TOKEN ERROR')
        break
    idx_char = idx_char + 1

if state == 'accept':
    print('CURRENT TOKEN :',current_token.replace("#", ""),'    [ VALID ]')
    print("==========================")
    print('ALL TOKEN     :', kalimat, ' [ VALID ] ')