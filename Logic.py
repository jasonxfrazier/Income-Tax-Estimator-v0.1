import Brackets


class Calculation:
    def __init__(self, status: str, tax_inc: float, non_tax_inc: float) -> None:
        self.status: str = status
        self.taxable_income: float = tax_inc
        self.non_taxable_income: float = non_tax_inc

        self.rate: int
        self.tax_owed: float
        self.data: dict

    def _determine_rate(self) -> None:
        data: dict[str, any] = Brackets.bracket[self.status]
        for item in data:
            lower: int = item["range"][0]
            upper: int = item["range"][1]
            if self.taxable_income >= lower and self.taxable_income <= upper:
                self.rate = item["rate"]
                self.data = item

    def _determine_tax_owed(self) -> None:
        base: int = self.data["base"]
        tax: float = (self.taxable_income - self.data["range"][0]) * (self.data["rate"]/100)
        self.tax_owed = base + tax

    def Calculate(self) -> None:
        self._determine_rate()
        self._determine_tax_owed()

    def GetPostTax(self) -> float:
        return float(self.taxable_income + self.non_taxable_income - self.tax_owed)

    def GetPreTax(self) -> float:
        return float(self.taxable_income + self.non_taxable_income)

class Output():
    def __init__(self) -> None:
        self.text: str
    
    def SetText(self, text: str) -> None:
        self.text = text

    def GetText(self) -> str:
        return self.text
    
output = Output()
def calculate(data: dict[str,any]) -> str:
    status = data["status"]
    tax_inc = data["taxable_income"]
    non_tax_inc = data["non_taxable_income"]
    calc = Calculation(status, tax_inc, non_tax_inc)
    calc.Calculate()
    output.SetText(f"Before Taxes: ${calc.GetPreTax():.2f}\nTaxes Owed: ${calc.tax_owed:.2f}\nAfter Tax Total: ${calc.GetPostTax():.2f}")

