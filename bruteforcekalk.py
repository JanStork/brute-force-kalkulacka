import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x650")

# function
# def calculation(passwordLength, charLength):

# GUI
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Brute force kalkulačka")
label.pack(pady=12, padx=10)

# Checkboxes for options
checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Malá písmena (a-z)")
checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Velká písmena (A-Z)")
checkbox3 = customtkinter.CTkCheckBox(master=frame, text="Číslice (0-9)")
checkbox4 = customtkinter.CTkCheckBox(master=frame, text="Speciální znaky (*!@)")

checkbox1.pack(anchor='w', pady=2, padx=10)
checkbox2.pack(anchor='w', pady=2, padx=10)
checkbox3.pack(anchor='w', pady=2, padx=10)
checkbox4.pack(anchor='w', pady=2, padx=10)

# Entry textbox
entryLabelNChars = customtkinter.CTkLabel(master=frame, text="Počet znaků hesla:")
entryLabelNChars.pack(pady=5, padx=10)

entryTextTriesS = customtkinter.CTkEntry(master=frame)
entryTextTriesS.pack(pady=2.5, padx=10)

entryLabelTriesS = customtkinter.CTkLabel(master=frame, text="Počet pokusů/s:")
entryLabelTriesS.pack(pady=5, padx=10)

entryTextTriesS = customtkinter.CTkEntry(master=frame)
entryTextTriesS.pack(pady=2.5, padx=10)

# Button
button = customtkinter.CTkButton(master=frame, text="Vypočítej", command=calculation)
button.pack(pady=10)

# Labels
labelLenghtCalc = customtkinter.CTkLabel(master=frame, text="Brute force attack bude trvat")
labelLenghtCalc.pack(padx=10)

labelNOperations = customtkinter.CTkLabel(master=frame, text="Proběhne přes XXX pokusů")
labelNOperations.pack(padx=10)




root.mainloop()