def dezimal_zu_hexadezimal(dezimal):
    if dezimal == 0:
        return "0x0"
    hexadezimal = ""
    while dezimal > 0:
        rest = dezimal % 16
        if rest < 10:
            hexadezimal = chr(48 + rest) + hexadezimal
        else:
            hexadezimal = chr(55 + rest) + hexadezimal
        dezimal = dezimal // 16
    return "0x" + hexadezimal

# Benutzerinput
eingabe = input("Bitte geben Sie eine Dezimalzahl ein: ")

# Umwandlung der Eingabe in eine Ganzzahl
try:
    dezimalzahl = int(eingabe)
    hexadezimalzahl = dezimal_zu_hexadezimal(dezimalzahl)
    print(f"Dezimal: {dezimalzahl} => Hexadezimal: {hexadezimalzahl}")
except ValueError:
    print("Bitte geben Sie eine gültige Ganzzahl ein.")