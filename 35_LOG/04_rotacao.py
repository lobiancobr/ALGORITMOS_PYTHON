import logging
from logging.handlers import RotatingFileHandler

# Criando um logger com rotação
logger = logging.getLogger('BancoRotativo')
logger.setLevel(logging.DEBUG)

# Handler: máximo 500 bytes por arquivo, mantém 3 backups
handler = RotatingFileHandler(
    filename='banco_rotativo.log',
    maxBytes=500,      # Tamanho máximo do arquivo (500 bytes para demonstração)
    backupCount=3      # Manter 3 arquivos antigos
)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

print("🔄 Simulando rotação de logs (limite de 500 bytes por arquivo):\n")

# Gerando várias mensagens para forçar a rotação
for i in range(30):
    logger.info(f"Transação #{i+1}: Cliente comprou produto X por R$ {(i+1)*10},00")

print("✅ Rotação concluída!")
print("\n📁 Arquivos gerados (observe o sistema de backup):")
import os
for arquivo in sorted(os.listdir('.')):
    if arquivo.startswith('banco_rotativo'):
        tamanho = os.path.getsize(arquivo)
        print(f"  📄 {arquivo:25s} ({tamanho} bytes)")

print("\n💡 Veja como o Python criou banco_rotativo.log.1, .2 e .3 automaticamente!")