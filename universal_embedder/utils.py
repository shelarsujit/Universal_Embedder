import os

def generate_metadata(input_source):
    metadata = {}
    if os.path.isfile(input_source):
        file_extension = os.path.splitext(input_source)[-1].lower()
        metadata['type'] = file_extension.replace('.', '')
        metadata['name'] = os.path.basename(input_source)
    elif input_source.startswith('http'):
        metadata['type'] = 'url'
        metadata['name'] = input_source.split('//')[-1].split('/')[0]  # Use domain as name
    else:
        metadata['type'] = 'unknown'
        metadata['name'] = 'unknown'
    return metadata
