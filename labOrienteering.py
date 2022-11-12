import sys
from PIL import Image
from colormap import rgb2hex
import numpy
import math

width_image = 395
height_image = 500
tbest = 4

LAND_COLORS = {'#F89412': '1', '#FFC000': '2', '#FFFFFF': '3',
               '#02D03C': '4', '#028828': '5', '#054918': '6',
               '#0000FF': '7', '#473303': '8', '#000000': '9',
               '#CD0065': '10'}

LAND_FACTORS = {'1': 4, '2': 0.5, '3': 2.5, '4': 2, '5': 1,
                '6': 0, '7': 0, '8': 4, '9': 3, '10': 0}


def getelevation(ele_file):
    ele_mat = numpy.zeros(shape=(height_image, width_image))
    i = 0
    for line in ele_file:
        elevations = line.split()
        for j in range(0, width_image):
            ele_mat[i][j] = elevations[j]
        i += 1
    return ele_mat


def getimage(tfile):
    im = Image.open(tfile)
    RGBA = im.load()
    hexaval = []
    for i in range(0, height_image):
        hors = []
        for j in range(0, width_image):
            r = RGBA[j, i][0]
            g = RGBA[j, i][1]
            b = RGBA[j, i][2]
            hors.append(rgb2hex(r, g, b))
        hexaval.append(hors)

    return hexaval


def getpoints(file):
    c_points = []
    i = 0
    for line in file:
        points = line.split()
        c_points.append((int(points[0]), int(points[1])))
        i += 1
    return c_points


def hn(pixel_matrix, ele_matrix, np, finals):
    final_i = finals[1]
    final_j = finals[0]
    np_j = np % 395
    np_i = int(np / 395)

    e_dist = math.sqrt((7.55 * (final_i - np_i)) ** 2 + (10.29 * (final_j - np_j)) ** 2)
    hn = e_dist * tbest


def findpath(start, end, pixel_matrix, ele_matrix):
    scolor = pixel_matrix[start[1]][start[0]]
    factor = LAND_FACTORS[LAND_COLORS[scolor]]
    dest_color = pixel_matrix[end[1]][end[0]]
    dfactor = LAND_FACTORS[LAND_COLORS[dest_color]]


def main():
    tfile=open(sys.argv[1])
    file = open(sys.argv[3])
    ele_file = open(sys.argv[2])
    pixel_matrix = getimage(tfile)
    ele_mat = getelevation(ele_file)
    c_points = getpoints(file)

