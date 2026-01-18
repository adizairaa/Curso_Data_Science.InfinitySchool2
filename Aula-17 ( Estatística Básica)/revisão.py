# Crie um código em Python que receba a string texto_sujo e realize as seguintes ações: Importe o módulo re. Use o método re.sub() para aplicar o padrão que busca e substitui todos os caracteres que não são letras (a-z, A-Z), números (0-9) ou espaços em branco (\s) por uma string vazia (""). Imprima a string resultante após a limpeza.

import re
texto_sujo = " Olá TuDo BeNm 123@#$   "
texto_limpo =  re.sub(r'[^a-zA-Z0-9\s]', '', texto_sujo)

print (f"{texto_limpo}")