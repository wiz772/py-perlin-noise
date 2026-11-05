import math
import random

def generate_random_angle() -> float:
    random_angle =  random.uniform(0, 2*math.pi)
    return random_angle

def create_gradients_matrice(width: int, height: int) -> list: 
    matrice = []
    columns = width + 1
    rows = height + 1

    for y in range(rows):
        row_list = []
        for x in range(columns):
            angle = generate_random_angle()

            gx = math.cos(angle)
            gy = math.sin(angle)
            gradient = (gx, gy)

            row_list.append(gradient)

        matrice.append(row_list)
    return matrice

def calculate_vectors(x, y):
    cell_x = math.floor(x)
    cell_y = math.floor(y)

    top_left_corner_x, top_left_corner_y = (cell_x, cell_y)
    top_right_corner_x, top_right_corner_y = (cell_x + 1, cell_y)
    bottom_left_corner_x, bottom_left_corner_y = (cell_x, cell_y + 1)
    bottom_right_corner_x, bottom_right_corner_y = (cell_x + 1, cell_y + 1)

    top_left_vector = (x - top_left_corner_x, y - top_left_corner_y)
    top_right_vector = (x - top_right_corner_x, y - top_right_corner_y)
    bottom_left_vector = (x - bottom_left_corner_x, y - bottom_left_corner_y)
    bottom_right_vector = (x - bottom_right_corner_x, y - bottom_right_corner_y)

    return (top_left_vector, top_right_vector, bottom_left_vector, bottom_right_vector)

def dot_product(vector_a, vector_b) -> float:
    return (vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1])

def get_all_dot_products(x, y, vectors, gradients: list) -> tuple:
    cell_x = math.floor(x)
    cell_y = math.floor(y)
    top_left_vector, top_right_vector, bottom_left_vector, bottom_right_vector = vectors
    top_left_gradient, top_right_gradient, bottom_left_gradient, bottom_right_gradient = gradients[cell_y][cell_x], gradients[cell_y][cell_x + 1], gradients[cell_y + 1][cell_x], gradients[cell_y + 1][cell_x + 1]

    top_left_dot_product = dot_product(top_left_vector, top_left_gradient)
    top_right_dot_product = dot_product(top_right_vector, top_right_gradient)
    bottom_left_dot_product = dot_product(bottom_left_vector, bottom_left_gradient)
    bottom_right_dot_product = dot_product(bottom_right_vector, bottom_right_gradient)

    return (top_left_dot_product, top_right_dot_product, bottom_left_dot_product, bottom_right_dot_product)

def fade(t: float) -> float:
    return (6*t**5 - 15*t**4 + 10*t**3)

def lerp(a:float, b:float, t:float) -> float:
    return a + t * (b - a)

def interpolate_dot_products(x, y, dot_products):
    top_left_dot_product, top_right_dot_product, bottom_left_dot_product, bottom_right_dot_product = dot_products

    cell_x = math.floor(x)
    cell_y = math.floor(y)
    local_x = x - cell_x
    local_y = y - cell_y 

    u = fade(local_x)
    v = fade(local_y)

    interpolated_top = lerp(top_left_dot_product, top_right_dot_product, u)
    interpolated_bottom = lerp(bottom_left_dot_product, bottom_right_dot_product, u)

    interpolated_top_and_bottom = lerp(interpolated_top, interpolated_bottom, v)
    return interpolated_top_and_bottom

