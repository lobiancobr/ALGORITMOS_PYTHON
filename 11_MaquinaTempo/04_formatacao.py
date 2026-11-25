import datetime as dt

hoje = dt.datetime.now()

print("🇧🇷 Formato Brasileiro (dd/mm/aaaa):")
print(hoje.strftime('%d/%m/%Y %H:%M:%S'))

print("\n📝 Formato por Extenso:")
print(hoje.strftime('%A, %B %d %Y'))