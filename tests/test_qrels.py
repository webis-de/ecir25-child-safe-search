import unittest

def load_qrels_as_map(file):
    ret = {}
    errors = []
    with open(file) as f:
        for l in f:
            topic, q0, docid, score = l.split()
            if topic not in ret:
                ret[topic] = {}
            if docid in ret[topic]:
                errors += [f"{topic} - {docid}"]
            ret[topic][docid] = score
    if len(errors) != 0:
        for error in errors:
            print(error)
        raise ValueError(errors)


class TestDataset(unittest.TestCase):
    def test_de_harm_qrels_have_no_duplicates(self):
        load_qrels_as_map("data/de/qrels/qrels-harm.txt")

    def test_en_harm_qrels_have_no_duplicates(self):
        load_qrels_as_map("data/en/qrels/qrels-harm.txt")

    def test_de_rel_qrels_have_no_duplicates(self):
        load_qrels_as_map("data/de/qrels/qrels-relevance.txt")

    def test_en_rel_qrels_have_no_duplicates(self):
        load_qrels_as_map("data/en/qrels/qrels-relevance.txt")
