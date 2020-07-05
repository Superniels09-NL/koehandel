input.onButtonPressed(Button.A, function () {
    if (!(menu_poz == 0)) {
        menu_poz += -1
    }
})
input.onButtonPressed(Button.AB, function () {
    if (menu_poz == 0) {
        if (geld > prijs - 1) {
            koeien += 1
            geld += 0 - prijs
        } else {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
        }
    } else if (!(menu_poz == 0) && koeien > 0) {
        if (menu_poz < koeien + 1 && menu_poz > 0) {
            geld += randint(5, 20)
            koeien += -1
            menu_poz += -1
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (!(menu_poz == koeien + 2)) {
        menu_poz += 1
    }
})
let prijs = 0
let koeien = 0
let menu_poz = 0
let geld = 0
geld = 20
basic.forever(function () {
    if (menu_poz == 0) {
        prijs = randint(2, 9)
        basic.showNumber(prijs)
        while (!(input.buttonIsPressed(Button.AB)) && menu_poz == 0) {
            basic.pause(100)
        }
    }
})
basic.forever(function () {
    if (menu_poz == koeien + 1) {
        basic.showNumber(geld)
    }
})
basic.forever(function () {
    if (menu_poz == koeien + 2) {
        basic.showLeds(`
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            `)
    }
})
basic.forever(function () {
    if (!(menu_poz == 0)) {
        if (!(koeien == 0)) {
            if (!(menu_poz == koeien + 1) && !(menu_poz == koeien + 2)) {
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . # . . .
                    . . # # #
                    . . # . #
                    `)
            }
        }
    }
})
