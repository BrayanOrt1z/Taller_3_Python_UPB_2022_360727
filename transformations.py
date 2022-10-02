import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def transformation(path_1, path_2):
    # Esta sección lo que hace es leer los argumentos de la función, es decir, la ruta de las imágenes.
    img_bgr = cv.imread(path_1)
    img2_bgr = cv.imread(path_2)

    # Aquí se hace el cambio de BGR a RGB.
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    img2_rgb = cv.cvtColor(img2_bgr, cv.COLOR_BGR2RGB)

    # Redimensionamiento de las imágenes.
    rsz_img1= cv.resize(img_rgb, (500,500))
    rsz_img2= cv.resize(img2_rgb, (500,500))

    # Cambio de la escala de colores a escala de grises.
    img_gray = cv.cvtColor(rsz_img1, cv.COLOR_RGB2GRAY)

    # Filtrado y máscara.
    retval, img_mask = cv.threshold(img_gray, 130, 255, cv.THRESH_BINARY)
    img_mask_inv = cv.bitwise_not(img_mask)
    img_background = cv.bitwise_and(rsz_img2, rsz_img2, mask=img_mask)
    img_foreground = cv.bitwise_and(rsz_img1, rsz_img1, mask=img_mask_inv)

    # Imagen resultante.
    result = cv.add(img_background,img_foreground)
    
    # Dibujo de un rectangulo en la imagen resultante.
    cv.rectangle(result, (110, 70),(370, 350),(0, 255, 0), 3)

    # Modificación de brillo de la imagen resultante.
    matrix = np.ones(rsz_img1.shape, dtype='uint8')*50
    img_rgb_darker = cv.subtract(result, matrix)
   
    # Modificación de contraste de la imagen a la que se le modifico el brillo.
    matrix2 = np.ones(rsz_img1.shape) * 1.2
    img_rgb_brighter = np.uint8(cv.multiply(np.float64(img_rgb_darker), matrix2))

    # Imagen resultante con todas las transformaciones.
    final_img = cv.rotate(img_rgb_brighter, cv.ROTATE_90_CLOCKWISE)

    # Se crea la carpeta dónde se almacenará la imagen resultante..
    folder = os.mkdir('Resultados')
    
    # Creación del archivo con extensión .png
    new_img = cv.imwrite("Resultados/Final_Image.png", final_img[:,:,::-1])
    return cv.imshow('Final Image', final_img), cv.waitKey(0)
