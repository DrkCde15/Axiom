# 📚 Axiom - Seu corretor de Tarefas com IA

Sistema web para correção automática de tarefas escolares usando Gemini AI.

## 📁 Estrutura do Projeto

```
projeto/
│
├── app.py                 # Backend Flask
├── requirements.txt       # Dependências Python
│
└── templates/
    ├── index.html        # Página inicial
    └── chat.html         # Página do chat
```

## 🚀 Como Instalar e Executar

### 1. Pré-requisitos
- Python 3.8 ou superior
- Conta Google Cloud com API do Gemini habilitada

### 2. Obter API Key do Gemini
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie sua chave

### 3. Instalação

```bash
# Clone ou baixe o projeto
cd seu-projeto

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 4. Configuração

Abra o arquivo `app.py` e substitua `'SUA_API_KEY_AQUI'` pela sua chave do Gemini.

**Ou** defina como variável de ambiente:

```bash
# Windows
set GEMINI_API_KEY=sua_chave_aqui

# Linux/Mac
export GEMINI_API_KEY=sua_chave_aqui
```

### 5. Executar

```bash
python app.py
```

O servidor estará rodando em: `http://localhost:5000`

## 🎯 Como Usar

1. Acesse `http://localhost:5000`
2. Clique em "Começar Agora"
3. Digite ou cole o texto da sua tarefa
4. (Opcional) Anexe imagens ou documentos do trabalho
5. Clique em "Enviar"
6. Receba feedback detalhado com:
   - Nota de 0 a 10
   - Classificação (Excelente/Bom/Médio/Ruim)
   - Pontos fortes
   - Pontos a melhorar
   - Sugestões específicas

## 📦 Funcionalidades

✅ Interface moderna e responsiva  
✅ Upload de múltiplos arquivos  
✅ Análise com IA (Gemini)  
✅ Feedback estruturado e detalhado  
✅ Histórico de conversas  
✅ Sistema de classificação visual por cores  

## 🛠️ Tecnologias

- **Backend:** Python
- **Frontend:** HTML5, CSS3, JavaScript
- **IA:** Google Gemini API
- **Processamento de Imagens:** Pillow

## 📝 Notas

- Tamanho máximo de arquivo: 16MB
- Formatos aceitos: Imagens (JPG, PNG, PDF, DOCX)
- A API Key do Gemini tem limite gratuito de requisições

## 📧 Suporte

Para problemas com a API do Gemini, consulte a [documentação oficial](https://ai.google.dev/docs).
