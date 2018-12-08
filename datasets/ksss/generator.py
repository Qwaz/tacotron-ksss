import json
import unicodedata

KSSS_DIRECTORY = './datasets/ksss'

result_dict = {}

with open('{}/KoreanSingleSpeakerSpeech/transcript.txt'.format(KSSS_DIRECTORY), encoding='utf-8') as transcript:
    for line in transcript:
        splitted = line.split('|')
        file_name = splitted[0]
        expanded_text = unicodedata.normalize('NFC', splitted[2])

        result_dict['{}/KoreanSingleSpeakerSpeech/{}'.format(KSSS_DIRECTORY, file_name)] = expanded_text

with open('{}/alignment.json'.format(KSSS_DIRECTORY), 'w') as alignment:
    json.dump(result_dict, alignment)
