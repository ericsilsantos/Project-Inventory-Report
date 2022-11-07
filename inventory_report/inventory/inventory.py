from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(self, path, relatory_type):
        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                arquivo = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )
            elif path.endswith(".json"):
                arquivo = json.load(file)
            else:
                arquivo = xmltodict.parse(file.read())["dataset"]["record"]

            if relatory_type == 'simples':
                return SimpleReport.generate(arquivo)
            elif relatory_type == 'completo':
                return CompleteReport.generate(arquivo)
