# ECIR25 (Under Review): How Child-Friendly is Web Search? An Evaluation of Relevance vs. Harm

This repository contains the code and the data for our evaluation for child-safe search. We compared three general and three child-oriented web search engines based on a new non-English evaluation corpus of 50 queries spanning personal, political, educational, and entertainment information needs of children. For each query, we annotate the search engines’ top-10 results with respect to relevance and potential harm—a child-friendly result should be relevant but harmless.

## English  Version of our Dataset

In the version for Double-Blind review, we include a DeepL translation of our non-English evaluation corpus to English. Upon acceptance, we will release the original non-English corpus (language omitted for double-blind review) and the DeepL translations.

The structure of the dataset is:

- [data/en/documents.jsonl.gz](data/en/documents.jsonl.gz): The documents.
- [data/en/runs](data/en/runs): The run files for the six search engines (three general web search engines and three child-oriented search engines).
- [data/en/topics.xml](data/en/topics.xml): The topics, including the query, category, description, and narrative.
- [data/en/qrels-harm.txt](data/en/qrels-harm.txt): The qrel file containing the harm annotations.
- [data/en/qrels-relevance.txt](data/en/qrels-relevance.txt): The qrel file containing the relevance annotations.

### Citation

TBD.

