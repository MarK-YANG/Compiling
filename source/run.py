#
#----------------------------------
# @author: MarK
# @Date: 2015-01-11
#----------------------------------

import sys

tokens = (
            'H1','H2','H3','H4','H5','H6','CR','TEXT','BOLD','HIGHLIGHT'
        )

# Tokens
t_H1 = r'\# '
t_H2 = r'\#\# ' 
t_H3 = r'\#\#\# '
t_H4 = r'\#\#\#\# '
t_H5 = r'\#\#\#\#\# '
t_H6 = r'\#\#\#\#\#\# '
t_BOLD = r'\*\* '
t_HIGHLIGHT = r'\`'

def t_TEXT(t):
    r'[_a-zA-Z0-9]+'
    t.value = str(t.value)
    return t

t_ignore = "\t"

def t_CR(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer

import ply.lex as lex
lex.lex()

# -----------------------------------------
# Definitions of parsing rules by yacc
# -----------------------------------------

precedence = (
        )
name = {}

def p_body(p):
    '''body : statement'''
    print '<body>' + p[1] + '</body>'


def p_state(p):
    '''statement : expression
            | statement CR expression'''
    if(len(p)==2):
        p[0] = p[1]
    elif (len(p) == 4):
        p[0] = str(p[1]) + str(p[3])


def p_exp_cr(p):
    '''expression : H1 factor
                | H2 factor
                | H3 factor
                | H4 factor
                | H5 factor
                | H6 factor
                | factor'''
    if p[1] == '#':
        p[0] = '<h1>' + str(p[2]) + '</h1>'
    elif p[1] == '##':
        p[0] = '<h2>' + str(p[2]) + '</h2>'
    elif p[1] == '##':
        p[0] = '<h2>' + str(p[2]) + '</h2>'
    elif p[1] == '###':
        p[0] = '<h3>' + str(p[2]) + '</h3>'
    elif p[1] == '####':
        p[0] = '<h4>' + str(p[2]) + '</h4>'
    elif p[1] == '#####':
        p[0] = '<h5>' + str(p[2]) + '</h5>'
    elif p[1] == '######':
        p[0] = '<h6>' + str(p[2]) + '</h6>'
    else:
        p[0] = p[1]

def p_factor_text(p):
    '''factor : TEXT
            | BOLDTEXT
            | HIGHLIGHTTEXT'''
  
    p[0] = p[1]
    
def p_bold_text(p):
    "BOLDTEXT : BOLD TEXT BOLD"
    p[0] = '<B>' + str(p[2]) + '</B>'
def p_highLight_text(p):
    "HIGHLIGHTTEXT : HIGHLIGHT TEXT HIGHLIGHT"
    p[0] = '<u>' + str(p[2]) + '<u>'

def p_error(p):
    if p:
        print("error at '%s' line '%d'" % (p.value, p.lineno))
    else:
        print("error at EOF")


import ply.yacc as yacc
yacc.yacc()

if __name__ == '__main__':
    filename = 'test.md'
    yacc.parse(open(filename).read())




    

