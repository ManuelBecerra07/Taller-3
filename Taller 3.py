import re

def analizar_codigo(codigo):
    palabras_clave = {"int", "float", "string", "if", "while", "return", "void"}
    operadores = {"+", "-", "*", "/", "=", ">", "<", "=="}
    delimitadores = {";", "{", "}", "(", ")"}
    simbolos = []
    tabla_simbolos = {}
    lineas = codigo.split("\n")
    
    for num_linea, linea in enumerate(lineas, start=1):
        tokens = re.findall(r'\w+|[=+\-*/<>;{}()]|"[^"]*"', linea)
        
        for token in tokens:
            if token in palabras_clave:
                simbolos.append(("Keyword", token, num_linea))
            elif token in operadores:
                simbolos.append(("Operator", token, num_linea))
            elif token in delimitadores:
                simbolos.append(("Delimiter", token, num_linea))
            elif re.fullmatch(r'\d+(\.\d+)?', token):
                simbolos.append(("Number", token, num_linea))
            elif re.fullmatch(r'"[^"]*"', token):
                simbolos.append(("String", token, num_linea))
            else:
                simbolos.append(("Identifier", token, num_linea))
                if num_linea not in tabla_simbolos:
                    tabla_simbolos[token] = {"Tipo": None, "Tipo de Token": "Variable", "Línea": num_linea}
                if len(simbolos) > 1 and simbolos[-2][1] in {"int", "float", "string", "void"}:
                    tabla_simbolos[token]["Tipo"] = simbolos[-2][1]
                    if simbolos[-2][1] == "void":
                        tabla_simbolos[token]["Tipo de Token"] = "Function"
    
    return simbolos, tabla_simbolos

def imprimir_resultados(simbolos, tabla_simbolos):
    print("Tokens detectados:")
    print("Tipo\tValor\tLínea")
    for tipo, valor, linea in simbolos:
        print(f"{tipo}\t{valor}\t{linea}")
    
    print("\nTabla de Símbolos:")
    print("Nombre\tTipo\tTipo de Token\tLínea")
    for nombre, info in tabla_simbolos.items():
        print(f"{nombre}\t{info['Tipo']}\t{info['Tipo de Token']}\t{info['Línea']}")

# Código de prueba
ejemplo_codigo = """
int x = 10;
float y = 5.5;
string mensaje = "Hola";
if (x > y) {
    x = x + 1;
}
void imprimir() {
    return;
}
"""

simbolos, tabla_simbolos = analizar_codigo(ejemplo_codigo)
imprimir_resultados(simbolos, tabla_simbolos)
