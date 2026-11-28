import logging
from datetime import datetime

# 🧹 PASSO 1: Limpar qualquer configuração anterior (reset completo)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# 🎯 PASSO 2: Criar um LOGGER NOMEADO (a forma profissional)
logger_banco = logging.getLogger('BancoDigital')
logger_banco.setLevel(logging.DEBUG)  # Captura TODOS os níveis

# 🧹 Remover handlers antigos se existirem (evita duplicação)
logger_banco.handlers.clear()

# 📄 PASSO 3: Criar um HANDLER específico para arquivo
handler_arquivo = logging.FileHandler('banco_digital.log', mode='w', encoding='utf-8')
handler_arquivo.setLevel(logging.DEBUG)

# 🎨 PASSO 4: Definir o formato bonito
formatador = logging.Formatter(
    '%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler_arquivo.setFormatter(formatador)

# 🔗 PASSO 5: Anexar o handler ao logger
logger_banco.addHandler(handler_arquivo)

print("🏦 Simulando um dia no Banco Digital...\n")

# 📝 Usando o logger nomeado (note: logger_banco.info, não logging.info)
logger_banco.info("Sistema iniciado")
logger_banco.info("Cliente João fez login")
logger_banco.info("João depositou R$ 500,00")
logger_banco.warning("Tentativa de saque acima do limite por João")
logger_banco.error("Falha na conexão com o servidor de e-mail")
logger_banco.info("João fez logout")
logger_banco.info("Sistema finalizado")

print("✅ Log gravado no arquivo 'banco_digital.log'")
print("\n📄 Conteúdo do arquivo:")
print("-" * 60)
with open('banco_digital.log', 'r', encoding='utf-8') as f:
    print(f.read())