from mathlang.interpreter import ejecutar_codigo

if __name__ == "__main__":
    with open("examples/ejemplo1.mlang", "r") as archivo:
        codigo = archivo.read()
    ejecutar_codigo(codigo)
