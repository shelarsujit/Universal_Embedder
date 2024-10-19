import sys
from universal_embedder.extractor import process_file, process_link
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_source>")
        sys.exit(1)
    input_source = sys.argv[1]
    if os.path.isfile(input_source):
        process_file(input_source)
    elif input_source.startswith('http'):  # This handles URLs
        process_link(input_source)
    else:
        print("Unsupported input source")

if __name__ == "__main__":
    main()
