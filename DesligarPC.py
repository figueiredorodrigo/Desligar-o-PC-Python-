import pywhatkit
"""Para programar horário para o computador desligar."""

programar = int(input('Em quantos minutos você deseja desligar o computador? '))
desligar = programar * 60
pywhatkit.shutdown(time=desligar)