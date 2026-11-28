import logging

# Formato "profissional" com muitas informações
logging.basicConfig(
    filename='banco_detalhado.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def depositar(conta, valor):
    logging.info(f"Tentativa de depósito de R$ {valor} na conta {conta}")
    if valor <= 0:
        logging.error(f"Valor inválido de depósito: R$ {valor}")
        return False
    logging.info(f"Depósito de R$ {valor} realizado com sucesso")
    return True

def sacar(conta, valor, saldo):
    logging.debug(f"Verificando saldo: conta={conta}, valor={valor}, saldo={saldo}")
    if valor > saldo:
        logging.warning(f"Saldo insuficiente para saque de R$ {valor}")
        return False
    logging.info(f"Saque de R$ {valor} realizado")
    return True

print("🔬 Log com formato rico (detalhes de arquivo, linha e função):\n")
depositar("001", 500)
depositar("002", -100)  # vai dar erro
sacar("001", 200, 1000)
sacar("001", 2000, 1000)  # saldo insuficiente

print("\n📄 Veja como o log mostra EXATAMENTE onde cada evento ocorreu:")
print("-" * 80)
with open('banco_detalhado.log', 'r') as f:
    print(f.read())