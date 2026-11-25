from datetime import datetime, timedelta

print('🔮 somar 50 dias à data atual')
print(datetime.today() + timedelta(days=50))

print('\n⏪ subtrair 15 horas da data atual')
print(datetime.today() - timedelta(hours=15))

print('\n⏩ acrescentar 60 minutos à data atual')
print(datetime.today() + timedelta(minutes=60))

print('\n📅 subtrair 2 semanas da data atual')
print(datetime.today() - timedelta(weeks=2))