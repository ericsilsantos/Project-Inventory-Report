from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(self, path, relatory_type):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                arquivo = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                    )

            if relatory_type == 'simples':
                return SimpleReport.generate(arquivo)
            elif relatory_type == 'complete':
                return CompleteReport.generate(arquivo)
