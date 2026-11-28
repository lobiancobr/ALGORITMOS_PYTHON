import re
from collections import Counter

print("🔍 ANÁLISE DO ARQUIVO 'banco_completo.log'")
print("=" * 60)

# Lendo o arquivo
with open('banco_completo.log', 'r') as f:
    linhas = f.readlines()

print(f"\n📊 Total de linhas no log: {len(linhas)}")

# Contando níveis de severidade
niveis = Counter()
for linha in linhas:
    if 'DEBUG' in linha:
        niveis['DEBUG'] += 1
    elif 'INFO' in linha:
        niveis['INFO'] += 1
    elif 'WARNING' in linha:
        niveis['WARNING'] += 1
    elif 'ERROR' in linha:
        niveis['ERROR'] += 1
    elif 'CRITICAL' in linha:
        niveis['CRITICAL'] += 1

print("\n📈 Distribuição de níveis:")
for nivel, contagem in niveis.items():
    barra = '█' * contagem
    print(f"  {nivel:10s} {barra} ({contagem})")

# Encontrando mensagens de erro
print("\n❌ Mensagens de ERRO encontradas:")
erros = [l.strip() for l in linhas if 'ERROR' in l or 'CRITICAL' in l]
for i, erro in enumerate(erros, 1):
    print(f"  {i}. {erro}")

# Procurando padrões (ex: horários)
print("\n⏰ Horários dos eventos:")
horarios = re.findall(r'\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2})', ''.join(linhas))
for h in horarios:
    print(f"  • {h}")

print("\n💡 Isso é apenas o começo! Em produção, usamos ferramentas como:")
print("  • grep/awk para buscas rápidas")
print("  • Elasticsearch + Kibana para visualização")
print("  • Splunk para análise corporativa")