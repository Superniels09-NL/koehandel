def on_button_pressed_a():
    global menu_poz
    if not (menu_poz == 0):
        menu_poz += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global koeien, geld, menu_poz
    if menu_poz == 0:
        if geld > prijs - 1:
            koeien += 1
            geld += 0 - prijs
        else:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
    else:
        if not (menu_poz == 0) and koeien > 0:
            if menu_poz < koeien + 1 and menu_poz > 0:
                geld += randint(5, 20)
                koeien += -1
                menu_poz += -1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global menu_poz
    if not (menu_poz == koeien + 2):
        menu_poz += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

koeien = 0
prijs = 0
menu_poz = 0
geld = 0
geld = 20

def on_forever():
    global prijs
    if menu_poz == 0:
        prijs = randint(2, 9)
        basic.show_number(prijs)
        while not (input.button_is_pressed(Button.AB)) and menu_poz == 0:
            basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    if menu_poz == koeien + 1:
        basic.show_number(geld)
basic.forever(on_forever2)

def on_forever3():
    if menu_poz == koeien + 2:
        basic.show_leds("""
            # . # . #
            . # . # .
            # . # . #
            . # . # .
            # . # . #
            """)
basic.forever(on_forever3)

def on_forever4():
    if not (menu_poz == 0):
        if not (koeien == 0):
            if not (menu_poz == koeien + 1) and not (menu_poz == koeien + 2):
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . # . . .
                    . . # # #
                    . . # . #
                    """)
basic.forever(on_forever4)

