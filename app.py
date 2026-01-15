from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os
import io
from PIL import Image

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Tipos de arquivo suportados
ALLOWED_EXTENSIONS = {
    'png', 'jpg', 'jpeg', 'gif', 'webp',
    'pdf', 'docx', 'doc', 'pptx', 'ppt',
    'xlsx', 'xls', 'txt'
}

MIME_TYPES = {
    'pdf': 'application/pdf',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'doc': 'application/msword',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'ppt': 'application/vnd.ms-powerpoint',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'xls': 'application/vnd.ms-excel',
    'txt': 'text/plain',
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif',
    'webp': 'image/webp'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_mime_type(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    return MIME_TYPES.get(ext, 'application/octet-stream')

# Configure a API do Gemini
# IMPORTANTE: Use 'gemini-1.5-flash' sem o 'models/' se usar o SDK novo, 
# mas se der 404, o SDK pode estar tentando v1beta indevidamente.
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'SUA_API_KEY_AQUI')
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        message = request.form.get('message')
        files = request.files.getlist('files')
        
        if not message:
            return jsonify({'success': False, 'error': 'Mensagem não fornecida'}), 400

        # Seu system_instruction original
        prompt = f"""Você é um assistente educacional especializado em ajudar estudantes com trabalhos escolares e universitários.

O aluno enviou a seguinte mensagem:
{message}

Instruções:
- Se for uma saudação (oi, olá, etc), responda de forma amigável e se apresente
- Se for uma pergunta, responda de forma clara e educativa
- Se for um trabalho/tarefa para corrigir, forneça feedback detalhado incluindo:
  * Avaliação geral
  * Pontos positivos
  * Pontos a melhorar
  * Sugestões específicas
  * Nota de 0 a 10 e classificação (Excelente/Bom/Médio/Ruim)
- Se o aluno pedir para você fazer ou resolver algo, faça da melhor forma possível
- Se for uma conversa casual sobre estudos, seja prestativo e motivador

Responda de forma natural, clara e educativa."""

        contents = [prompt]
        
        for file in files:
            if file and file.filename and allowed_file(file.filename):
                file_data = file.read()
                mime_type = get_mime_type(file.filename)
                contents.append(types.Part.from_bytes(
                    data=file_data,
                    mime_type=mime_type
                ))
        
        # CHAMADA CORRIGIDA
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=2000
            )
        )
        
        # Extração segura do texto
        response_text = ""
        if response.text:
            response_text = response.text
        elif response.candidates and response.candidates[0].content.parts:
            response_text = response.candidates[0].content.parts[0].text
        else:
            return jsonify({'success': False, 'error': 'A IA não retornou texto.'}), 500

        return jsonify({
            'success': True,
            'response': response_text
        })
        
    except Exception as e:
        print(f"ERRO: {e}")
        return jsonify({
            'success': False, 
            'error': f'Erro no servidor: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)