def on_button_pressed_a():
    global ze1, zl1, ce1, ze2, zl2, ce2, chyba
    if ze1 == 1:
        ze1 = 0
        zl1 = 1
        ce1 = 0
        ze2 = 0
        zl2 = 1
        ce2 = 1
    elif ce1 == 0 and zl1 == 1:
        ze1 = 0
        zl1 = 0
        ce1 = 1
        ze2 = 1
        zl2 = 0
        ce2 = 0
    elif zl1 == 0 and ce1 == 1:
        ce1 = 1
        zl1 = 1
        ze1 = 0
        ze2 = 0
        zl2 = 1
        ce2 = 0
    elif zl1 == 1 and ce1 == 1:
        ce1 = 0
        zl1 = 0
        ze1 = 1
        ze2 = 0
        zl2 = 0
        ce2 = 1
    if chyba == 1:
        ce1 = 1
        zl1 = 0
        ze1 = 0
        ze2 = 1
        zl2 = 0
        ce2 = 0
        chyba = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global chyba
    chyba = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

zl2 = 0
ze2 = 0
chyba = 0
ce2 = 0
ce1 = 0
zl1 = 0
ze1 = 0
ze1 = 1
zl1 = 0
ce1 = 0
ce2 = 1
chyba = 0
led.enable(False)

def on_forever():
    if chyba == 0:
        pins.digital_write_pin(DigitalPin.P0, ze1)
        pins.digital_write_pin(DigitalPin.P1, zl1)
        pins.digital_write_pin(DigitalPin.P2, ce1)
        pins.digital_write_pin(DigitalPin.P3, ze2)
        pins.digital_write_pin(DigitalPin.P4, zl2)
        pins.digital_write_pin(DigitalPin.P6, ce2)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P3, 0)
        pins.digital_write_pin(DigitalPin.P4, 0)
        pins.digital_write_pin(DigitalPin.P6, 0)
        basic.pause(200)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P4, 1)
        basic.pause(200)
basic.forever(on_forever)
