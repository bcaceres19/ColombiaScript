# ColombiaScript

Lenguaje de reglas condicionales con jerga colombiana, desarrollado como proyecto
para el curso de Lenguajes Formales.

## Integrantes

- Nombre del grupo/repositorio: ColombiaScript
- Integrantes:
  - [@bcaceres19](https://github.com/bcaceres19)
  - [@DavidTorres16](https://github.com/DavidTorres16)
  - [@ItzMarlon2](https://github.com/ItzMarlon2)
  - [@sams0ft](https://github.com/sams0ft)

## 1. Dominio del sistema

ColombiaScript modela un **asistente de decisiones para la vida cotidiana**: un motor
de reglas que, a partir de datos simples del entorno de una persona (edad, saldo,
temperatura, hora del día, hambre, clima, permisos, intentos de acceso, etc.), decide
qué acción tomar. Cubre varios sub-dominios de uso diario:

- **Seguridad y acceso**: permitir o negar entrada, bloquear acceso tras varios intentos.
- **Hogar / clima**: encender ventilador, aire acondicionado o luces según temperatura,
  hora o estado de dispositivos.
- **Finanzas personales**: autorizar compras, pagar deudas ("culebras"), usar tarjeta
  según el saldo disponible.
- **Movilidad**: pedir un taxi si hay disponibilidad y dinero suficiente.
- **Bienestar**: buscar comida según el nivel de hambre, llevar chaqueta según el clima.

Todas las reglas se expresan con la misma gramática, usando jerga colombiana en
lugar de las palabras clave tradicionales (`if`, `then`, `and`, `or`, `true`, `false`).

## 2. Las 15 reglas (lenguaje natural)

1. Si la edad es mayor o igual a 18 años, se permite la entrada.
2. Si la temperatura alcanza o supera los 30°C, se enciende el ventilador.
3. Si el saldo es menor o igual a cero, se muestra el mensaje "Paila, no hay lucas".
4. Si son las 22:00 horas o más y la luz está apagada, se enciende la luz.
5. Si la temperatura supera los 28°C y el aire acondicionado está apagado, se enciende el aire.
6. Si el saldo es mayor o igual a 50000 y el pago está autorizado, se realiza la compra.
7. Si está lloviendo o hace frío, se debe llevar chaqueta.
8. Si la edad es menor a 18 años o no se tiene permiso, se niega la entrada.
9. Si hay una deuda ("culebra") mayor a cero y hay dinero extra ("liga") disponible, se paga la deuda.
10. Si se han hecho 3 o más intentos, se bloquea el acceso.
11. Si el saldo es menor a 20000 o hay una tarjeta disponible, se usa la tarjeta.
12. Si hay un taxi disponible y se cuenta con al menos 15000 de dinero, se pide el taxi.
13. Si el nivel de hambre es 8 o más, o no hay comida disponible, se busca comida.
14. Si no se tiene permiso y ya son las 21:00 horas o más, se muestra "Paila nea, el cucho dijo que no".
15. Si el proceso ha terminado, se muestra el mensaje de cierre "Nombre de Dios, nos pillamos".

La versión formal de estas mismas 15 reglas, escrita en la sintaxis de ColombiaScript,
está en [`reglas.txt`](reglas.txt).

### Cumplimiento de requisitos

- **Al menos 3 reglas con una sola condición**: reglas 1, 2, 3, 10 y 15.
- **Al menos 3 reglas con condiciones compuestas (Y/O)**: reglas 4, 5, 6, 7, 8, 9, 11, 12, 13 y 14
  (`Tin` = Y, `Tan` = O).
- **Al menos 2 reglas que combinan tipos de datos distintos** (numérico + booleano):
  reglas 4, 5, 6, 8, 11, 12, 13 y 14.

## 3. Tabla de clasificación de variables

| Variable | Tipo Java | Ejemplo |
|---|---|---|
| `edad` | `int` | `20` |
| `temperatura` | `double` | `31.5` |
| `saldo` | `double` | `45000.0` |
| `hora` | `int` | `22` |
| `luz_encendida` | `boolean` | `false` |
| `aire_encendido` | `boolean` | `false` |
| `pago_autorizado` | `boolean` | `true` |
| `esta_lloviendo` | `boolean` | `true` |
| `hace_frio` | `boolean` | `false` |
| `tiene_permiso` | `boolean` | `true` |
| `deuda` | `double` | `30000.0` |
| `liga` | `double` | `5000.0` |
| `intentos` | `int` | `3` |
| `tarjeta_disponible` | `boolean` | `true` |
| `taxi_disponible` | `boolean` | `true` |
| `dinero` | `double` | `20000.0` |
| `hambre` | `int` | `9` |
| `comida_disponible` | `boolean` | `false` |
| `permiso` | `boolean` | `false` |
| `proceso_terminado` | `boolean` | `true` |

Las acciones (`permitir_entrada`, `encender_luz`, `pagar_culebra`, `mostrar`, etc.) son
identificadores de tipo `String` que el motor de reglas resuelve a una función o
procedimiento a ejecutar.

## 4. Sintaxis formal de las reglas

```
<regla>       ::= "Si" <condicion> { <conector> <condicion> } "Eche" <accion>
<conector>    ::= "Tin" | "Tan"
<condicion>   ::= <variable> <operador> <valor>
<operador>    ::= ">" | "<" | ">=" | "<=" | "="
<variable>    ::= <identificador_minusculas>
<valor>       ::= <numero> | "Melo" | "Paila" | <cadena>
<accion>      ::= <identificador_minusculas> | "mostrar" <cadena>
<identificador_minusculas> ::= <letra_minuscula> { <letra_minuscula> | "_" | <digito> }
<numero>      ::= <digito> { <digito> } [ "." <digito> { <digito> } ]
<cadena>      ::= '"' { <caracter> } '"'
```

Donde:

- `Tin` = Y (AND), `Tan` = O (OR)
- `Melo` = verdadero, `Paila` = falso
- `Eche` = entonces / ejecuta la acción

El detalle de cada palabra reservada, su significado y su categoría gramatical está
en [`palabras_reservadas.md`](palabras_reservadas.md).

## Estructura del repositorio

```
.
├── README.md
├── reglas.txt
├── palabras_reservadas.md
└── docs/
    └── fuentes/
        ├── Actividades y entregables del proyecto.pdf
        └── Documentacion_ColombiaScript_original.docx
```
