import random

def generuj_test(pocet_otazek):
    for i in range(pocet_otazek):
        cislo1 = random.randint(1, 10)
        cislo2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        if operator == '+':
            spravna_odpoved = cislo1 + cislo2
        elif operator == '-':
            spravna_odpoved = cislo1 - cislo2
        elif operator == '*':
            spravna_odpoved = cislo1 * cislo2

        otazka = f"{cislo1} {operator} {cislo2} = ?"
        yield otazka, spravna_odpoved

def zkontroluj_odpoved(otazka, odpoved):
    operator_ = otazka.split()[1]
    if operator_ == '+':
        spravna_odopved = int(otazka.split()[0].strip()) + int(otazka.split()[2].strip())
    elif operator_ == '-':
        spravna_odopved = int(otazka.split()[0].strip()) - int(otazka.split()[2].strip())
    elif operator_ == '*':
        spravna_odopved = int(otazka.split()[0].strip()) * int(otazka.split()[2].strip())

    return spravna_odopved == odpoved

def main():
    pocet_otazek = 5
    spravne = 0

    for otazka, spravna_odpoved in generuj_test(pocet_otazek):
        print(otazka)
        uzivatelska_odpoved = int(input("Vaše odpověď: "))

        if zkontroluj_odpoved(otazka, uzivatelska_odpoved):
            print("Správně!")
            spravne += 1
        else:
            print(f"Špatně. Správná odpověď byla: {spravna_odpoved}")

    print(f"Získali jste {spravne} bodů z {pocet_otazek} možných.")

if __name__ == "__main__":
    main()
