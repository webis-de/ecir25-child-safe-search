import unittest
from kid_friend import ir_datasets

# One relevance entry
REL_QREL_EXAMPLE = "TrecQrel(query_id='50', doc_id='e4adf192c95d4114a131174f6df262dd', relevance=2, iteration='0')"

# One harm entry
HARM_QREL_EXAMPLE = "TrecQrel(query_id='50', doc_id='fe7fffdae20e4521a223bf749a9d3877', relevance=2, iteration='0')"

class TestDataset(unittest.TestCase):
    def test_topics_for_harm_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/harm')
        topics = {i.query_id: i.default_text() for i in dataset.queries_iter()}
        
        self.assertEqual(50, len(topics))
        self.assertEqual('Does she like me?', topics['50'])

    def test_topics_for_relevance_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/relevance')
        topics = {i.query_id: i.default_text() for i in dataset.queries_iter()}
        
        self.assertEqual(50, len(topics))
        self.assertEqual('Does she like me?', topics['50'])

    def test_qrels_for_harm_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/harm')
        qrels = set([str(i) for i in dataset.qrels_iter()])

        self.assertEqual(116850, len(qrels))

        self.assertTrue(HARM_QREL_EXAMPLE in qrels)
        self.assertTrue(REL_QREL_EXAMPLE not in qrels)

    def test_qrels_for_relevance_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/relevance')
        qrels = set([str(i) for i in dataset.qrels_iter()])

        self.assertEqual(2303, len(qrels))

        self.assertTrue(HARM_QREL_EXAMPLE not in qrels)
        self.assertTrue(REL_QREL_EXAMPLE in qrels)

    def test_documents_for_harm_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/harm')
        docs_store = dataset.docs_store()
        docs_count = len([i for i in dataset.docs_iter()])
        example_doc = docs_store.get('d339f2b9c94d4982a7c96d2a682911b7')

        self.assertEqual(2385, docs_count)
        self.assertTrue(example_doc.snippet.startswith('At the beginning the series was called Delphin'))
        self.assertEqual(example_doc.title, '[PDF] Small Dolphin Art Books by Kurt Dröge eBook | Perlego')
        self.assertTrue(example_doc.default_text().startswith('[PDF] Small Dolphin Art Books by Kurt Dröge eBook | Perlego'))

    def test_documents_for_relevance_dataset(self):
        dataset = ir_datasets.load('kidFRIEND/en/relevance')
        docs_store = dataset.docs_store()
        docs_count = len([i for i in dataset.docs_iter()])
        example_doc = docs_store.get('d339f2b9c94d4982a7c96d2a682911b7')

        self.assertEqual(2385, docs_count)
        self.assertTrue(example_doc.snippet.startswith('At the beginning the series was called Delphin'))
        self.assertEqual(example_doc.title, '[PDF] Small Dolphin Art Books by Kurt Dröge eBook | Perlego')
        self.assertTrue(example_doc.default_text().startswith('[PDF] Small Dolphin Art Books by Kurt Dröge eBook | Perlego'))

