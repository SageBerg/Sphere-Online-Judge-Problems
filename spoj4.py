"""
Sage Berg
SPOJ: 4 Transform the Expression
2 Dec 2014
"""

class Symbol(object):

    def __init__(self, sym):
        self.sym = sym 
        self.moved = False

def polishify(string):
    sym_list = list()
    for sym in string:
        sym_list.append(Symbol(sym))
    for i in range(len(sym_list)): 
        if sym_list[i].sym in "+*-/^" and not sym_list[i].moved:
            j = i
            parens = 0
            while parens < 1 and j < len(sym_list):
                if sym_list[j].sym == "(":
                    parens -= 1
                elif sym_list[j].sym == ")":
                    parens += 1
                j += 1
            if parens == 1:
                sym_list[i].moved = True
                sym_list = sym_list[:i] + sym_list[i+1:j+1] \
                        + [sym_list[i]] + sym_list[j+1:]
    sym_list = [x for x in sym_list if x.sym != "(" and \
                                       x.sym != ")" and \
                                       x.sym != " "]
    string = ""
    for sym in sym_list:
        string += sym.sym
    print(string)

n = int(input())
for i in range(n):
    polishify(input())
