import sympy as sp
import re

context = {
    'mostrar': lambda expr: print(sp.simplify(expr)),
    'derivar': lambda f, x: sp.diff(f, x),
    'integrar': lambda f, x, a=None, b=None: sp.integrate(f, (x, a, b)) if a is not None and b is not None else sp.integrate(f, x),
    'resolver': lambda eq, x: sp.solve(eq, x),
    'simbolo': lambda: sp.Symbol('x'),
}
variables = {}

def es_llamada_funcion(linea):
    return re.match(r"(\w+)\(([^)]*)\)", linea)

def evaluar_funcion(nombre, valor):
    if nombre in context and isinstance(context[nombre], sp.Lambda):
        arg = context[nombre].args[0]
        return context[nombre].expr.subs(arg, valor)
    return None

def procesar_linea(linea):
    linea = linea.strip()
    if linea.startswith("#") or not linea:
        return

    if re.match(r"(\w+) *= *simbolo\(\)", linea):
        nombre = linea.split("=")[0].strip()
        context[nombre] = sp.Symbol(nombre)
        return

    if linea.startswith("funcion"):
        match = re.match(r"funcion (\w+)\((\w+)\) *= *(.*)", linea)
        if match:
            nombre, var, expr = match.groups()
            x = sp.Symbol(var)
            f = sp.sympify(expr.replace("^", "**"), locals=context)
            context[nombre] = sp.Lambda(x, f)
        return

    if "=" in linea:
        nombre, expr = linea.split("=", 1)
        nombre = nombre.strip()
        expr = expr.strip()

        if expr.startswith("derivar"):
            match = re.match(r"derivar\((\w+),\s*(\w+)\)", expr)
            if match:
                f, var = match.groups()
                x = context.get(var, sp.Symbol(var))
                resultado = context["derivar"](context[f], x)
                context[nombre] = resultado

        elif expr.startswith("integrar"):
            match = re.match(r"integrar\((\w+),\s*(\w+)(?:,\s*([\d.\w]+),\s*([\d.\w]+))?\)", expr)
            if match:
                f, var, a, b = match.groups()
                x = context.get(var, sp.Symbol(var))
                a = context.get(a, float(a)) if a else None
                b = context.get(b, float(b)) if b else None
                resultado = context["integrar"](context[f], x, a, b)
                context[nombre] = resultado

        elif expr.startswith("resolver"):
            match = re.match(r"resolver\((.+)\s*=\s*0,\s*(\w+)\)", expr)
            if match:
                eq_str, var = match.groups()
                eq = sp.sympify(eq_str.replace("^", "**"), locals=context)
                x = context.get(var, sp.Symbol(var))
                resultado = context["resolver"](eq, x)
                context[nombre] = resultado

        elif es_llamada_funcion(expr):
            match = es_llamada_funcion(expr)
            fname, arg = match.groups()
            arg_val = context.get(arg, sp.sympify(arg))
            resultado = evaluar_funcion(fname, arg_val)
            context[nombre] = resultado

        else:
            context[nombre] = sp.sympify(expr.replace("^", "**"), locals=context)
        return

    if linea.startswith("mostrar"):
        match = re.match(r"mostrar\((.+)\)", linea)
        if match:
            expr = match.group(1).strip()
            mostrar = context.get("mostrar")
            if expr in context:
                mostrar(context[expr])
            else:
                mostrar(sp.sympify(expr.replace("^", "**"), locals=context))

def ejecutar_codigo(codigo):
    for linea in codigo.strip().splitlines():
        procesar_linea(linea)
