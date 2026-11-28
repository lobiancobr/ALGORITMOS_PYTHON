import logging

# Configuração básica - mostra no console
logging.basicConfig(
    level=logging.DEBUG,  # Mostra TODOS os níveis
    format='%(levelname)-10s | %(message)s'
)

print("=" * 60)
print("🎬 MISSÃO 1: Os 5 Níveis de Severidade")
print("=" * 60)

# Simulando um dia no sistema bancário
logging.debug("🔍 [DEBUG] Conectando ao banco de dados em localhost:5432")
logging.info("ℹ️ [INFO] Sistema iniciado com sucesso")
logging.warning("⚠️ [WARNING] Espaço em disco abaixo de 20%")
logging.error("❌ [ERROR] Falha ao processar transação #12345")
logging.critical("🚨 [CRITICAL] Banco de dados principal caiu!")

print("\n💡 Observe como cada nível tem uma 'personalidade' diferente!")