# Split.py

Efficient large file splitting with Python.

This python utility script provides a way to split a large file into smaller files
based on their number of lines. It does not load any files into memory so can be run on very large files.

## Usage

    usage: split.py [-h] [-l N] [-o file] [-v] [input_file]
    
    Split large file into smaller files.
    
    positional arguments:
      input_file            Path to input file to be split. If not specified will
                            default to stdin. (default: STDIN)
    
    optional arguments:
      -h, --help            show this help message and exit
      -l N, --num-lines N   Maximum number of lines for each output file.
                            (default: 1000 lines)
      -o file, --output-file file
                            Base-name of output file chunks. A base-name of
                            chunk.txt will result in output of the format
                            chunk_1.txt, chunk_2.txt, etc. (default: chunk.txt)
      -v, --verbose         Use verbose output. Can be specified multiple times to
                            increase verbosity (maximum of two times)

## Tests

Currently there are no unit tests written for split.py, but there are some doctests.
These can be run with the following:

    python3 -m doctest split.py