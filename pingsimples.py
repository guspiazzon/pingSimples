import os #Importar o módulo ou biblioteca OS
# que integra os programas e recursos do sistema operacional

print("#" *60) #Imprimindo o sostenido por 60 vezes antes de entrar com o valor a ser verificado

ip_ou_host = input ("Digite o IP ou HOST a ser verificado: ")  #Criando uma variável que irá receber
# do usuário um IP
print("-" *60) #Imprimindo o traço por 60 vezes
os.system('ping -n 6 {}' .format(ip_ou_host)) #Chamando o módulo sistema da biblioteca OS para chamar
# um comando desse sistema que é o comando PING, o -6 chama um determinado número de pacotes e depois vem o IP
# que vem em um formato através do format
print("-" *60) #Imprimindo o traço por 60 vezes


