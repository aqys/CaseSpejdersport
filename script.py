with open("kontakter.txt", "a") as file:
    file.writelines(f"{q}: {input(f'{q}: ')}\n" for q in ["Fornavn", "Efternavn", "Email", "Telefon nr.", "Addresse"])