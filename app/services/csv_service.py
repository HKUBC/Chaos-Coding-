import csv

from services.data_service import DataService

class CSVService(DataService):
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_data(self) -> list[dict]:
        try:
            with open(self.csv_path, 'r', newline='') as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.csv_path} not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}") from e