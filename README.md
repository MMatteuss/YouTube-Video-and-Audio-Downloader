### Baixar Vídeos do YouTube com Python

# YouTube Video and Audio Downloader

## Descrição do Projeto

Este projeto é uma aplicação web que permite aos usuários baixar vídeos e músicas do YouTube nos formatos MP4 e MP3, respectivamente. Usando Flask para o backend, a aplicação processa URLs do YouTube fornecidas pelos usuários, baixa o conteúdo usando a biblioteca `pytubefix` e permite que os usuários façam o download dos arquivos diretamente de seu navegador.

## Funcionalidades

- **Baixar Vídeos**: Permite baixar vídeos do YouTube em formato MP4.
- **Baixar Músicas**: Permite baixar músicas do YouTube em formato MP3.
- **Interface Simples e Responsiva**: Utiliza Bootstrap para uma experiência amigável.
- **Animações Suaves**: CSS e JavaScript garantem uma navegação fluida.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes dependências instaladas:

- Python 3.10 ou superior
- Flask
- pytubefix
- Bootstrap (incluído via CDN)
- Um navegador web moderno

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```bash
cd seu-repositorio
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
├── app.py              # Arquivo principal da aplicação Flask  
├── templates/          
│   └── index.html      # Página principal  
├── static/             
│   ├── css/            
│   │   └── style.css   # Estilos customizados  
│   └── js/             
│       └── animations.js # Animações JavaScript  
├── downloads/          # Diretório temporário para arquivos baixados  
└── README.md           # Este arquivo  
```

## Como Usar

1. Inicie o servidor Flask:

```bash
python app.py
```

2. Abra seu navegador e acesse `http://localhost:8080`.

3. Insira a URL do vídeo do YouTube que deseja baixar.

4. Escolha entre baixar como Vídeo (MP4) ou Música (MP3).

5. O arquivo será baixado diretamente para o seu dispositivo.

## Exemplo de Uso

1. Insira o link do vídeo do YouTube no campo designado.
2. Clique em "Vídeo" para baixar em MP4 ou "Música" para baixar em MP3.
3. Aguarde até que o download seja concluído.
4. O arquivo será salvo no diretório de downloads do seu navegador.

## Contribuição

Quer contribuir? Siga estas etapas:

1. Faça um fork do repositório.
2. Crie um branch para sua nova funcionalidade:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Commit suas alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie para o branch remoto:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações ou dúvidas, entre em contato:

- **Nome**: Mateus Monteiro
- **Email**: mateusmonteito57@gmail.com
- **GitHub**: [MMatteuss](https://github.com/MMatteuss)

---

Feito com ❤️ por Mateus Monteiro
