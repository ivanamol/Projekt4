# """
# projekt4, task_manager.py: čtvrtý projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """


def hlavni_menu():
    while True:
        print(f"\nSprávce úkolů - Hlavní menu\n1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
        volba = input("Vyberte možnost (1-4): ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu")
            break
        else:
            print("Zadali jste neplatnou volbu, volba musí být od 1 do 4.")


def pridat_ukol():
    novy_ukol = {}
    while True:
        nazev_ukolu = input("\nZadejte název úkolu: ").strip()
        try:
            if nazev_ukolu:
                popis_ukolu = input("Zadejte popis úkolu: ").strip()
                if popis_ukolu:
                    novy_ukol = {"nazev": nazev_ukolu, "popis": popis_ukolu}
                    ukoly.append(novy_ukol)
                    print(f"Úkol '{novy_ukol["nazev"]}' byl přidán.")
                    break
                else:
                    raise ValueError("Zadali jste prázdný vstup do popisu úkolu.")
            else:
                raise ValueError("Zadali jste prázdný vstup do názvu úkolu.")
        except ValueError as e:
            print(e)


def zobrazit_ukoly():
    print("\nSeznam úkolů:")
    index = 1
    for ukol in ukoly:
        print(f"{index}. {ukol.get("nazev")} - {ukol.get("popis")}")
        index = index + 1


def odstranit_ukol():
    if not ukoly:
        print("\nNejsou zatím zadány žádné úkoly.")
        return
    while True:
        zobrazit_ukoly()
        index = input("\nZadejte číslo úkolu, který chcete odstranit: ")
        try:
            if not index.isdigit():
                raise ValueError("Není zadáno číslo úkolu - hodnota není kladné celé číslo.")
            if int(index) != 0:
                # potřebovala jsem ošetřit, že nepůjde zadat ani 0 - index je pak -1 a odstraní se poslední úkol, což je nechtěné
                nazev_odstranovaneho_ukolu = ukoly.pop(int(index) - 1)
                print(f"Úkol '{nazev_odstranovaneho_ukolu.get("nazev")}' byl odstraněn.")
                break
            else:
                raise ValueError("Zadané číslo úkolu neexistuje - nemůže být 0.")
        except IndexError:
            print("Zadané číslo úkolu neexistuje, je mimo rozsah.")
        except ValueError as e:
            print(e)


ukoly = []
if __name__ == "__main__":
    hlavni_menu()