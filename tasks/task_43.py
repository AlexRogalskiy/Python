import re

def t_Sup(scanner, token): return "Sup", token[1:]
def t_Word(scanner, token):   return "Word", token
def t_Comma(scanner, token):   return "Comma", token
def t_Dot(scanner, token):   return "Dot", token
def t_Number(scanner, token):   return "Number", token
def t_Operator(scanner, token):   return "Operator", token
def t_EqualsLine(scanner, token):   return "EqualsLine", token
def t_DoubleEquals(scanner, token):   return "DoubleEquals", token
def t_EVAL(scanner, token): return "EVAL", token[:-1]+str(eval(token[:-2]))
def t_MathBegin(scanner, token): return "MathBegin", token
def t_Newline(scanner, token): return "Newline", token
def t_Space(scanner, token): return "Space", token

def scan1(text):
    scanner1 = re.Scanner([
        (r">", t_MathBegin),
        (r"[a-zA-Z]+", t_Word),
        (r"[,:;]+", t_Comma),
        (r"[\.!]+", t_Dot),
        (r"[0-9]+", t_Number),
        (r"\n==+\n", t_EqualsLine),
        (r"==", t_DoubleEquals),
        (r"\^[0-9]+", t_Sup),
        (r"[\+*-/]", t_Operator),
        (r"\n", t_Newline),
        (r"\s+", t_Space),
        ])
    parse1 = ""
    math="false"
    calc=""
    tokens, remainder = scanner1.scan(text)
    for token in tokens:
        if math=="true":
            if token[0]=="DoubleEquals":
                math="false"
                parse1+="="+str(eval(calc))
                calc=""
            elif token[0]=="Sup":
                calc+="**"+token[1]
                parse1+="<sup>"+token[1]+"</sup>"
            else:
                calc+=token[1]
                parse1+=token[1]
        
        elif token[0]=="MathBegin":
            math="true"
            parse1+=token[1]
        else:
            parse1+=token[1]
    print parse1


md="""Math in markdown
================

>3^7/9==


Then we multiply by 4 because there is 4 legs,
>3*4=="""
scan1(md)

    