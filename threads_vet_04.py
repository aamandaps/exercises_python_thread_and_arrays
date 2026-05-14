import multiprocessing
import platform
import subprocess

def prop_os():

    return platform.system() # Retorna o SO
#Fim

def processamento(params):
    os_name:str=''
    comando:str=''
    output:str=''
    line:str=''

    #for i in range (3):
    os_name = prop_os() # Verificando qual o SO
    #print (os_name)

    if os_name == 'Linux':

        comando = 'ping -4 -c 10 ' + params

        process_array = comando.split(' ') #Divide string por espaços

        output = subprocess.Popen(process_array, stdout= subprocess.PIPE,text=True) #Executa o processo
        line = output.stdout.readline().decode('utf-8' , errors = 'ignore') #Leitura de cada linha

        #Enquanto a linha não for vazia
        while(line != ''):
            if ('avg' in line):
                
                #Particionando a linha
                parte = line.split('=')
                dados = parte[1]
                valores = dados.split('/')
                media = valores [1]

                print(params, 'Média =>', media)
            #Fim-verificação

            if ('time' in line):
                #Particionando a linha
                parte = line.split('=')
                tempo = parte [1]

                print(params, 'Tempo =>', tempo)
            #Fim-verificação
            #Lendo próxima linha
            line = output.stdout.readline().decode('utf-8', errors='ignore')
            #Fim-verificação da linha
        #Fim-loop
    elif os_name == 'Windows':

        comando = 'ping -4 -n 10 ' + params

        process_array = comando.split(' ')   #Divide string com espaços

        output = subprocess.Popen(process_array, stdout= subprocess.PIPE, text=True) #Executa o processo
        line = output.stdout.readline()

        #Enquanto a linha não for vazia
        while(line != ''):
            if ('Média' in line):

                #Particionando a linha
                parte = line.split('=')
                media = parte [1]

                print(params, 'Média =>', media)
            #Fim-verificação
            
            if ('tempo' in line):

                #Particionando a linha
                parte = line.split('=')
                
                if len(parte) > 1:
                    tempo = parte [1]
                
                    print(params, 'Tempo =>', tempo)
            #Fim-verificação
            #Lendo próxima linha
            line = output.stdout.readline()
            #Fim-verificação da linha      
        #Fim-loop
    else:
        print('Sistema Operacional não encontrado.')
    #Fim-verificação
#Fim-processamento

def main():
    params:str=[]
    proc:int=0

    proc=3

    params = [ 
        "www.uol.com.br",
        "www.terra.com.br",
        "www.google.com.br"
    ] # Lista dos servidores

    # Inicializando threads
    with multiprocessing.Pool(processes=proc) as pool:
        pool.map(processamento,params)
    #Fim
#Fim-main

if __name__ == '__main__':
    main()
#Fim