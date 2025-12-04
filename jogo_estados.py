# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.
#Critério adicionados ao desafio
# Pontuação
# O jogador terá 3 tentativas para acertar a capital do estado.
# Se acertar na primeira tentativa ganha 5 pontos
# Se acertar na segunda tentativa ganha 3 pontos
import unicodedata
def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return nfkd.encode('ASCII', 'ignore').decode('UTF-8')

estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',       
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
} 

print('Seja bem-vindo ao jogo dos estados e capitais do Brasil!')

for estados, capitais in estados_capitais.items():
    tentativas = 3
    pontos = 0
    acertou = False
    
    while tentativas > 0 and not acertou:
        resposta = input(f'Qual a capital do Estado {estados}? ')
        
        if remover_acentos(resposta.strip().lower()) == remover_acentos(capitais.strip().lower()):
            if tentativas == 3:
                pontos = 5
            elif tentativas == 2:
                pontos = 3
            else:
                pontos = 1
            
            print(f'Parabéns! Você acertou e ganhou {pontos} pontos.\n')
            acertou = True
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f'Resposta incorreta. Você tem mais {tentativas} tentativas.\n')
            else:
                print(f'Você esgotou suas tentativas. A capital de {estados} é {capitais}.\n')  
    else:
        continuar = input('Deseja continuar para a próxima pergunta? (s/n): ')
        if continuar.strip().lower() != 's':
            print('Obrigado por jogar o jogo dos estados e capitais do Brasil!')
            exit()
               
#finalizar o jogo apos chegar em 0 tentativas ou finalizar todas as perguntas
#print('Obrigado por jogar o jogo dos estados e capitais do Brasil!')



