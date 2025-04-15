def identificar_letra(letra):
    vogal = "aeiou"
    consoante = "bcdfghjklmnpqrstvxwyz"
    cv = 0
    cc = 0
    v = ""
    c = ""
    for l in letra:
        if l in vogal:
            v += l
            cv += 1
        elif l in consoante:
            c += l
            cc += 1
    return f"Na palavra {letra} tem {cv} vogais ({v}) e {cc} consoantes ({c})"

# Teste

print(identificar_letra("kennedh"))