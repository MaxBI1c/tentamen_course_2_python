import matplotlib.pyplot as plt


def file_open():
    """leest de bestanden die de gebruiker geeft
    input:

    file: - file
    bestand: - file

    output:

    gff3_file - list
    fasta_seq - list

    """
    try:
        # file vraagt de gebruiker om de naam van een bestand in te voeren dat de gebruiker wil openen.
        file = input("please enter a file you'd like to open")
        # bestand vraagt de gebruiker om de naam van een bestand in te voeren dat de gebruiker wil openen.
        bestand = input("please enter another file you'd like to open")
        # gff3_file is de lijst die de inhoud van het gff3 bestand bevat.
        gff3_file = []
        # fasta_header is de lijst die de headers van het fasta bestand bevat.
        fasta_header = []
        # fasta_seq is de lijst die de sequenties van de headers van het fasta bestand bevat.
        fasta_seq = []
        # fasta_sequence is de variabele waarin de sequentie van het fasta bestand tijdelijk in wordt opgeslagen.
        fasta_sequence = ""
        # Controleert of .GFF3 in zowel de variabele file als in de variabele bestand zit.
        if ".GFF3" in file and bestand:
            # print statement dat uitlegt dat de twee ingevoerde bestanden een verschillend datatype moeten zijn.
            print("you can't open two files of the same datatypePlease enter a different file to open ")
        # Controleert of .FAA in zowel de variabele file als in de variabele bestand zit.
        elif "FAA" in file and ".FAA" in bestand:
            # print statement dat uitlegt dat de twee ingevoerde bestanden een verschillend datatype moeten zijn.
            print("you can't open two files of the same datatypePlease enter a different file to open ")
        # Controleert of .FASTA in zowel de variabele file als in de variabele bestand zit.
        elif ".FASTA" in file and ".FASTA" in bestand:
            # print statement dat uitlegt dat de twee ingevoerde bestanden een verschillend datatype moeten zijn.
            print("you can't open two files of the same datatypePlease enter a different file to open ")
        # controleert of er .GFF3 in de naam van de variabele file zit.
            # moet eerst nog een ">" toevoegen aan het einde van het bestand
            if ".GFF3" in file:
            # opent de ingevoerde naam bij de variabele file als file.
            with open(file) as file:
                # gaat voor elke regel in file splitten op de tab.
                for line in file:
                    # split voor elke line op de tab door middel van split waardoor die regel in een lijst komt.
                    regel = line.split("\t")
                    # voegt de lijst regel toe aan de lijst gff3_file.
                    gff3_file.append(regel)
        # controleert of er .GFF3 in de naam van de variabele bestand zit.
        elif ".GFF3" in bestand:
            # opent de ingevoerde naam bij de variabele file als file.
            with open(bestand) as file:
                # gaat voor elke regel in file splitten op de tab.
                for line in file:
                    # split voor elke line op de tab door middel van split waardoor die regel in een lijst komt.
                    regel = line.split("\t")
                    # voegt de lijst regel toe aan de lijst gff3_file.
                    gff3_file.append(regel)
        # controleert of er .FAA of .FASTA in de naam van de variabele file zit.
        elif ".FAA" in file or ".FASTA" in file:
            # opent het bestand file.
            open(file, "w")
            # voegt een groter dan teken toe aan het einde van het bestand file.
            file.write(">")
            file.close()
            # opent de ingevoerde naam bij de variabele file als bestand.
            with open(file, "r") as bestand:
                # gaat voor elke regel in bestand door de loop kijken of het een groter dan teken tegenkomt.
                for line in bestand:
                    # controleert of er een groter dan teken in line zit.
                    if ">" in line:
                        # voegt line toe aan de lijst fasta_header.
                        fasta_header.append(line)
                        # gaat over elke letter in de variabele fasta_sequence
                        for item in fasta_sequence:
                            # voegt elke letter in de variabele fasta_sequence apart toe aan de lijst fasta_seq
                            fasta_seq.append(item)
                        # maakt de variabele fasta_sequence leeg.
                        fasta_sequence = ""
                    # als er geen groter dan teken in line zit dan gaat de code in het else statement.
                    else:
                        # verwijdert enters uit line.
                        line.replace("\n")
                        # voegt line toe aan de variabele fasta_sequence.
                        fasta_sequence += line
        # controleert of er .FAA of .FASTA in de naam van de variabele file zit.
        elif ".FAA" in bestand or ".FASTA" in bestand:
            # opent het bestand bestand.
            open(bestand, "w")
            # voegt een groter dan teken toe aan het einde van het bestand bestand.
            bestand.write(">")
            bestand.close()
            # opent de ingevoerde naam bij variabele bestand als bestand.
            with open(bestand, "r") as bestand:
                # gaat voor elke regel in bestand door de loop kijken of het een groter dan teken tegenkomt.
                for line in bestand:
                    # controleert of er een groter dan teken in line zit.
                    if ">" in line:
                        # voegt line toe aan de lijst fasta_header.
                        fasta_header.append(line)
                        # gaat over elke letter in de variabele fasta_sequence
                        for item in fasta_sequence:
                            # voegt elke letter in de variabele fasta_sequence apart toe aan de lijst fasta_seq
                            fasta_seq.append(item)
                        # maakt de variabele fasta_sequence leeg.
                        fasta_sequence = ""
                    # als er geen groter dan teken in line zit dan gaat de code in het else statement.
                    else:
                        # verwijdert enters uit line.
                        line.replace("\n")
                        # voegt line toe aan de variabele fasta_sequence.
                        fasta_sequence += line
        else:
            print("The files that you are looking for don't exist")
        return fasta_seq, gff3_file
    except FileNotFoundError:
        print("The file you are looking for doesn't exist")
    except ValueError:
        print("The variable isn't the right type it must be a string ")

def seq_controle(fasta_seq, gff3_file):
    """kijkt in de lijst gff3_file naar de locatie van de genen en voegt de sequentie toe aan het fasta bestand
    input:

    fasta_seq: - lijst
    gff3_file: - lijst

    output:

    tentamen_course_2.FASTA: - file

    """
    try:
        # verwijderd de eerste 2 regels uit de lijst gff3_file.
        gff3_file.remove([0,2])
        # de variabele index heeft de waarde 0.
        index = 0
        # opent het FASTA bestand tentamen_course_2 om in te schrijven als fasta_file.
        with open("tentamen_course_2.FASTA", "w") as fasta_file:
            # voor elk item in de lijst fasta_seq gaat door de loop.
            for items in fasta_seq:

                #if gff3_file[ind][2] not in type_list:

                # als het derde item van een regel in de lijst gff3_file gene is gaat het in het if statement.
                if gff3_file[index][2] == "gene":
                    # start_index pakt de start positie van het gen door te kijken op positie 4 in de lijst gff3_file en
                    # van die waarde 1 af te halen
                    start_index = gff3_file[index][3] - 1
                    # end_index pakt de stop positie van het gen door te kijken op positie 5 in de lijst gff3_file en
                    # van die waarde wordt 1 afgetrokken
                    end_index = gff3_file[index][4] -1
                    # elke letter in de lijst fasta_seq die tussen de start en stop positie zit van de genen uit de
                    # gff3_file worden appart toegevoegd aan het bestand tentamen_course_2.FASTA.
                    for letter in range(start_index, end_index):
                        # elke letter in de lijst fasta_seq die tussen de start en stop positie van het gen zit
                        # wordt appart toegevoegd aan het bestand tentamen_course_2.FASTA
                        fasta_file.write(fasta_seq[letter])
                    # de index wordt verhoogd met 1.
                    index+=1
                else:
                    # de index wordt verhoogd met 1.
                    index += 1
                    print("This index is not equel to gene")
        return gff3_file
    except IndexError:
        print("The index is too big for this list which is why this loop stopped")
    except ValueError:
        print("It is not possible to subtract 1 from a string")
def graphic(gff3_file):
    """kijkt welke datatypes in de lijst gff3_file voorkomen en maakt aan de hand daarvan een taart diagram
    input:

    gff3_file - list

    output:

    piechart
    """

    try:
        # lijst waarin de verschillende types voorkomen die voorkomen in de lijst gff3_file.
        type_list = []
        #
        # kan momenteel beter de regular expressions laten zitten en gew de taart diagram maken. moet verder kijken wat de error is als iets leeg is
        # de variabele index_type heeft de waarde 0
        index_type = 0

        # voor elke regel in de lijst gff3_file wordt gekeken of het type al in de type_list list zit.
        for items in gff3_file:
            # als de gff3_file index_type op index 2 niet in de type_list list zit dan wordt dat type toegevoegd aan de
            # type_list.
            if gff3_file[index_type][2] not in type_list:
                # voegt het type dat nog niet in de type_list list zit toe aan de type_list
                type_list.append(gff3_file[index_type][2])
                # index_type wordt met een verhoogd.
                index_type +=1
            # als de gff3_file index_type op index 2 wel in de type_list list zit gaat index_type met 1 omhoog.
            else:
                # de variabele index_type gaat met 1 omhoog
                index_type += 1
        # variabele waarin wordt opgeslagen wat de index van de list type_list is.
        index_type_diagram = 0
        # variabele waarin wordt opgeslagen wat de index van het gff3_file is.
        index_gff3_file = 0
        # variabele waarin wordt opgeslagen hoevaak elk type voorkomt deze is nu nog gelijk aan 0.
        amount_type = 0
        # lijst die opslaat hoevaak elk type voorkomt in de lijst gff3_file.
        list_type_diagram = []
        # voor elk item in de lijst list_type_diagram gaat door een loop.
        for items in type_list:
            # amount_type is gelijk aan 0.
            amount_type = 0
            # index_gff3_file is gelijk aan 0.
            index_gff3_file = 0
            # voor elk item in de lijst gff3_file gaat door een loop.
            for items in gff3_file:
                # als gff3_file index_gff3_file index 2 gelijk is aan type_list index_type_diagram worden amount_type en
                # index_gff3_file met 1 verhoogd.
                if gff3_file[index_gff3_file][2] == type_list[index_type_diagram]:
                    # de variabele amount_type wordt met 1 verhoogd.
                    amount_type += 1
                    # de variabele index_gff3_file wordt met 1 verhoogd
                    index_gff3_file += 1
                # als gff3_file index_gff3_file index 2 niet gelijk is aan type_list index_type_diagram wordt
                # index_gff3_file met 1 verhoogd.
                else:
                    # de variabele index_gff3_file wordt met 1 verhoogd.
                    index_gff3_file += 1
                # de variabele amount_type wordt toegevoegd aan de lijst index_type_diagram.
                index_type_diagram.append(amount_type)

        # creeert voor elk item in lijst een deel van de taart.
        fig1, ax1 = plt.subplots()
        # maakt de taartdiagram aan
        ax1.pie(list_type_diagram, labels= type_list, autopct= "%1.1f%%", startangle= 0)
        # zorgt dat zeker is dat de taart diagram een cirkel is
        ax1.axis("equal")
        # laat de taart diagram zien
        plt.show()
    except IndexError:
        print("The index is too big for this list which is why this loop stopped")
    except NameError:
        print("variable/list is not defined")
    except ImportError:
        print("The importet library isn't correct/ the good version")
    except ValueError:
        print("The lists in the pie chart must be of equel length")

if __name__ == "__main__":
    fasta_seq, gff3_file =file_open()
    seq_controle(fasta_seq, gff3_file)
    graphic(gff3_file)
