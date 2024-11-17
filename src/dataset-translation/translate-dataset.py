#!/usr/bin/env python3
from tqdm import tqdm
import os
import gzip
import json


def deepl_translator():
    import deepl
    import os

    if 'DEEPL_AUTH_KEY' not in os.environ:
        print('Please provide an environment variable DEEPL_AUTH_KEY.')
        raise ValueError('Please provide an environment variable DEEPL_AUTH_KEY.')

    auth_key = os.environ['DEEPL_AUTH_KEY']
    return deepl.Translator(auth_key)

def load_topics():
    import xml.etree.ElementTree as ET
    tree = ET.parse('data/do-not-commit/topics.xml')
    ret = []
    for topic in tree.getroot().iter('topic'):
        ret += [{
            'number': topic.get('number'),
            'query': topic.find('query').text,
            'description': topic.find('description').text,
            'narrative': topic.find('narrative').text,
            'category': topic.find('category').text,
        }]

    return ret


def write_topics(topics, translator):
    if os.path.exists('data/en/topics.xml'):
        return

    with open('data/en/topics.xml', 'wt') as f:
        ret = []
        for topic in tqdm(topics):
            topic['query'] = translator.translate_text(topic['query'], source_lang="DE", target_lang="EN-US").text
            topic['description'] = translator.translate_text(topic['description'], source_lang="DE", target_lang="EN-US").text
            topic['narrative'] = translator.translate_text(topic['narrative'], source_lang="DE", target_lang="EN-US").text

            ret += ['''  <topic number="''' + str(topic['number']) + '''">
    <query>''' + topic['query'] + '''</query>
    <category>''' + topic['category'] + '''</category>
    <description>''' + topic['description'].replace('\\s', ' ').strip() + '''</description>
    <narrative>''' + topic['narrative'].replace('\\s', ' ').strip() + '''</narrative>
  </topic>
''']

        f.write('<topics>' + (''.join(ret)) + '</topics>')


def write_documents(translator):
    translated_docs = {}
    if os.path.exists('data/en/documents.jsonl.gz'):
        with gzip.open('data/en/documents.jsonl.gz', 'rt') as f:
            for l in f:
                l = json.loads(l)
                translated_docs[l['docno']] = l

    with gzip.open('data/do-not-commit/documents.jsonl.gz', 'rt') as f, gzip.open('data/en/documents.jsonl.gz', 'wt') as output:
        for l in tqdm(list(f)):
            l = json.loads(l)
            translated = {'docno': l['docno']}
            if l['docno'] in translated_docs:
                for k, v in translated_docs[l['docno']].items():
                    translated[k] = v
            for field_to_translate in ['snippet', 'title', 'main_content']:
                if field_to_translate not in translated:
                    if not l[field_to_translate] or len(l[field_to_translate]) == 0:
                        translated[field_to_translate] = ''
                    else:
                        translated[field_to_translate] = translator.translate_text(l[field_to_translate][:50000], source_lang="DE", target_lang="EN-US").text

            output.write(json.dumps(translated) + '\n')
            output.flush()


if __name__ == '__main__':
    topics = load_topics()
    translator = deepl_translator()

    write_topics(topics, translator)

    write_documents(translator)
