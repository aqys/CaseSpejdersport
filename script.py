with open("kontakter.txt", "a") as file:
    questions = ["Fornavn", "Efternavn", "Email", "Telefon nr.", "Addresse"]
    for q in questions:
        file.write(f"{q}: {input(f'{q}: ')}\n")