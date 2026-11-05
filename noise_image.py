from perlin_noise import PerlinNoise
from PIL import Image

class NoiseImage:
    def __init__(self, width: int, height: int, noise: PerlinNoise, frequency: float = 1.0):
        self.width = width
        self.height = height
        self.noise = noise
        self.frequency = frequency

    def generate_image(self):
        image = Image.new('RGB', (self.width, self.height), "white")
        pixels = image.load()
        assert pixels is not None

        for i in range(image.size[0]):   
            for j in range(image.size[1]): 
                scale_x = self.noise.width / self.width
                scale_y = self.noise.height / self.height

                x = i * scale_x
                y = j * scale_y   
                noise_value = self.noise.get_noise(x * self.frequency, y * self.frequency)

                gray = int(((noise_value + 1) / 2) * 255)
                pixels[i, j] = (gray, gray, gray)

        image.show()