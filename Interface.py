import customtkinter as ctk
import Logic

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("718x450")
        self.title("Tax Estimation")
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)

        self.filing_status = Filing_Status(self)
        self.filing_status.grid(row=0, column=0, padx=5, sticky="n")

        self.input_frame1 = Input(self, text="Earner 1")
        self.input_frame1.grid(row=1, column=0, padx=5, sticky="n")
        self.input_frame2 = Input(self, text="Earner 2")
        self.input_frame2.grid(row=1, column=1, padx=5, sticky="n")

        self.output_box = Output_Box(self)
        self.output_box.grid(row=0, column=2, rowspan=10, padx=5, sticky="n")

        self.button = ctk.CTkButton(self, text="Calculate", command=self._send_data)
        self.button.grid(row=2, column=0, columnspan=2, sticky="n")

    def _send_data(self) -> None:
        try:
            taxable1 = int(self.input_frame1.label_input1.entry.get())
        except ValueError:
            taxable1 = 0
        try:    
            nontax1 = int(self.input_frame2.label_input1.entry.get())
        except ValueError:
            nontax1 = 0
        try:
            taxable2 = int(self.input_frame2.label_input1.entry.get())
        except ValueError:
            taxable2 = 0
        try:
            nontax2 = int(self.input_frame2.label_input2.entry.get())
        except ValueError:
            nontax2 = 0
        status = self.filing_status.status.get()

        taxable_income: int = taxable1 + taxable2
        non_taxable_income: int = nontax1 + nontax2

        Logic.calculate({"status": status, "taxable_income": taxable_income, "non_taxable_income": non_taxable_income})
        self.output_box.box.configure(state="normal")
        self.output_box.box.delete("1.0", "end")
        self.output_box.box.insert("end", Logic.output.GetText())
        self.output_box.box.configure(state="disabled")

class Input(ctk.CTkFrame):
    def __init__(self, master, text: str):
        super().__init__(master)
        self.text = ctk.CTkLabel(self, text=text)
        self.text.grid(row=0, column=0)
        
        self.label_input1 = Label_Input(self, title="Taxable Income")
        self.label_input1.grid(row=1, column=0, pady=2)
        self.label_input2 = Label_Input(self, title="Non Taxable Income")
        self.label_input2.grid(row=2, column=0, pady=2, padx=2)

class Label_Input(ctk.CTkFrame):
    def __init__(self, master, title: str):
        super().__init__(master)
        self.configure(bg_color="transparent", fg_color="transparent")

        self.label = ctk.CTkLabel(self, text=title)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry = ctk.CTkEntry(self, placeholder_text="-")
        self.entry.grid(row=1, column=0)

class Output_Box(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.text = ctk.CTkLabel(self, text="Output")
        self.text.grid(row=0, column=0)

        self.box = ctk.CTkTextbox(self, width=400, height=400, state="disabled")
        self.box.grid(row=1, column=0)

class Filing_Status(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.status_label = ctk.CTkLabel(self, text="Filing Status")
        self.status_label.grid(row=0, column=0, sticky="n")
        self.status = ctk.CTkComboBox(self, values=["single", "married_separate", "head_of_household", "married_joint"])
        self.status.grid(row=1, column=0, sticky="n")

