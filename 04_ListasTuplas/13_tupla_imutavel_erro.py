# PY04 - Tentando modificar um elemento de uma tupla
# ATENÇÃO: este código gera TypeError DE PROPÓSITO.
# Demonstra que tuplas são imutáveis:
#   TypeError: 'tuple' object does not support item assignment

dimensions = (200, 50)  # (adicionado para o arquivo rodar isoladamente)
dimensions[0] = 250