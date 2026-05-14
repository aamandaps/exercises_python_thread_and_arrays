import multiprocessing
import time

def processamento(id):

    time.sleep(0.5)
    print('Thread #' , id)
    
#Fim-proc

def main():

    i:int=0
    proc:int=0

    proc=5 # quant. threads

    param:int=[0]*proc

    # Incrementando o vetor
    for i in range (proc):
        param[i]= i  # i  = id
    #Fim-loop

    with multiprocessing.Pool(processes=proc) as pool:
        pool.map(processamento,param) # Pega o valor do vetor e envia para a função
    #Fim-multiprocessing
#Fim-main

if __name__=="__main__":
    main()
#Fim