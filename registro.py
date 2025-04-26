from time import sleep
utl = str(input(("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "-     Registro Hopitalario    -\n"
      "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "-                             -\n"
      "-Gostaria de adicionar um     -\n"
      "-Registro?                    -\n"
                 "-[Y/N                         -\n"
                 "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                 "")))
if utl == "Y":
    print("0%")
    sleep(2)
    print("50%")
    sleep(2)
    print("100%")
    sleep(2)
else:
    print("Obrigado por usar")
    sleep(2)
    quit()

fich = str(input("Qual é o nome do ficheiro de registro?: "))
file = open(f'{fich}.txt', "w")
proceed = 1
while proceed == 1:
    nome = str(input("Nome do utente? "))
    file.write(f'nome: {nome}/')
    idade = str(input("Quantos anos é que tem? "))
    file.write(f'idade: {idade}\n')
    con = str(input("Continuar? [Y/N]"))
    if con == "Y":
        proceed = 1
    else:
        print("Obrigado por usar")
        sleep(5)
        proceed = 0
