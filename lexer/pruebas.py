# Pruebas del lexer de ColombiaScript (puntos 4 a 6.1 y tareas 8 a 16).
#
#     python pruebas.py
#
# Lo ESPERADO se calculó a mano ANTES de ejecutar (columna = posición del primer
# carácter de la pieza, contando desde 1 en cada línea). Después se compara con la
# salida real del lexer.

from lexer import tokenizar
from tokens import Token, ErrorLexico

resultados = []


def toks(*tuplas):
    # Atajo para escribir lo esperado: ("TIPO", "Pille", 1, 1) -> Token(...)
    return [Token(*t) for t in tuplas]


def probar(punto, nombre, entrada, esperado):
    # esperado es una lista de Token, o un texto si se espera un error léxico
    try:
        real = tokenizar(entrada)
    except ErrorLexico as e:
        real = str(e)
    coincide = (real == esperado)
    resultados.append(coincide)
    if not coincide:
        print(f"[{punto}] {nombre}")
        print("   entrada :", repr(entrada))
        print("   esperado:", esperado)
        print("   obtenido:", real)
        print("   resultado: NO COINCIDE")
        print()


# ---------------- Puntos 4, 5, 6 y 6.1 (ahora con Token y EOF) ----------------

probar("4", "Pille es un TIPO y edad un IDENTIFICADOR",
       "Pille edad",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7), ("EOF", "", 1, 11)))
probar("4", "Pillesito NO se parte en Pille + sito",
       "Pillesito",
       toks(("IDENTIFICADOR", "Pillesito", 1, 1), ("EOF", "", 1, 10)))
probar("4", "pille en minúscula no es el tipo (distingue mayúsculas)",
       "pille edad",
       toks(("IDENTIFICADOR", "pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7), ("EOF", "", 1, 11)))

probar("5", "declaración completa con espacios",
       "Pille edad := 18",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7),
            ("ASIGNACION", ":=", 1, 12), ("NUMERO", "18", 1, 15), ("EOF", "", 1, 17)))
probar("5", "declaración sin espacios alrededor de :=",
       "Pille edad:=18",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7),
            ("ASIGNACION", ":=", 1, 11), ("NUMERO", "18", 1, 13), ("EOF", "", 1, 15)))
probar("5", ">= se lee completo (el símbolo más largo primero)",
       "Si edad >= 18",
       toks(("RESERVADA", "Si", 1, 1), ("IDENTIFICADOR", "edad", 1, 4),
            ("RELACIONAL", ">=", 1, 9), ("NUMERO", "18", 1, 12), ("EOF", "", 1, 14)))
probar("5", "asignación estilo Java (=) produce error",
       "Pille edad = 18",
       "Error léxico en línea 1, columna 12: la asignación se escribe ':=' (el '=' solo sirve para comparar)")
probar("5", "fin de instrucción estilo Java (;) produce error",
       "Pille edad := 18;",
       "Error léxico en línea 1, columna 17: carácter ';' no reconocido")
probar("5", ": suelto produce error",
       "Pille edad : 18",
       "Error léxico en línea 1, columna 12: se esperaba '=' después de ':' (la asignación se escribe :=)")

probar("6", "comentario al final no cambia los tokens",
       "Pille edad := 18 // mayor de edad",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7),
            ("ASIGNACION", ":=", 1, 12), ("NUMERO", "18", 1, 15), ("EOF", "", 1, 34)))
probar("6", "la línea siguiente conserva su número de línea",
       "Pille edad := 18 // mayor de edad\nPille hora := 23",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "edad", 1, 7),
            ("ASIGNACION", ":=", 1, 12), ("NUMERO", "18", 1, 15),
            ("TIPO", "Pille", 2, 1), ("IDENTIFICADOR", "hora", 2, 7),
            ("ASIGNACION", ":=", 2, 12), ("NUMERO", "23", 2, 15), ("EOF", "", 2, 17)))
probar("6", "un comentario con símbolos raros se ignora completo",
       "// $ @ # ; 3.4.5",
       toks(("EOF", "", 1, 17)))

probar("6.1", "@ en la línea 1",
       "Pille x := 5 @",
       "Error léxico en línea 1, columna 14: carácter '@' no reconocido")
probar("6.1", "el mismo error en la línea 2 reporta línea 2",
       "Pille x := 5\nPille y := @",
       "Error léxico en línea 2, columna 12: carácter '@' no reconocido")
probar("6.1", "un comentario antes no descuadra la línea",
       "// nota\nPille x := $",
       "Error léxico en línea 2, columna 12: carácter '$' no reconocido")
probar("6.1", "la columna cuenta los espacios del comienzo",
       "  Pille x := #",
       "Error léxico en línea 1, columna 14: carácter '#' no reconocido")
probar("6.1", "cadena sin cerrar",
       'Si x = 1 Eche mostrar "hola',
       "Error léxico en línea 1, columna 23: cadena sin cerrar, falta la comilla final")
probar("6.1", "signo - separado del número",
       "Pille frio := - 5",
       "Error léxico en línea 1, columna 15: el signo '-' debe ir pegado a un número (ej. -5)")

# ---------------- Tarea 8: delimitadores ----------------

probar("8", "paréntesis y coma con columnas correctas",
       "(a, 2)",
       toks(("SIMBOLO", "(", 1, 1), ("IDENTIFICADOR", "a", 1, 2), ("SIMBOLO", ",", 1, 3),
            ("NUMERO", "2", 1, 5), ("SIMBOLO", ")", 1, 6), ("EOF", "", 1, 7)))
probar("8", "llaves",
       "{a}",
       toks(("SIMBOLO", "{", 1, 1), ("IDENTIFICADOR", "a", 1, 2),
            ("SIMBOLO", "}", 1, 3), ("EOF", "", 1, 4)))
probar("8", "punto entre dos nombres es SIMBOLO",
       "System.out",
       toks(("IDENTIFICADOR", "System", 1, 1), ("SIMBOLO", ".", 1, 7),
            ("IDENTIFICADOR", "out", 1, 8), ("EOF", "", 1, 11)))
probar("8", "punto dentro de un número sigue siendo parte del número",
       "Pille t := 3.14",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "t", 1, 7), ("ASIGNACION", ":=", 1, 9),
            ("NUMERO", "3.14", 1, 12), ("EOF", "", 1, 16)))
probar("8", "decimal negativo",
       "Pille t := -0.5",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "t", 1, 7), ("ASIGNACION", ":=", 1, 9),
            ("NUMERO", "-0.5", 1, 12), ("EOF", "", 1, 16)))
probar("8", "punto sin dígito detrás no es decimal",
       "3.",
       toks(("NUMERO", "3", 1, 1), ("SIMBOLO", ".", 1, 2), ("EOF", "", 1, 3)))

# ---------------- Tarea 9: operadores de dos caracteres ----------------

probar("9", "x == 5 da 3 tokens (más EOF)",
       "x == 5",
       toks(("IDENTIFICADOR", "x", 1, 1), ("RELACIONAL", "==", 1, 3),
            ("NUMERO", "5", 1, 6), ("EOF", "", 1, 7)))
probar("9", "x = = 5 da 4 tokens (más EOF)",
       "x = = 5",
       toks(("IDENTIFICADOR", "x", 1, 1), ("RELACIONAL", "=", 1, 3),
            ("RELACIONAL", "=", 1, 5), ("NUMERO", "5", 1, 7), ("EOF", "", 1, 8)))
probar("9", "!= <= >= < >",
       "a != b <= c >= d < e > f",
       toks(("IDENTIFICADOR", "a", 1, 1), ("RELACIONAL", "!=", 1, 3), ("IDENTIFICADOR", "b", 1, 6),
            ("RELACIONAL", "<=", 1, 8), ("IDENTIFICADOR", "c", 1, 11), ("RELACIONAL", ">=", 1, 13),
            ("IDENTIFICADOR", "d", 1, 16), ("RELACIONAL", "<", 1, 18), ("IDENTIFICADOR", "e", 1, 20),
            ("RELACIONAL", ">", 1, 22), ("IDENTIFICADOR", "f", 1, 24), ("EOF", "", 1, 25)))
probar("9", "! solo (sin =) es error léxico",
       "x ! 5",
       "Error léxico en línea 1, columna 3: carácter '!' no reconocido")

# ---------------- Tarea 10: reservadas de control y booleanos ----------------

probar("10", "Si es RESERVADA, Sillo y Tin_x son IDENTIFICADOR",
       "Si Sillo Tin_x",
       toks(("RESERVADA", "Si", 1, 1), ("IDENTIFICADOR", "Sillo", 1, 4),
            ("IDENTIFICADOR", "Tin_x", 1, 10), ("EOF", "", 1, 15)))
probar("10", "Eche, Tin, Tan y mostrar son RESERVADA; Melo y Paila BOOLEANO",
       "Eche Tin Tan mostrar Melo Paila",
       toks(("RESERVADA", "Eche", 1, 1), ("RESERVADA", "Tin", 1, 6), ("RESERVADA", "Tan", 1, 10),
            ("RESERVADA", "mostrar", 1, 14), ("BOOLEANO", "Melo", 1, 22),
            ("BOOLEANO", "Paila", 1, 27), ("EOF", "", 1, 32)))
probar("10", "Melosa no es el booleano Melo",
       "Melosa",
       toks(("IDENTIFICADOR", "Melosa", 1, 1), ("EOF", "", 1, 7)))

# ---------------- Tarea 11: comentarios de bloque ----------------

probar("11", "comentario de 3 líneas deja la segunda declaración en la línea 4",
       "Pille a := 1 /* uno\ndos\ntres */\nPille b := 2",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "a", 1, 7), ("ASIGNACION", ":=", 1, 9),
            ("NUMERO", "1", 1, 12),
            ("TIPO", "Pille", 4, 1), ("IDENTIFICADOR", "b", 4, 7), ("ASIGNACION", ":=", 4, 9),
            ("NUMERO", "2", 4, 12), ("EOF", "", 4, 13)))
probar("11", "la columna se reinicia después del cierre en la misma línea",
       "/* a\nb */ x",
       toks(("IDENTIFICADOR", "x", 2, 6), ("EOF", "", 2, 7)))
probar("11", "comentario de bloque en una sola línea",
       "a /* x */ b",
       toks(("IDENTIFICADOR", "a", 1, 1), ("IDENTIFICADOR", "b", 1, 11), ("EOF", "", 1, 12)))
probar("11", "comentario sin cerrar: error en la línea donde empezó",
       "Pille a := 1 /* sin cerrar",
       "Error léxico en línea 1, columna 14: comentario sin cerrar")
probar("11", "comentario sin cerrar que empezó en la línea 2",
       "Pille a := 1\n  /* sin\ncerrar",
       "Error léxico en línea 2, columna 3: comentario sin cerrar")
probar("11", "/*/ no cuenta como comentario cerrado",
       "/*/",
       "Error léxico en línea 1, columna 1: comentario sin cerrar")

# ---------------- Tarea 12: EOF ----------------

probar("12", "una declaración termina con EOF",
       "Pille x := 5",
       toks(("TIPO", "Pille", 1, 1), ("IDENTIFICADOR", "x", 1, 7), ("ASIGNACION", ":=", 1, 9),
            ("NUMERO", "5", 1, 12), ("EOF", "", 1, 13)))
probar("12", "texto vacío produce solo EOF",
       "",
       toks(("EOF", "", 1, 1)))
probar("12", "texto que termina en salto de línea: EOF al comienzo de la línea siguiente",
       "x\n",
       toks(("IDENTIFICADOR", "x", 1, 1), ("EOF", "", 2, 1)))

# ---------------- Tarea 13: clase Token ----------------

t = Token("NUMERO", "5", 1, 9)
resultados.append(t.tipo == "NUMERO" and t.texto == "5" and t.linea == 1 and t.columna == 9)
resultados.append(str(t) == "NUMERO('5') en 1:9")
resultados.append([str(x) for x in tokenizar("x := 5")] ==
                  ["IDENTIFICADOR('x') en 1:1", "ASIGNACION(':=') en 1:3",
                   "NUMERO('5') en 1:6", "EOF('') en 1:7"])

# ---------------- Tarea 14: ErrorLexico ----------------

try:
    tokenizar("Pille a := 1\nPille b := 2 @")
    resultados.append(False)
except ErrorLexico as e:
    resultados.append(e.linea == 2 and e.columna == 14
                      and str(e) == "Error léxico en línea 2, columna 14: carácter '@' no reconocido")

# ---------------- Tarea 16: ejemplo.txt ----------------

with open("ejemplo.txt", encoding="utf-8") as f:
    ejemplo = f.read()
tokens_ejemplo = tokenizar(ejemplo)
resultados.append(len(ejemplo.splitlines()) >= 10 and tokens_ejemplo[-1].tipo == "EOF")
# Calculado a mano: la línea 1 es comentario; líneas 2 y 3 son declaraciones.
esperado_ejemplo = toks(
    ("TIPO", "Pille", 2, 1), ("IDENTIFICADOR", "edad", 2, 7), ("ASIGNACION", ":=", 2, 12), ("NUMERO", "20", 2, 15),
    ("TIPO", "Pille", 3, 1), ("IDENTIFICADOR", "temperatura", 3, 7), ("ASIGNACION", ":=", 3, 19),
    ("NUMERO", "31.5", 3, 22))
resultados.append(tokens_ejemplo[:len(esperado_ejemplo)] == esperado_ejemplo)

print(f"Resumen: {sum(resultados)} de {len(resultados)} pruebas coinciden con lo esperado a mano.")
