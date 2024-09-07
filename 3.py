def main(faturamento_anual):
    
    menor_faturamento = faturamento_anual[0]
    maior_faturamento = 0
    total_faturamento = 0
    dias_com_faturamento = 0
    media_faturamento = 0
    dias_maiores_que_media = 0

    for i in range(len(faturamento_anual)):

        if(faturamento_anual[i] > 0):
            total_faturamento += faturamento_anual[i]

            if(faturamento_anual[i] < menor_faturamento):
                menor_faturamento = faturamento_anual[i]

            if(faturamento_anual[i] > maior_faturamento):
                maior_faturamento = faturamento_anual[i]

            dias_com_faturamento += 1

    media_faturamento = total_faturamento / dias_com_faturamento

    for i in range(len(faturamento_anual)):

        if(faturamento_anual[i] > 0):

            if(faturamento_anual[i] > media_faturamento):
                dias_maiores_que_media += 1

    print("{:.2f} eh o menor valor de faturamento diario".format(menor_faturamento))
    print("{:.2f} eh o maior valor de faturamento diario".format(maior_faturamento))
    print("{:.2f} eh a quantidade de dias com faturamento acima da media".format(dias_maiores_que_media))

if __name__ == '__main__':
    main([1, 2, 3, 4, 4, 4, 7, 3, 2, 1, 0, 0, 0, 8]) 