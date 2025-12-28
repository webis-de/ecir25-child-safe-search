# ECIR25: How Child-Friendly is Web Search? An Evaluation of Relevance vs. Harm

This repository contains the code and the data for our evaluation of web search child-friendliness. We compare three general and three child-oriented web search engines based on a new non-English evaluation corpus of 50 queries spanning personal, political, educational, and entertainment information needs of children. For each query, we annotate the search engines’ top-10 results with respect to relevance and potential harm: a child-friendly result should be relevant but harmless. The dataset is in the [data](data) directory and additionally hosted on [Zenodo](https://zenodo.org/records/18076554).

If you use the kid-FRIEND dataset in your research, please cite:

```
@InProceedings{froebe:2025d,
  address =                  {Cham, Switzerland},
  author =                   {Maik Fr{\"o}be and Sophie Charlotte Bartholly and Matthias Hagen},
  booktitle =                {Advances in Information Retrieval. 47th European Conference on IR Research (ECIR 2025)},
  doi =                      {10.1007/978-3-031-88717-8\_16},
  editor =                   {Claudia Hauff and Craig Macdonald and Dietmar Jannach and Gabriella Kazai and Franco Maria Nardini and Fabio Pinelli and Fabrizio Silvestri and Nicola Tonellotto},
  month =                    apr,
  pages =                    {214--222},
  publisher =                {Springer Nature},
  series =                   {Lecture Notes in Computer Science},
  site =                     {Lucca, Italy},
  title =                    {{How Child-Friendly is Web Search? An Evaluation of Relevance vs. Harm}},
  volume =                   15575,
  year =                     2025
}
```

## German Version of our Dataset

The original version of our dataset is in German, we include a English translation for simplified usage as well.
The structure of the dataset is:

- [data/de/inputs/documents.jsonl.gz](data/en/inputs/documents.jsonl.gz): The documents.
- [data/de/runs](data/de/runs): The run files for the six search engines (three general web search engines and three child-oriented search engines).
- [data/de/inputs/topics.xml](data/de/inputs/topics.xml): The topics, each including a query, a category, a description, and a narrative.
- [data/de/qrels/qrels-harm.txt](data/de/qrels/qrels-harm.txt): The qrel file containing the harm annotations.
- [data/de/qrels/qrels-relevance.txt](data/de/qrels/qrels-relevance.txt): The qrel file containing the relevance annotations.


## English  Version of our Dataset

We include a DeepL translation of our non-English evaluation corpus to English. Upon acceptance, we will release the original non-English corpus (language omitted for double-blind review) and the DeepL translations.

The structure of the dataset is:

- [data/en/inputs/documents.jsonl.gz](data/en/inputs/documents.jsonl.gz): The documents.
- [data/en/runs](data/en/runs): The run files for the six search engines (three general web search engines and three child-oriented search engines).
- [data/en/inputs/topics.xml](data/en/inputs/topics.xml): The topics, each including a query, a category, a description, and a narrative.
- [data/en/qrels/qrels-harm.txt](data/en/qrels/qrels-harm.txt): The qrel file containing the harm annotations.
- [data/en/qrels/qrels-relevance.txt](data/en/qrels/qrels-relevance.txt): The qrel file containing the relevance annotations.

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

