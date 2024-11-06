#!/usr/bin/env python3

def deepl_translator():
    import deepl
    import os

    if 'DEEPL_AUTH_KEY' not in os.environ:
        print('Please provide an environment variable DEEPL_AUTH_KEY.')
        raise ValueError('Please provide an environment variable DEEPL_AUTH_KEY.')

    auth_key = os.environ['DEEPL_AUTH_KEY']
    return deepl.Translator(auth_key)

translator = deepl_translator()
input_text = "Hallo Welt!"
result = translator.translate_text(input_text, source_lang="DE", target_lang="EN-US")
print(input_text, '->', result.text)
