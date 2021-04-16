import json

archivoTemas = open('.alacritty.yml', 'x')
n = 0

coloresExtra = open('color-extra.txt')
temasExtra = open('themes-extra.txt')

archivoTemas.write(
    '#------------------------------------------------Themes-Extra\n\n')
archivoTemas.write(coloresExtra.read())

archivoTemas.write(
    '#------------------------------------------------Themes-Gogh\n\n')

with open('themes.json')as file:
    data = json.load(file)

for order in data['themes']:
    datos = (
        "#------------------------------------------------{}_".format(
            order.get('name')))

    datos += ("\n\n{}_: &{}_\n\n".format(
        order.get('name'), order.get('name')))

    datos += ("  primary:\n    background: \"{}\"\n".format(
        order.get('background')))

    datos += ("    foreground: \"{}\"".format(
        order.get('foreground')))

    datos += ("\n\n  cursor:\n    cursor:   \"{}\"".format(
        order.get('cursorColor')))

    datos += ("\n\n  normal:")

    datos += ("\n    black:    \"{}\"".format(order.get('black')))
    datos += ("\n    red:      \"{}\"".format(order.get('red')))
    datos += ("\n    green:    \"{}\"".format(order.get('green')))
    datos += ("\n    yellow:   \"{}\"".format(order.get('yellow')))
    datos += ("\n    blue:     \"{}\"".format(order.get('blue')))
    datos += ("\n    magenta:  \"{}\"".format(order.get('purple')))
    datos += ("\n    cyan:     \"{}\"".format(order.get('cyan')))
    datos += ("\n    white:    \"{}\"".format(order.get('white')))

    datos += ("\n\n  bright:")

    datos += ("\n    black:    \"{}\"".format(order.get('brightBlack')))
    datos += ("\n    red:      \"{}\"".format(order.get('brightRed')))
    datos += ("\n    green:    \"{}\"".format(order.get('brightGreen')))
    datos += ("\n    yellow:   \"{}\"".format(order.get('brightYellow')))
    datos += ("\n    blue:     \"{}\"".format(order.get('brightBlue')))
    datos += ("\n    magenta:  \"{}\"".format(order.get('brightPurple')))
    datos += ("\n    cyan:     \"{}\"".format(order.get('brightCyan')))
    datos += ("\n    white:    \"{}\"".format(order.get('brightWhite')))
    datos += ("\n\n")
    archivoTemas.write(datos)


archivoTemas.write(temasExtra.read())

archivoTemas.write(
    '#------------------------------------------------Themes-Gogh\n\n')

for x in data['themes']:
    n += 1
    if n == 6:
        n = 0
        datos += ("\n")
    else:
        datos += ("#--{}_\t".format(x.get('name')))

archivoTemas.write(datos)
