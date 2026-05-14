import multiprocessing
import time
import random

def processamento(id , valores):
    soma:int=0

    # Loop que percorre o vetor num e incrementa a soma
    for cont in range (5):
        soma += valores[cont]
        time.sleep(0.2)
        #print(id , '=' , soma) /// 
    #Fim-loop
    print(id , '=' , soma)
#Fim-processamento

def main():
    id:int=0
    valores:int=0
    proc:int=0

    proc=3 # quant. threads

    params:int=[0]*proc

    for i in range(proc):

        valores = [0]*5

        for j in range (5):
            
            valores[j] = random.randint(1,100) # Preenchendo o vetor de num aleatórios
        #Fim-loop

        params[i] = (i , valores) # id + valores presentes na linha
    #Fim-loop

    with multiprocessing.Pool(processes=proc) as pool:
        pool.starmap(processamento,params)
    #Fim

if __name__ == '__main__':
    main()
#Fim