from zipfile import ZipFile
from operations import Activity
import os

weekDays = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo", "buf"]

for day in range(8):
    file = open('{}.txt'.format(weekDays[day]), 'w')
    open("resultados.txt", "a")

    file.write("\t\t   {}\n".format(weekDays[day]))
    file.write("\nHorário: ______________ às _______________\n")
    file.write("\n1) Resolva as operações matemáticas abaixo:\n")

Activity.buildOperations()

#Zip and delete files
zipObj = ZipFile('atividadesDaSemana.zip', 'w')
for addFile in range(7):
    zipObj.write('{}.txt'.format(weekDays[addFile]))
    os.remove('{}.txt'.format(weekDays[addFile]))

zipObj.write('resultados.txt')
os.remove('buf.txt'), os.remove('resultados.txt')

print("Arquivos criados com sucesso!")
