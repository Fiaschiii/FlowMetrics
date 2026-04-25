# 📊 FlowMetrics

Sistema automatizado de análise de dados que coleta métricas do Google Analytics, armazena em um banco MySQL e exibe em um dashboard interativo — de forma totalmente automática.


## 🛠️ Stack Tecnológica

- **Python 3.13**
- **MySQL** — Banco de dados
- **Google Analytics API** — Fonte de dados
- **Streamlit** — Dashboard visual
- **CustomTkinter** — Janela desktop
- **Google Cloud ADC** — Autenticação
- **Ubuntu** — Sistema operacional
- **VSCode** — Editor de código

---

## ✅ Funcionalidades

- Pipeline automatizado com execução diária às 08:00
- Dashboard visual com gráficos e métricas
- Janela desktop para rodar sem usar o terminal
- Integração com Google Cloud ADC
- Histórico de 30 dias de métricas
- Resumo geral com total de sessões, usuários e visualizações

---

## 📁 Estrutura do Projeto

```
FLOW_METRICS/
├── automation/
│   └── pipeline.py          # Cérebro da automação
├── dashboard/
│   └── app.py               # Interface visual (Streamlit)
├── database/
│   ├── setup_db.py          # Cria o banco de dados
│   └── seed.py              # Gera dados fictícios
├── services/
│   ├── analytics_service.py # Busca dados no Google
│   └── db_service.py        # Opera o banco MySQL
├── venv/                    # Ambiente virtual Python
├── .gitignore               # Arquivos ignorados pelo Git
├── app_launcher.py          # Janela de interface
├── main.py                  # Ponto de entrada
└── requirements.txt         # Lista de bibliotecas
```

---

## ⚙️ Instalação e Configuração

### Pré-requisitos

- Python 3.13
- MySQL
- Google Cloud CLI
- Git

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/flow_metrics.git
cd flow_metrics
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o MySQL

```bash
sudo systemctl start mysql
sudo mysql
```

Dentro do MySQL:
```sql
CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON *.* TO 'seu_usuario'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5️⃣ Configure o Google Cloud

```bash
sudo snap install google-cloud-cli --classic
gcloud auth application-default login
gcloud auth application-default set-quota-project seu-project-id
```

### 6️⃣ Crie o banco de dados

```bash
python3 database/setup_db.py
```

### 7️⃣ (Opcional) Gere dados fictícios para teste

```bash
python3 database/seed.py
```

---

## ▶️ Como Rodar

```bash
# 1. Ative o venv
source venv/bin/activate

# 2. Inicie o MySQL
sudo systemctl start mysql

# 3. Rode a janela do FlowMetrics
python3 app_launcher.py
```

Na janela clique em **▶️ Iniciar FlowMetrics** e depois em **🌐 Abrir no Navegador**!

---

## 🔄 Fluxo Completo

```
app_launcher.py
      ↓
Clica em "Iniciar FlowMetrics"
      ↓
main.py
      ↓
setup_db.py → Garante banco criado
      ↓
pipeline.py → Executa automação
      ↓
analytics_service.py → Busca no Google Analytics
      ↓
db_service.py → Salva no MySQL
      ↓
dashboard/app.py → Exibe no navegador
      ↓
📊 Dados visíveis no FlowMetrics!
```

---

## 🪟 Rodando no Windows

```powershell
# Ativar o venv
venv\Scripts\activate

# Instalar as libs
pip install -r requirements.txt

# Rodar o projeto
python app_launcher.py
```

Diferenças principais:
- Ativar venv: `venv\Scripts\activate` em vez de `source venv/bin/activate`
- Rodar Python: `python` em vez de `python3`
- MySQL inicia automaticamente como serviço do sistema
- Tkinter já vem incluído com o Python

---

## 📊 Métricas Monitoradas

| Métrica | Descrição |
|---|---|
| **Sessões** | Número de visitas ao site por dia |
| **Usuários** | Número de pessoas únicas que acessaram |
| **Visualizações** | Total de páginas abertas |
| **Taxa de Rejeição** | % de pessoas que saíram sem interagir |
| **Tempo Médio** | Tempo médio de cada sessão em segundos |

---

## 🔑 Variáveis Importantes

```
Banco MySQL:       flowmetrics_db
Porta Streamlit:   localhost:8501
Execução diária:   08:00
Histórico:         30 dias
```

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por Miguel Fiaschi 🚀
