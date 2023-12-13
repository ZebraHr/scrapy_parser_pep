from pathlib import Path


BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent

DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
    }


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
