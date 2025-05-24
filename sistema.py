import json # Biblioteca para lidar com arquivos em formato JSON
import os # Biblioteca para usar comandos do sistema operacional
from hashlib import sha256
os.system('cls')

caminho_arquivo = 'cadastros.json' # Nome do arquivo onde os cadastros são salvos
usuario_logado = None # Variável para armazenar o usuário logado

# Função que pergunta ao usuário se quer voltar aos cursos ou encerrar o programa
def funcao_voltar_curso():
    while True:
        resposta = input('Para voltar aos cursos(sim/não)\n').strip().lower()[0]
        if resposta == 's':
            return 'voltar' 
        elif resposta == 'n':
            print('Programa encerrado.')
            exit()
        else:
            print('DIGITE APENAS(sim/não)')

def funcao_voltar_sair():
    while True:
        resposta = input('Para voltar digite(sim/não)\n').strip().lower()[0]
        if resposta == 's':
            return 'voltar'
        elif resposta == 'n':
            print('Programa encerrado.')
            exit()
        else:
            print('DIGITE APENAS (sim/não)')

# Verifica se o arquivo de cadastros existe
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        try:
            cadastros = json.load(arquivo) # Carrega os dados do arquivo JSON
        except json.JSONDecodeError:
            cadastros = []
else:
    cadastros = []

# Loop principal do programa
while True:
    print('Seja bem vindo, a nossa plataforma digital de cursos!')

    print('| 1 - Introdução |')
    print('| 2 - Cadastro   |')
    print('| 3 - Cursos     |')
    print('| 4 - Login      |')

    ver = input('Para entrar digite (1, 2, 3 ou 4)\n').strip().lower()
    
    # Opção 1 - Introdução
    if ver == '1':
        print('A nossa plataforma é voltada para conteúdos de educação digital e inclusão tecnologica.')
        if funcao_voltar_sair() == 'voltar':
            continue

    if ver == '2': # Opção 2 - Cadastro
        while True:
            print('Área do cadastro')

            # Aceitação do termo LGPD
            print('''Termo de Consentimento de Uso de Dados
Ao prosseguir com o cadastro, você autoriza o uso dos dados fornecidos para fins educacionais e estatísticos dentro da plataforma. Seus dados serão armazenados com segurança, não serão compartilhados com terceiros e serão utilizados conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).''')
            while True:
                aceitar = input('Para aceitar digite sim, para negar digite não.\n').strip().lower()[0]

                if aceitar == 's':
                    print('Aceito!')
                    break
                elif aceitar == 'n':
                    print('Não aceito. É preciso aceitar os termos.')
                    exit()
                else:
                    print('Resposta incorreta! Tente novamente.')

            nome = input('Digite seu nome: \n')
            if not nome.isdigit():
                nome = str(nome)
                break
            else:
                print('Digite apenas letras.')
                continue

        while True:
            idade = input('Digite sua idade: \n')
            if idade.isdigit():
                idade = int(idade)
                break
            else:
                print('Só é possível digitar números.')
                continue

        while True:     
            email = input('Digite seu email: \n')
            if "@" not in email or "." not in email:
                print("E-mail inválido")
                continue
            else:
                print('Email válido.')
                break

        while True:
            senha = input('Crie sua senha (mínimo 6 caracteres e forte de preferência): \n')
            if len(senha) < 6:
                print('Senha muito curta.')
                continue
            confirmar_senha = input('Confirme sua senha: \n')
            if senha != confirmar_senha:
                print('Senhas não conferem.')
                continue

           # Criptografa a senha
            senha_armazenar = sha256(senha.encode()).hexdigest()
            print('Sua senha foi criptografada!')
            print('Cadastro concluído com sucesso!')

            # Salva o novo cadastro
            novo_cadastro = {
                'nome': nome,
                'idade': idade,
                'email': email,
                'senha': senha_armazenar
            }
            cadastros.append(novo_cadastro)

            with open(caminho_arquivo, 'w') as arquivo:
                json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)
            break

        if funcao_voltar_sair() == 'voltar':
            continue
    # Opção 4 - Login
    if ver == '4':
        print('Área de Login')
        email_login = input('Digite seu email: \n').strip()
        senha_login = input('Digite sua senha: \n').strip()
        senha_login_hash = sha256(senha_login.encode()).hexdigest()
        
        # Verifica se o e-mail e senha estão corretos
        for usuario in cadastros:
            if usuario['email'] == email_login and usuario['senha'] == senha_login_hash:
                print(f'Login bem-sucedido! Bem-vindo, {usuario["nome"]}!')
                usuario_logado = usuario
                break
        else:
            print('Email ou senha incorretos.')

        if funcao_voltar_sair() == 'voltar':
            continue

    if ver == '3':
        if usuario_logado is None:
            print(' Você precisa estar logado para acessar os cursos.')
            if funcao_voltar_sair() == 'voltar':
                continue
            else:
                exit()
        while True:
            print('Cursos disponíveis')
            print('| 0 - Página anterior                 |')
            print('| 1 - Linguagem python                |')
            print('| 2 - Pensamento lógico computacional | ')
            print('| 3 - Cibersegurança                  |')
                
            selecionar = input('Selecione (0,1,2 ou 3)\n')

            if selecionar == ('0'):
                 break
            
            if selecionar == ('1'):
                print('Seja bem vindo ao curso de Linguagem Python!')
                print('Neste curso será apresentado um conteúdo sobre a matéria, e no final você responderá um questionário!\n')
                while True:
                    print('| 0 - Página anterior|')
                    print('| 1 - Conteúdo       |')
                    print('| 2 - Questionário   |')
                    
                    learn = input('Escolha: (0/1/2)\n').strip()
                    
                    if learn == ('0'):
                        break

                    if learn == ('1'):
                        print('''Python é uma linguagem de programação muito usada no mundo todo. Ela foi criada para ser simples de aprender e fácil de entender. Por isso, muitas pessoas que estão começando a programar escolhem Python como primeira linguagem.

    Uma das coisas que torna o Python tão legal é que ele usa palavras parecidas com o inglês. Por exemplo, se você quiser mostrar algo na tela, basta escrever print("Olá!"). A palavra print significa "imprimir", mas aqui quer dizer "mostrar na tela".

    Para repetir algo várias vezes, Python usa comandos chamados laços de repetição, e um dos mais usados é o for. Ele permite que o programa faça algo várias vezes de forma automática.

    Além disso, quando o programador quer escrever uma dica ou explicação no código, ele pode usar um comentário. Comentários não são executados pelo computador — são só para ajudar as pessoas a entenderem melhor. Em Python, comentários começam com o símbolo''')
                        if funcao_voltar_sair() == 'voltar':
                            continue
                    
                    elif learn == ('2'):
                        print('Hora de colocar o aprendizado em prática!')
                        print('No seguinte questionário você responderá 3 perguntas. Boa sorte!')
                        
                        while True:
                            p1 = input(''' 1 - Qual comando é usado para exibir algo na tela em Python?
        a) echo
        b) show
        c) print
        d) display\n''').strip().lower()
                            if p1 == ('c'):
                                print('Resposta correta!')
                                break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                        while True:
                            p2 = input(''' Qual dessas estruturas é usada para repetição em Python?
        a) if
        b) loop
        c) repeat
        d) for\n''').strip().lower()
                            if p2 == ('d'):
                                    print('Resposta correta!')
                                    break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                    while True:    
                        p3 = input(''' Como se inicia um comentário em Python?
        a) //
        b) <!--
        c) #
        d) /*\n''').strip().lower()
                        if p3 == ('c'):
                                    print('Resposta correta!')
                                    print('PARABÉNS! Você finalizou o curso de Python. Volte e faça os outros!')
                                    break
                        else:
                            print('Resposta incorreta! Tente novamente.')
                            continue
            if selecionar == ('2'):
                print('Seja bem vindo ao curso de pensamento lógico computacional!')
                print('Neste curso será apresentado um conteúdo sobre a matéria, e no final voce responderá um questionário!\n')
                while True:
                    print('| 0 - Página anterior|')
                    print('| 1 - Conteúdo       |')
                    print('| 2 - Questionário   |')
                    
                    learn = input('Escolha: (0/1/2)\n').strip()
                    
                    if learn == ('0'):
                        break

                    if learn == ('1'):
                        print(''' Pensamento lógico computacional é a base para quem quer programar ou resolver problemas com organização e clareza. Ele envolve entender um problema, pensar em soluções passo a passo e criar um algoritmo, que é uma sequência de instruções bem definidas para resolver uma tarefa.

Essa forma de pensar não é usada só na programação — ela também ajuda no dia a dia, como quando seguimos uma receita, montamos um móvel ou planejamos uma rota.

Os quatro pilares principais do pensamento lógico computacional são:

Decomposição: dividir um problema grande em partes menores para facilitar a solução.

Reconhecimento de padrões: observar semelhanças entre problemas para resolver mais rápido.

Abstração: focar no que é importante e ignorar os detalhes que não influenciam.

Algoritmos: criar passos claros e organizados para chegar ao resultado.

Além disso, usamos sequência, repetição e decisões (condições) para montar a lógica. Por exemplo, um programa pode repetir uma ação enquanto uma condição for verdadeira, ou tomar caminhos diferentes dependendo de uma escolha do usuário. ''')
                        if funcao_voltar_sair() == 'voltar':
                            continue
                    
                    elif learn == ('2'):
                        print('Hora de colocar o aprendizado em prática!')
                        print('No seguinte questionário você responderá 3 perguntas. Boa sorte!')
                        
                        while True:
                            p1 = input(''' 1) O que é um algoritmo?
a) Um código secreto usado por hackers
b) Um conjunto de passos organizados para resolver um problema
c) Uma linguagem de programação visual
d) Um tipo de erro comum em computadores\n''').strip().lower()
                            if p1 == ('b'):
                                print('Resposta Correta!')
                                break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                        while True:
                            p2 = input(''' 2) O que significa decompor um problema?
a) Torná-lo mais difícil com muitas variáveis
b) Dividir o problema em partes menores e mais simples
c) Esquecer o problema temporariamente
d) Criar cópias diferentes do mesmo problema\n''').strip().lower()
                            if p2 == ('b'):
                                    print('Resposta correta!')
                                    break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                    while True:    
                        p3 = input(''' 3) Qual estrutura lógica representa uma escolha entre caminhos diferentes?
a) for
b) print
c) if
d) input\n''').strip().lower()
                        if p3 == ('c'):
                                    print('Resposta correta!')
                                    print('PARABÉNS! Você finalizou o curso de infraestrutura. Volte e faça os outros!')
                                    break
                        else:
                            print('Resposta incorreta! Tente novamente.')
                            continue
            if selecionar == ('3'):
                print('Seja bem vindo ao curso de Cibersegurança!')
                print('Neste curso será apresentado um conteúdo sobre a matéria, e no final você responderá um questionário!\n')
                while True:
                    print('| 0 - Página anterior|')
                    print('| 1 - Conteúdo       |')
                    print('| 2 - Questionário   |')
                    
                    learn = input('Escolha: (0/1/2)\n').strip()
                    
                    if learn == ('0'):
                        break

                    if learn == ('1'):
                        print('''Cibersegurança é a área da tecnologia que cuida da proteção de dados, sistemas e redes contra ataques, acessos indevidos e vazamentos. Hoje em dia, como quase tudo está conectado — bancos, escolas, redes sociais — proteger essas informações se tornou essencial.

Existem várias formas de ataque, como os vírus (malwares), que podem danificar arquivos ou roubar dados, e as tentativas de phishing, que são golpes onde alguém finge ser uma empresa confiável para enganar o usuário e conseguir senhas ou informações.

Uma boa prática de cibersegurança inclui usar senhas fortes, manter sistemas atualizados, não clicar em links suspeitos e usar antivírus. Também é importante saber que firewalls e outras ferramentas ajudam a controlar o que entra e sai das redes, criando uma camada extra de proteção.''')
                        if funcao_voltar_sair() == 'voltar':
                            continue
                    
                    elif learn == ('2'):
                        print('Hora de colocar o aprendizado em prática!')
                        print('No seguinte questionário você responderá 3 perguntas. Boa sorte!')
                        
                        while True:
                            p1 = input(''' 1) O que é cibersegurança?
a) Um tipo de computador mais seguro
b) O estudo de como organizar cabos de rede
c) A proteção de sistemas e dados contra ameaças digitais
d) Um programa usado para limpar arquivos inúteis
\n''').strip().lower()
                            if p1 == ('c'):
                                print('Resposta correta!')
                                break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                        while True:
                            p2 = input(''' 2) O que é phishing?
a) Um antivírus popular
b) Um tipo de ataque que tenta enganar a pessoa para roubar dados
c) Um erro no sistema de senhas
d) Um aplicativo de segurança para redes sociais\n''').strip().lower()
                            if p2 == ('b'):
                                    print('Resposta correta!')
                                    break
                            else:
                                print('Resposta incorreta! Tente novamente.')
                                continue
                    while True:    
                        p3 = input(''' 3) O que o firewall faz?
a) Refrigera os componentes do computador
b) Controla o que entra e sai da rede, ajudando na proteção
c) Limpa os cookies do navegador
d) Armazena backups automaticamente\n''').strip().lower()
                        if p3 == ('b'):
                                    print('Resposta correta!')
                                    print('PARABÉNS! Você finalizou o curso de Cibersegurança. Volte e faça os outros!')
                                    break
                        else:
                            print('Resposta incorreta! Tente novamente.')
                            continue