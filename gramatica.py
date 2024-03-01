gramatica = {
    ('<REPETITIVA>', 'do'): ['do', '<CUERPO>', '<MIENTRAS>'],
    ('<CUERPO>', "{}"): ["{}"],
    ('<MIENTRAS>', 'mientras'): ['mientras', '<CONDICIONAL>'],
    ('<CONDICIONAL>', '('): ['(', '<EXPRESION>', ')'],
    ('<EXPRESION>', 'letra'): ['<VALOR>', '<OPERADOR>', '<V>'],
    ('<VALOR>', 'letra'): ['<LETRA>', '<RESTO>'],
    ('<LETRA>', 'letra'): ['letra'],
    ('<RESTO>', 'letra'): ['<LETRA>', '<RESTO>'],
    ('<RESTO>', '=='): ['e'],
    ('<RESTO>', '!='): ['e'],
    ('<V>', 'true'): ['true'],
    ('<V>', 'false'): ['false'],
    ('<OPERADOR>', '=='): ['=='],
    ('<OPERADOR>', '!='): ['!=']
}
