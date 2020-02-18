
import cv2 as c
import glob as g



def segmentar_with_limiar(imagens, saida):

    #determinar limiar da imagem


    for a in range(len(imagens)):
        img = c.imread(imagens[a],0)
        soma = 0;
        total = 0;
        variacao = 1
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] > 0:
                    soma += img[i][j]
                    total += 1
        limiar = soma / total
        print('valor do limiar na imagem %s [ %i / %i ] ' %(str(a),soma,total) , ' = ', str(limiar), 'total = ', str((limiar+variacao)))

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] < (limiar+variacao):
                    img[i][j] = 0;

        c.imwrite(saida+str(a)+'.png', img)
        print('done:  ', saida+str(a)+'.png', ' = ', imagens[a])



if __name__ == '__main__':
    ''''''

    lista_img = g.glob('img/*.jpg')
    segmentar_with_limiar(lista_img, 'img/')
