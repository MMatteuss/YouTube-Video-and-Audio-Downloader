# Importação
from pytubefix.cli import on_progress
from pytubefix import YouTube
import time
import re

# Carregando
def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

# Espaçamento
def espaco():
    print(" ")

# Verificador de URL
def verificarUrl(link):
    # Expressão regular para verificar se o link é do YouTube
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$')
    
    # Verifica se o link corresponde ao padrão do YouTube
    if youtube_regex.match(link):
        print("Link aceito.")
        return True
    else:
        # Extrai o domínio do link para exibir na mensagem
        dominio = re.findall(r'https?://(?:www\.)?([^/]+)', link)
        if dominio:
            print(f"Não aceitamos esse site ({dominio[0]}). Tente novamente.")
        else:
            print("Não aceitamos esse site. Tente novamente.")
        return False


# Pergunta de confirmação
def confirmacao(nomeLink):
    simNao = ''
    print(f'O nome é \033[32m{nomeLink}\033[m?')

    simNao = input('Digite S(Sim) ou N(Não): ').lower()
    print(simNao)

    if simNao == 's' or simNao == 'sim':
        return 1
    if simNao == 'n' or simNao == 'não' or simNao == 'nao':
        return 0
    else:
        espaco()
        print('Não entendi')
        confirmacao(nomeLink=nomeLink)

# Download do video
def videoDownload(youtubeLink, youtubeYt):
    url = youtubeLink
    yt = youtubeYt
    nomeLink = yt.title
    # Obtém o stream com a resolução mais alta disponível
    stream = yt.streams.get_highest_resolution()

    # Faz o download do stream com vídeo e áudio juntos
    resultado = confirmacao(nomeLink)
    if resultado == 1:
        if verificarUrl(url):
            for n in range(101):
                progress_bar(n/100)
                time.sleep(0.01)
            espaco()
            stream.download()
            print('\033[1;32;40mConcluido com sucesso\033[m')
            time.sleep(1)
        else:
            print('\033[1;31;40mLink inválido.\033[m')
            espaco()
            telaUsuario()
        espaco()
        telaUsuario()
    else:
        espaco()
        telaUsuario()

# Download do audio
def audioDownload(youtubeLink, youtubeYt):
    url = youtubeLink
    yt = youtubeYt
    nomeLink = yt.title
    # Obtém o melhor stream de vídeo e o melhor stream de áudio
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').first()

    # Baixa os streams de vídeo e áudio
    resultado = confirmacao(nomeLink)
    if resultado == 1:
        if verificarUrl(url):
            for n in range(101):
                progress_bar(n/100)
                time.sleep(0.01)
            espaco()
            audio_stream.download()
            print('\033[1;32;40mConcluido com sucesso\033[m')
            time.sleep(1)
        else:
            print('\033[1;31;40mLink inválido.\033[m')
            espaco()
            telaUsuario()
        espaco()
        telaUsuario()
    else:
        espaco()
        telaUsuario()

# Escolha do usuario
def telaUsuario():
    print("Escolha o formato do download do arquivo:")
    print("1 - Video")
    print("2 - Audio")
    print("0 - Sair")

    escolhaUsuario = int(input('Digite:'))

    if escolhaUsuario == 0:
        print('Saindo... saiu')
    elif escolhaUsuario == 1 or escolhaUsuario == 2:
        espaco()
        print("Digite a URL(link) do audio que será feito o download:")
        url = input("URL >")
        yt = YouTube(url, on_progress_callback=on_progress)
        
        if escolhaUsuario == 1:
            videoDownload(url, yt)

        if escolhaUsuario == 2:
            audioDownload(url, yt)

    else:
        print('Carectere desconhecido, por favor, tente novamente!')
        telaUsuario()
    
telaUsuario()