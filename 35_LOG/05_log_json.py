import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Formatter personalizado que transforma logs em JSON"""
    def format(self, record):
        log_record = {
            "timestamp": datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S'),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        # Adiciona campos extras se existirem
        if hasattr(record, 'user'):
            log_record['user'] = record.user
        if hasattr(record, 'ip'):
            log_record['ip'] = record.ip
        if hasattr(record, 'action'):
            log_record['action'] = record.action

        return json.dumps(log_record, ensure_ascii=False)

# Configurando o logger JSON
logger_json = logging.getLogger('BancoJSON')
logger_json.setLevel(logging.DEBUG)

handler = logging.FileHandler('banco_json.log', mode='w')
handler.setFormatter(JSONFormatter())
logger_json.addHandler(handler)

print("📊 Gerando logs estruturados em JSON:\n")

# Simulando eventos com dados extras
extra_login = {'user': 'joao.silva', 'ip': '192.168.1.50', 'action': 'login'}
extra_saque = {'user': 'maria.santos', 'ip': '10.0.0.25', 'action': 'saque'}

logger_json.info("Usuário fez login", extra=extra_login)
logger_json.info("Saque realizado: R$ 200,00", extra=extra_saque)
logger_json.warning("Tentativa de saque acima do limite", extra=extra_saque)
logger_json.error("Falha na conexão com o banco de dados")

print("✅ Logs JSON gerados!")
print("\n📄 Conteúdo do arquivo (note como é estruturado):")
print("-" * 80)
with open('banco_json.log', 'r') as f:
    for linha in f:
        # Formata o JSON para ficar bonito
        dados = json.loads(linha)
        print(json.dumps(dados, indent=2, ensure_ascii=False))
        print()

print("\n💡 Cada linha é um JSON válido! Ferramentas como Elasticsearch amam isso!")