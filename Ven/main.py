from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from pytubefix.cli import on_progress
from pytubefix import YouTube, exceptions
import re
import os

app = Flask(__name__)
app.secret_key = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'  # Necessário para usar flash messages

DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def progress_bar(done):
    return "\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100)

def verificarUrl(link):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$')
    return youtube_regex.match(link)

def confirmacao(nomeLink):
    return True

def limpar_link(link):
    # Remove parâmetros adicionais após o '&' ou '?'
    link_limpo = link.split('&')[0].split('?')[0]
    # Converte "watch?v=" para "embed/" e "youtu.be" para "youtube.com/embed"
    if "watch?v=" in link:
        link_limpo = link.replace("watch?v=", "embed/")
    elif "youtu.be" in link:
        link_limpo = link.replace("youtu.be/", "youtube.com/embed/")
    return link_limpo

@app.route('/', methods=['GET', 'POST'])
def index():
    prontoDownload = False
    linkVideo = ""
    nomeVideo = ""
    arquivo = ""

    if request.method == 'POST':
        url = request.form['linkYoutube']
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            nomeLink = yt.title
            nomeArquivo = re.sub(r'[^\w\s-]', '', nomeLink).replace(' ', '_')  # Remove caracteres especiais
            linkVideo = limpar_link(url)  # Limpa e converte o link
            prontoDownload = True

            if 'formato' in request.form:
                formato = request.form['formato']

                if formato == 'mp4':
                    stream = yt.streams.get_highest_resolution()
                    if verificarUrl(url) and confirmacao(nomeLink):
                        for n in range(101):
                            progress_bar(n/100)
                        arquivo = os.path.join(DOWNLOAD_FOLDER, f'{nomeArquivo}.mp4')
                        stream.download(output_path=DOWNLOAD_FOLDER, filename=f'{nomeArquivo}.mp4')
                        flash(f"Download de vídeo concluído: {nomeLink}", "success")
                    else:
                        flash(f"Link inválido: {url}. Tente novamente.", "error")
                        return redirect(url_for('index'))
                elif formato == 'mp3':
                    audio_stream = yt.streams.filter(only_audio=True).first()
                    if verificarUrl(url) and confirmacao(nomeLink):
                        for n in range(101):
                            progress_bar(n/100)
                        arquivo = os.path.join(DOWNLOAD_FOLDER, f'{nomeArquivo}.mp3')
                        audio_stream.download(output_path=DOWNLOAD_FOLDER, filename=f'{nomeArquivo}.mp3')
                        flash(f"Download de música concluído: {nomeLink}", "success")
                    else:
                        flash(f"Link inválido: {url}. Tente novamente.", "error")
                        return redirect(url_for('index'))
                
                arquivo_absoluto = os.path.abspath(arquivo)
                return send_file(arquivo_absoluto, as_attachment=True)
        
        except exceptions.RegexMatchError:
            flash(f"Link inválido: {url}. Tente novamente.", "error")
            return redirect(url_for('index'))
        except exceptions.VideoUnavailable:
            flash(f"Erro na URL. Tente novamente.", "error")
            return redirect(url_for('index'))

    return render_template('index.html', prontoDownload=prontoDownload, linkVideo=linkVideo, nomeVideo=nomeVideo)

if __name__ == "__main__":
    app.run(port=8080)
