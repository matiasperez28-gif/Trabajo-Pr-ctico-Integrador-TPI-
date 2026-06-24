def solicitar_entero_valido(mensaje):
    """
    validar que el usuario ingrese un número entero 
    positivo y que no deje el campo vacío o ponga letras.
    """
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("Error: El campo no puede estar vacío.")
            continue
        try:
            numero = int(entrada)
            if numero < 0:
                print("Error: El número debe ser mayor o igual a cero.")
                continue
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido (sin letras ni símbolos).")