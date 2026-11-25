from pathlib import Path
PASTA = Path.cwd()
print("Pasta de trabalho:", PASTA)
print("Arquivos:", [p.name for p in PASTA.iterdir() if p.is_file()])