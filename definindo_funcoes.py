"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

Obs.: Se você escrever uma função que a realiza várias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada;

Já utilizamos várias funções desde que iniciamos este curso:
- print(), len(), max(), min(), count() e etc;
"""

# Exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando uma função integrada (Built-in) do python print()

# print(cores)

curso = 'Programação em Python: Essencial'

# print(curso)

cores.append('roxo')

# print(cores)

# curso.append('Mais dados...') Vai dar o erro: AtributeError, porque não existe esse atributo em string
# print(curso)

cores.clear()
# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself (Não repita o seu código)

# Mas então, como definir funções?

"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada:
    bloco da funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (snake case)
parametros_de_entrada -> São opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais
não.
bloco_da_funcao -> Também chamado de "Corpo da Função" ou "Implementação", é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

Obs.: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao python que estamos 
definindo uma função. Também abrimos o bloco código com o já conhecido o dois pontos ':' que é utilizado em python
para definir blocos.
"""


# Definindo a primeira função

# Definição
def diz_oi():
    print('oi')


"""
OBS.:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que, nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que que está função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÂO:
Nunca esqueça de utilizar o parenteses ao executar uma função.

Exemplos:
# Errado
diz_oi
# Errado
diz_oi ()
# Certo
diz_oi()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra vocês')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# for n in range(5):
#    cantar_parabens()

# Em Python podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.

canta = cantar_parabens

canta()
