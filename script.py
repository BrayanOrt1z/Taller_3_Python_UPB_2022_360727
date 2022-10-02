import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from transformations import transformation


path1 = input('Ingrese la dirección de la primera imagen: ')
path2 = input('Ingrese la dirección de la segunda imagen: ')

transformation(path1, path2)