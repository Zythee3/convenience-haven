from flask import Flask, request, render_template
import os

def upload():
    app = Flask(__name__)

    @app.route('/')
    
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        # Verifica se a solicitação tem o arquivo
        if 'file' not in request.files:
            return 'Nenhum arquivo encontrado'

        file = request.files['file']

        # Verifica se o nome do arquivo está vazio
        if file.filename == '':
            return 'Nome de arquivo vazio'

        # Salva o arquivo na pasta de upload
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)

        return 'Arquivo enviado com sucesso!'

    if __name__ == '__main__':
        app.run(debug=True)