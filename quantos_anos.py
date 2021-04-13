import datetime

nascimento = int(input("Qual o ano que você nasceu: "))
ano = datetime.date.today().year
print(f"A minha idade é: {ano - nascimento}")




"""
import datetime

nascimento = int(input('Digite o ano em que voce nasceu: '))

ano = datetime.date.today().year

idade = ano - nascimento

print(f'Então vc possui: {idade} anos de idade.')
"""