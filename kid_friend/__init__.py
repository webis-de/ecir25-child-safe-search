import ir_datasets
from ir_datasets.datasets.base import Dataset
from ir_datasets.formats.trec import TrecQrels, TrecXmlQueries, BaseDocs
from ir_datasets.util.fileio import StringFile
from typing import NamedTuple
import json
import gzip
import pathlib
BASE_DIR = pathlib.Path(__file__).parent.parent.resolve()


class KidFriendDoc(NamedTuple):
    doc_id: str
    title: str
    snippet: str
    url: str
    main_content: str
    def default_text(self):
        """
        title and text
        """
        return f'{self.title} {self.snippet} {self.main_content}'


class KidFriendDocs(BaseDocs):
    def __init__(self, document_dictionary):
        self.document_dictionary = document_dictionary

    def docs_iter(self):
        for doc in self.document_dictionary.values():
            yield KidFriendDoc(doc_id=doc['docno'], title=doc['title'], snippet=doc['snippet'], url=doc.get('url'), main_content=doc['main_content'])

    def docs_store(self):
        ret = {}
        for doc in self.document_dictionary.values():
            ret[doc['docno']] = KidFriendDoc(doc_id=doc['docno'], title=doc['title'], snippet=doc['snippet'], url=doc.get('url'), main_content=doc['main_content'])

        return ret


def load_documents():
    ret = {}
    with gzip.open(BASE_DIR / 'data' / 'en' / 'documents.jsonl.gz', 'rt') as f:
        for l in f:
            l = json.loads(l)
            ret[l['docno']] = l
    return ret

def string_file(resource):
    return StringFile(open(BASE_DIR / 'data' / 'en' / resource, 'r').read())

kid_friend_documents = load_documents()

QRELS_DEFS = {
    'harm': {
        0: 'The document is appropriate for children.',
        1: 'The document not perfectly approprate for children, it is too complex but does not contain content of any of the four harmful categories defined by Coleman.',
        2: 'The document is not appropriate for children and contains content from the harmful Coleman categories.',
    },
    'relevance': {
        0: 'The document is not relevant.',
        1: 'The document is on the topic of the information need but does not directly answer the information need.',
        2: 'The document answers the information need directly.',
    }
}

print(len(kid_friend_documents))

def load_qrels(qrels_type):
    pass

for qrel_type in ['harm', 'relevance']:
    qrels = TrecQrels(string_file(f'qrels-{qrel_type}.txt'), QRELS_DEFS[qrel_type])
    queries = TrecXmlQueries(string_file(f'topics.xml'), qtype_map={'query': 'title', 'description': 'description', 'narrative': 'narrative'})
    docs = KidFriendDocs(kid_friend_documents)
    scoreddocs = None

    dataset = Dataset(docs, queries, qrels, scoreddocs)
    dataset.metadata = None
    
    ir_datasets.registry.register(f'kidFRIEND/en/{qrel_type}', dataset)

