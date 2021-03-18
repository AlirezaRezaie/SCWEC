from cep import eye_open
import screen_brightness_control as sbc

def main():
    while True:
        try:
            if eye_open():
                sbc.set_brightness(100)
            else:
                sbc.set_brightness(0)
        except sbc.ScreenBrightnessError as error:
            print(error)
            pass
if __name__ == '__main__':
    main()
