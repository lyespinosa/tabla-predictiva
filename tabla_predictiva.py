from gramatica import gramatica


def verificar_tabla(entrada):
    symbols = {key[1] for key in gramatica.keys()}
    pila = ['$', '<REPETITIVA>']
    registro = [' '.join(pila)]
    entrada = entrada.strip()
    simbolos_procesados = []
    entrada_reemplazada = entrada.replace('{}', ' {} ').replace(
        '(', ' ( ').replace(')', ' ) ').replace('==', ' == ').replace('!=', ' != ')
    elementos = entrada_reemplazada.split()

    for elemento in elementos:
        if elemento in ['do', 'mientras', '{}', '(', ')', '==', '!=', 'true', 'false']:
            simbolos_procesados.append(elemento)
        elif elemento == '(' or elemento == ')':
            simbolos_procesados.append(elemento)
        else:
            for char in elemento:
                simbolos_procesados.append('letra')
    entry_symbols = simbolos_procesados + ['$']

    while pila and entry_symbols:
        tope_pila = pila[-1]
        current_symbol = entry_symbols[0]

        if tope_pila == current_symbol:
            pila.pop()
            entry_symbols.pop(0)
        elif (tope_pila, current_symbol) in gramatica:
            pila.pop()
            elementos_produccion = gramatica[(
                tope_pila, current_symbol)]
            if elementos_produccion != ['e']:
                pila.extend(reversed(elementos_produccion))
        else:
            return '\n'.join(registro) + f'\nERROR en: "{current_symbol}"'
        registro.append(' '.join(pila) if pila else 'Pila vaciada \nCORRECTO')

    return '\n'.join(registro)
