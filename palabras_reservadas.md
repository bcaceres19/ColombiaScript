# Palabras reservadas de ColombiaScript

## Palabras clave y operadores del lenguaje

| Palabra reservada | Significado | Categoría |
|---|---|---|
| `Si` | Inicia una condición. Equivale a `if`. | Palabra clave |
| `Eche` | Indica la consecuencia de una condición: "entonces, haga esto". Equivale a `then`. | Palabra clave |
| `Tin` | Operador lógico Y. Exige que ambas condiciones se cumplan. Equivale a `AND`. | Operador lógico |
| `Tan` | Operador lógico O. Basta con que una de las condiciones se cumpla. Equivale a `OR`. | Operador lógico |
| `Melo` | Valor booleano verdadero. Indica que algo está activo, disponible o correcto. Equivale a `true`. | Literal |
| `Paila` | Valor booleano falso o estado negativo. Indica que algo no está disponible o salió mal. Equivale a `false`. | Literal |
| `mostrar` | Acción reservada para desplegar un mensaje de texto en pantalla. | Palabra clave / acción |
| `>` | Mayor que. | Operador relacional |
| `<` | Menor que. | Operador relacional |
| `>=` | Mayor o igual que. | Operador relacional |
| `<=` | Menor o igual que. | Operador relacional |
| `=` | Igual a. | Operador relacional |

## Vocabulario de jerga (no son palabras reservadas)

Estas expresiones no forman parte de la gramática del lenguaje: aparecen únicamente
dentro de literales de texto (mensajes con `mostrar "..."`) para darle sabor
colombiano al sistema. Se documentan aquí solo como glosario de contexto.

| Expresión | Significado |
|---|---|
| `Lucas` | Forma coloquial colombiana de referirse al dinero. |
| `Liga` | Dinero adicional o extra que se recibe. |
| `Culebra` | Deuda u obligación de dinero. |
| `Nea` | Forma coloquial de referirse a un amigo, compañero o persona cercana. |
| `Cucho` | Forma coloquial de referirse a una persona mayor o al papá. |
| `Nombre de Dios` | Expresión usada como despedida o bendición; acompaña el cierre de un proceso. |

## Convención de escritura

- Las palabras reservadas del lenguaje (`Si`, `Eche`, `Tin`, `Tan`, `Melo`, `Paila`, `mostrar`) se
  escriben con la primera letra en mayúscula (excepto `mostrar`, que va en minúscula por ser
  una acción).
- Las variables y las acciones se escriben en minúsculas, usando guion bajo (`snake_case`)
  para separar palabras, por ejemplo: `luz_encendida`, `pago_autorizado`, `bloquear_acceso`.
- Los literales de texto van entre comillas dobles: `"Paila, no hay lucas"`.
- Los operadores relacionales admitidos son: `>`, `<`, `>=`, `<=`, `=`.
- Toda regla sigue el formato uniforme: `Si <condición> [Tin|Tan <condición>]* Eche <acción>`.
