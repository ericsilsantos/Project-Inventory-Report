from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products):
        result = super().generate(products)
        all_products = Counter(prod["nome_da_empresa"] for prod in products)
        text_products = ""
        for empr in all_products:
            text_products += f"- {empr}: {all_products[empr]}\n"

        return (
            f"{result}\n"
            f"Produtos estocados por empresas:\n"
            f"{text_products}"
        )
