# ECIR25: How Child-Friendly is Web Search? An Evaluation of Relevance vs. Harm

This repository contains the code and the data for our evaluation of web search child-friendliness. We compare three general and three child-oriented web search engines based on a new non-English evaluation corpus of 50 queries spanning personal, political, educational, and entertainment information needs of children. For each query, we annotate the search engines’ top-10 results with respect to relevance and potential harm: a child-friendly result should be relevant but harmless. The dataset is in the [data](data) directory and additionally hosted on [Zenodo](https://zenodo.org/records/14684724).

If you use the kid-FRIEND dataset in your research, please cite:

```
TBD.
```

## German Version of our Dataset

TBD

## English  Version of our Dataset

In the version for double-blind review, we include a DeepL translation of our non-English evaluation corpus to English. Upon acceptance, we will release the original non-English corpus (language omitted for double-blind review) and the DeepL translations.

The structure of the dataset is:

- [data/en/documents.jsonl.gz](data/en/documents.jsonl.gz): The documents.
- [data/en/runs](data/en/runs): The run files for the six search engines (three general web search engines and three child-oriented search engines).
- [data/en/topics.xml](data/en/topics.xml): The topics, each including a query, a category, a description, and a narrative.
- [data/en/qrels-harm.txt](data/en/qrels-harm.txt): The qrel file containing the harm annotations.
- [data/en/qrels-relevance.txt](data/en/qrels-relevance.txt): The qrel file containing the relevance annotations.

## Unit Tests

Run `pytest` to run the unit tests (that mainly test the ir_datasets integration).

## Integration to ir_datasets

This repository provides an integration to [ir_datasets](https://ir-datasets.com/). To use it, please install the kid-FRIEND dataset via the ir_datasets plugin:

```
pip3 install -e .
```

Afterwards, you can load and process the ir_dataset via:

```
from kid_friend import ir_datasets

dataset = ir_datasets.load('kidFRIEND/en/relevance') # Alternatively kidFRIEND/en/harm

for query in dataset.queries_iter():
    print(query)

for doc in dataset.docs_iter():
    print(doc)

for qrel in dataset.qrels_iter():
    print(qrel)
```

### Citation

TBD.

