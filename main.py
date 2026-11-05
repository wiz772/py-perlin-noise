from perlin_noise import PerlinNoise
def main():
    new_grid = PerlinNoise(10,10)
    noise = new_grid.get_noise(1.4,5)
    print(noise)

if __name__ == "__main__":
    main()