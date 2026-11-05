from perlin_noise import PerlinNoise
from noise_image import NoiseImage
def main():
    new_grid = PerlinNoise(10,10)
    noise = new_grid.get_noise(1.4,5)
    print(noise)

    image = NoiseImage(1000, 1000, new_grid, 1)
    image.generate_image()

if __name__ == "__main__":
    main()