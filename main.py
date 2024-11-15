from PIL import Image, ImageDraw, ImageFont
from waveshare.epd2in13_V4 import EPD
import logging
import time

class Font():
    def __init__(self, clock: bool, size: int):
        if clock:
            self.font_name = 'digital-7.ttf'
        else:
            self.font_name = "DejaVuSansMono"
        self.get_font = ImageFont.truetype(self.font_name, size)

class WaveshareV4():
    def initialize(self):
        logging.info("Initializing waveshare v2in13_V4 display")
        self._display = EPD()
        self._display.init()
        self._display.Clear(0xFF)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.displayPartial(buf)

    def gpio_test(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, GPIO.HIGH)
        GPIO.cleanup()
        logging.info("GPIO successfully tested!")

    def clear(self):
        self._display.Clear(0xFF)

    def show_time(self):
        image = Image.new('1', (250, 122), 255)
        draw = ImageDraw.Draw(image)
        
        current_time = time.strftime("%H:%M:%S")
        font = Font(True, 85).get_font

        text_width, text_height = draw.textbbox((0, 0), current_time, font=font)[2:4]
        
        x_position = (250 - text_width) // 2
        y_position = (122 - text_height) // 2

        draw.text((x_position, y_position), current_time, font=font, fill=0)

        image = image.rotate(180, expand=True)
        self.render(image)

    def update_clock(self):
        while True:
            self.show_time()
            time.sleep(1)

if __name__ == "__main__":
    display = WaveshareV4()
    display.initialize()
    display.update_clock()