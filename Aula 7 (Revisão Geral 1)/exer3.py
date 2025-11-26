# Você tem uma lista de produtos e seus preços produtos = [('banana', 2.5), ('maçã', 4.0), ('laranja', 3.0)].
#  Use uma dictionary comprehension para criar um dicionário a partir dessa lista de tuplas, onde o nome do produto é a chave e o preço é o valor. 
# Em seguida, use um laço for com o método .items() para imprimir cada par chave-valor no formato: '
# O preço da [chave] é R$ [valor]'.

preços_produtos = [('banana', 2.5), ('maçã', 4.0), ('laranja', 3.0)]
preço = { fruta : preço for fruta, preço in  preços_produtos}
print({preço})
