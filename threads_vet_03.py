import multiprocessing
import random
import time

def processamento(vetor_id,dis_max):
    dis_percorrida:int=0
    tam_salto:int=0

    while dis_percorrida < dis_max:
        tam_salto = random.randint(1,5)
        dis_percorrida += tam_salto

        print(f'Sapo {vetor_id} percorreu {dis_percorrida}cm e o seu salto foi de {tam_salto}cm')
        time.sleep(0.4)
    #Fim-loop
    print (f'Sapo {vetor_id} venceu a corrida :)')
#Fim


def main():
    sapo_id:int=0
    proc:int=5 # 5 sapos
    dis_max:int=0
    
    dis_max = random.randint(1,15) # Distância máxima

    vetor_id:int=[0]*proc

    for i in range(proc):
        vetor_id[i] = i # id dos sapos

        vetor_id[i] = (i,dis_max) 
    #Fim-loop

    # Inicializando as threads
    with multiprocessing.Pool(processes=proc) as pool:
        pool.starmap(processamento,vetor_id)
    #Fim
#Fim-main

if __name__ == '__main__':
    main()
#Fim