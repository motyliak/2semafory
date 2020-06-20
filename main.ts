input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (ze1 == 1) {
        ze1 = 0
        zl1 = 1
        ce1 = 0
        ze2 = 0
        zl2 = 1
        ce2 = 1
    } else if (ce1 == 0 && zl1 == 1) {
        ze1 = 0
        zl1 = 0
        ce1 = 1
        ze2 = 1
        zl2 = 0
        ce2 = 0
    } else if (zl1 == 0 && ce1 == 1) {
        ce1 = 1
        zl1 = 1
        ze1 = 0
        ze2 = 0
        zl2 = 1
        ce2 = 0
    } else if (zl1 == 1 && ce1 == 1) {
        ce1 = 0
        zl1 = 0
        ze1 = 1
        ze2 = 0
        zl2 = 0
        ce2 = 1
    }
    
    if (chyba == 1) {
        ce1 = 1
        zl1 = 0
        ze1 = 0
        ze2 = 1
        zl2 = 0
        ce2 = 0
        chyba = 0
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    chyba = 1
})
let zl2 = 0
let ze2 = 0
let chyba = 0
let ce2 = 0
let ce1 = 0
let zl1 = 0
let ze1 = 0
ze1 = 1
zl1 = 0
ce1 = 0
ce2 = 1
chyba = 0
led.enable(false)
basic.forever(function on_forever() {
    if (chyba == 0) {
        pins.digitalWritePin(DigitalPin.P0, ze1)
        pins.digitalWritePin(DigitalPin.P1, zl1)
        pins.digitalWritePin(DigitalPin.P2, ce1)
        pins.digitalWritePin(DigitalPin.P3, ze2)
        pins.digitalWritePin(DigitalPin.P4, zl2)
        pins.digitalWritePin(DigitalPin.P6, ce2)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P3, 0)
        pins.digitalWritePin(DigitalPin.P4, 0)
        pins.digitalWritePin(DigitalPin.P6, 0)
        basic.pause(200)
        pins.digitalWritePin(DigitalPin.P1, 1)
        pins.digitalWritePin(DigitalPin.P4, 1)
        basic.pause(200)
    }
    
})
