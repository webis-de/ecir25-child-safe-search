#!/usr/bin/env python3
from tqdm import tqdm

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
    tree = ET.parse('data/de/topics.xml')
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


topics = load_topics()
translator = deepl_translator()

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
