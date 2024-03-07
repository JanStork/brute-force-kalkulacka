import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Honziho brute force attack kalkulačka")
root.geometry("800x650")

# Function for calculation
def calculation(passwordLength, nTries, smallDigits, upperDigits, numbers, specials):
    nPossibilities = 0
    
    if smallDigits:
        nPossibilities += 26
    if upperDigits:
        nPossibilities += 26
    if numbers:
        nPossibilities += 10
    if specials:
        nPossibilities += 33
    
    nPossibilities **= passwordLength
    time_seconds = nPossibilities / nTries
    
    years = time_seconds // (365 * 24 * 3600)
    time_seconds %= (365 * 24 * 3600)
    days = time_seconds // (24 * 3600)
    time_seconds %= (24 * 3600)
    hours = time_seconds // 3600
    time_seconds %= 3600
    minutes = time_seconds // 60
    time_seconds %= 60
    seconds = round(time_seconds)
    
    return nPossibilities, years, days, hours, minutes, seconds



# GUI
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Brute force kalkulačka")
label.pack(pady=12, padx=10)

# checkboxes
checkboxSmallDigits = tk.BooleanVar(value=False)
checkboxUpperDigits = tk.BooleanVar(value=False)
checkboxNumbers = tk.BooleanVar(value=False)
checkboxSpecials = tk.BooleanVar(value=False)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Malá písmena (a-z)", variable=checkboxSmallDigits)
checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Velká písmena (A-Z)", variable=checkboxUpperDigits)
checkbox3 = customtkinter.CTkCheckBox(master=frame, text="Číslice (0-9)", variable=checkboxNumbers)
checkbox4 = customtkinter.CTkCheckBox(master=frame, text="Speciální znaky (*!@)", variable=checkboxSpecials)

checkbox1.pack(anchor='w', pady=2, padx=10)
checkbox2.pack(anchor='w', pady=2, padx=10)
checkbox3.pack(anchor='w', pady=2, padx=10)
checkbox4.pack(anchor='w', pady=2, padx=10)

# text entries
entryLabelNChars = customtkinter.CTkLabel(master=frame, text="Počet znaků hesla:")
entryLabelNChars.pack(pady=5, padx=10)

entryTextNChars = customtkinter.CTkEntry(master=frame)
entryTextNChars.pack(pady=2.5, padx=10)

entryLabelTriesS = customtkinter.CTkLabel(master=frame, text="Počet pokusů/s:")
entryLabelTriesS.pack(pady=5, padx=10)

entryTextTriesS = customtkinter.CTkEntry(master=frame)
entryTextTriesS.pack(pady=2.5, padx=10)

# labels
labelLenghtCalc = customtkinter.CTkLabel(master=frame, text="Brute force attack bude trvat")
labelLenghtCalc.pack(padx=10)

labelNOperations = customtkinter.CTkLabel(master=frame, text="Proběhne přes  pokusů")
labelNOperations.pack(padx=10)

# button
def calculate():
    passwordLength = int(entryTextNChars.get())
    nTries = int(entryTextTriesS.get())
    smallDigits = checkboxSmallDigits.get()
    upperDigits = checkboxUpperDigits.get()
    numbers = checkboxNumbers.get()
    specials = checkboxSpecials.get()
    
    nPossibilities, years, days, hours, minutes, seconds = calculation(passwordLength, nTries, smallDigits, upperDigits, numbers, specials)
    
    time_str = f"{int(years)} let {int(days)} dní {int(hours)} hodin {int(minutes)} minut {int(seconds)} sekund"
    
    labelLenghtCalc.configure(text=f"Brute force attack bude trvat {time_str}")
    labelNOperations.configure(text=f"Proběhne přes {nPossibilities:,.0f} pokusů".replace(",", " "))


button = customtkinter.CTkButton(master=frame, text="Vypočítej", command=calculate)
button.pack(pady=10)

root.mainloop()
