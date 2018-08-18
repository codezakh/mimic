import json
import os

import re

def is_unparsed_data_batch_name(filename):
    return filename.endswith('dimension')


data_directory_name = './data'
final_data_filename = 'final_data.txt'


filtering_predicates = [
    lambda comment: len(comment['body']) >= 50
    ]

final_data = []

unparsed_data_batch_names = filter(
    is_unparsed_data_batch_name,
    os.listdir(data_directory_name)
    )

match_url = re.compile(r"\[.*\]\(.*\)")

for unparsed_data_batch_name in unparsed_data_batch_names:
    filename = os.path.join(data_directory_name, unparsed_data_batch_name)
    
    with open(filename) as unparsed_data_batch:
        print(filename)
        data_as_json = json.load(unparsed_data_batch).get('data')

    for comment in data_as_json:
        if all(predicate(comment) for predicate in filtering_predicates):
            comment_text = re.sub(match_url, 'URL_REPLACED', comment['body'])
            final_data.append(comment_text)



with open(os.path.join(data_directory_name, final_data_filename), 'w+') as final_data_file:
    final_data_file.writelines(final_data)
