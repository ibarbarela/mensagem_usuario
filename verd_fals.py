#aprendendo a usar if e else. Projeto verificador de idade

idade = int(input('Para tirar sua habilitação, digite sua idade para conferência: '))

if idade >=18:
    print('Você tem idade para tirar habilitação!')
else:
    print('Você não tem idade para tirar habilitação')



#outra opção usando elif. 

idade1 = int(input('Para tirar sua habilitação, digite sua idade para conferência:'))

if idade1 >=18:
    print('Você já pode fazer aprova prática para tirar sua habilitação!!')
elif idade1 >=16:
    print('Você ainda não tem idade para realizar a prova prática, mas pode fazer as aulas teóricas até ter 18 anos completos! ')
else:
    print('Você ainda não tem idade para iniciar o processo de habilitação!')
