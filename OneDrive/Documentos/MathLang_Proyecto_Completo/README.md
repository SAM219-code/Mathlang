# MathLang

**MathLang** es un lenguaje simbólico diseñado para resolver problemas matemáticos con una sintaxis clara y amigable inspirada en Python.

## Características

- Declaración de símbolos
- Funciones simbólicas
- Derivadas e integrales
- Evaluación y resolución de ecuaciones

## Ejemplo

```text
x = simbolo()
funcion f(x) = x^2 + 2*x + 1
df = derivar(f, x)
mostrar(df)
```

## Uso

```bash
pip install -r requirements.txt
python main.py
```

## Estructura del Lenguaje

- Variables: `a = 2`
- Funciones: `funcion f(x) = x^2`
- Derivar: `derivar(f, x)`
- Integrar: `integrar(f, x, a, b)`
- Mostrar resultados: `mostrar(expr)`
- Evaluar funciones: `f(2)`
- Resolver ecuaciones: `resolver(f(x) = 0, x)`

## Definición Formal (EBNF Simplificada)

<programa> ::= {<instruccion>}  
<instruccion> ::= <asignacion> | <funcion> | <mostrar> | <llamada>  
<asignacion> ::= <id> '=' <expresion>  
<funcion> ::= 'funcion' <id> '(' <id> ')' '=' <expresion>  
<mostrar> ::= 'mostrar(' <expresion> ')'  
<llamada> ::= <id> '(' <valor> ')'  
<expresion> ::= combinación de constantes, variables, operadores  
<valor> ::= número | identificador  
