import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATE_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_status_counts = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.pep_status_counts[status] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DATE_FORMAT)
        path = BASE_DIR / f'results/status_summary_{time}.csv'

        with open(path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.pep_status_counts.items())

            total = sum(self.pep_status_counts.values())
            writer.writerow(['Total', total])
