import ply.lex as lex
import ply.yacc as yacc
from graphviz import Digraph

# --------------------
# 1. Léxico
# --------------------
tokens = (
    'ID', 'NUM',
    'PLUS', 'MINUS',
    'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'EQUALS',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS  = r'='
t_ignore  = ' \t'

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# --------------------
# 2. Sintaxis
# --------------------
class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children else []

def p_S_asignacion(p):
    'S : ID EQUALS E'
    p[0] = Node('S', [Node('id', [Node(p[1])]), Node('='), p[3]])

def p_S_expresion(p):
    'S : E'
    p[0] = Node('S', [p[1]])

def p_E_expr(p):
    '''E : E PLUS T
         | E MINUS T'''
    p[0] = Node('E', [p[1], Node(p[2]), p[3]])

def p_E_to_T(p):
    'E : T'
    p[0] = Node('E', [p[1]])

def p_T_expr(p):
    '''T : T TIMES F
         | T DIVIDE F'''
    p[0] = Node('T', [p[1], Node(p[2]), p[3]])

def p_T_to_F(p):
    'T : F'
    p[0] = Node('T', [p[1]])

def p_F_group(p):
    'F : LPAREN E RPAREN'
    p[0] = Node('F', [Node('('), p[2], Node(')')])

def p_F_id(p):
    'F : ID'
    p[0] = Node('F', [Node('id', [Node(p[1])])])

def p_F_num(p):
    'F : NUM'
    p[0] = Node('F', [Node('num', [Node(p[1])])])

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()

# ------------------------
# 3. Visualización
# ------------------------
def draw_tree(node, dot=None, parent=None, count=[0]):
    if dot is None:
        dot = Digraph()
        dot.attr('node', shape='circle')

    node_id = str(count[0])
    count[0] += 1

    dot.node(node_id, node.label)

    if parent:
        dot.edge(parent, node_id)

    for child in node.children:
        draw_tree(child, dot, node_id, count)

    return dot

# ------------------------
# 4. Ejecución
# ------------------------

if __name__ == "__main__":
    entrada = input("Ingresa una expresión Matematica:\n> ").strip()
    
    if not entrada:
        print("No ingresaste ninguna expresión.")
    else:
        arbol = parser.parse(entrada)
        if arbol:
            print("Árbol generado con éxito. Dibujando...")
            graph = draw_tree(arbol)
            filename = graph.render("arbol_gramatica_profesor", format='png', view=True)
            print(f"Imagen generada: {filename}")
        else:
            print("No se pudo generar el árbol. Verifica la expresión.")