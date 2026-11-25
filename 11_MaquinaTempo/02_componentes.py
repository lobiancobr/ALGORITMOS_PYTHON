import datetime as dt

hoje = dt.datetime.now()

print("🧬 Raio-X do Momento Atual:")
print("dia:     %02d" % hoje.day)
print("mes:     %02d" % hoje.month)
print("ano:     %04d" % hoje.year)
print("-----------------------------")
print("hora:    %02d" % hoje.hour)
print("minuto:  %02d" % hoje.minute)
print("segundo: %02d" % hoje.second)