from microbit import *
import utime
active = False
pause = 1000
start = 0
screen = 0
x = 0
y = 0
bits = []
while True:
    cursor = display.set_pixel(x,y,5)
    sleep(30)
    if active:
        cursor = display.set_pixel(x,y,9)
    else:
        cursor = display.set_pixel(x,y,0)
    sleep(50)
    if button_b.is_pressed():
        start = utime.ticks_ms()
        while True:
            if not button_b.is_pressed():
                break
        if utime.ticks_diff(utime.ticks_ms(), start) < pause:
            if screen == 0:
                if active:
                    bits.append('1')
                else:
                    bits.append('0')
                if x + y == 8:
                    display.clear()
                    active = False
                    screen = 1
                    x = 0
                    y = 0
                elif x < 4:
                    active = False
                    x = x + 1
                else:
                    active = False
                    x = 0
                    y = y + 1
            else:
                if x and y == 1:
                    display.clear()
                    bitstring = ''.join(bits)

                elif x < 4:
                    active = False
                    x = x + 1
                else:
                    active = False
                    x = 0
                    y = y + 1
        else:
            if screen == 0:
                screen = 1
                while x <= 4 and y <= 4:
                    if x < 4:
                        x = x + 1

                    else:
                        x = 0
                        y = y + 1

                display.clear()
                x = 0
                y = 0
            else:
                x = 0
                y = 0
                display.clear()
                bitstring = ''.join(bits)

    elif button_a.is_pressed():
        start = utime.ticks_ms()
        while True:
            if not button_a.is_pressed():
                break
        if display.get_pixel(x,y) == 0:
            active = True
        else:
            active = False