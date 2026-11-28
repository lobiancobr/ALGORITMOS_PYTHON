import logging

# Códigos de cores ANSI
class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG':    '\033[36m',    # Ciano
        'INFO':     '\033[32m',    # Verde
        'WARNING':  '\033[33m',    # Amarelo
        'ERROR':    '\033[31m',    # Vermelho
        'CRITICAL': '\033[1;31m',  # Vermelho negrito
    }
    RESET = '\033[0m'

    def format(self, record):
        cor = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{cor}{record.levelname}{self.RESET}"
        return super().format(record)

# Configurando
logger_color = logging.getLogger('Colorido')
logger_color.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter('%(levelname)s | %(message)s'))
logger_color.addHandler(handler)

print("🌈 Logs coloridos para facilitar a leitura:\n")
logger_color.debug("🔍 Mensagem de debug (técnica)")
logger_color.info("ℹ️ Mensagem informativa")
logger_color.warning("⚠️ Atenção: algo estranho")
logger_color.error("❌ Erro detectado!")
logger_color.critical("🚨 ERRO CRÍTICO! Sistema em perigo!")

print("\n💡 Veja como as cores ajudam a identificar rapidamente o nível!")