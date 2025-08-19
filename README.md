# 💧 Projeto: Lembrete para Tomar Água

Esse projeto foi criado pensado no uso próprio e para uso daqueles que só querem um simples lembrete para tomar água enquanto usam o computador.

---

## 🚀 Funcionalidades
- [ ] Envia uma notificação pelo sistema te lembrando de tomar água;
- [ ] Permite escolher um intervalo de tempo entre 1 minuto e 3 horas;
- [ ] Roda em segundo plano (mantém uma janela aberta para que você saiba que ele está rodando);
- [ ] Utiliza janelas simples e sons do próprio sistema pra funcionar, logo possui baixo custo de recursos.

---
## 🛠 Tecnologias Utilizadas
Python

## 📚 O que aprendi
**Interface acessível:** Utilizar o tkInter para criar janelas que facilitam a interação do usuário com o programa
**Threading:** Utilizar threads para evitar congelamento completo do programa com a função sleep

## ⚙️ Instalação

Passos para instalar e rodar o projeto:

```bash
# Clone o repositório
git clone https://github.com/awtrox/lembrete-agua.git

# Acesse a pasta do projeto
cd lembrete-agua

# (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt