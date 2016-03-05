#!/usr/bin/env python3
"""
A utility for splitting large files into smaller chunks based on the number of
lines. It is similar to the linux command "split".

Usage information: split.py -h
"""

import argparse
import logging
import os
import sys


log_formatter = logging.Formatter("%(message)s")
logger = logging.getLogger(__name__)


def main():
	parser = argparse.ArgumentParser(
		description='Split large file into smaller files.',
		)
	parser.add_argument(
		'input_file',
		type=argparse.FileType('r'),
		nargs='?',
		default=sys.stdin,
		help='''Path to input file to be split.
		If not specified will default to stdin.
		(default: STDIN)''',
		)
	parser.add_argument(
		'-l',
		'--num-lines',
		metavar='N',
		dest='num_lines',
		default=1000,
		type=int,
		help='''Maximum number of lines for each output file.
		(default: %(default)d lines)''',
		)
	parser.add_argument(
		'-o',
		'--output-file',
		metavar='file',
		dest='output_file',
		default="chunk.txt",
		help='''Base-name of output file chunks.
		A base-name of chunk.txt will result in output of the
		format chunk_1.txt, chunk_2.txt, etc.
		(default: %(default)s)''',
		)
	parser.add_argument(
		'-v',
		'--verbose',
		dest='verbose',
		action='count',
		help='''Use verbose output.
		Can be specified multiple times to increase verbosity (maximum of two times)''',
		)

	args = parser.parse_args()
	setup_logging(verbose=args.verbose)

	file_num = 1
	while split(args.input_file, args.num_lines, args.output_file, file_num):
		file_num = file_num + 1


def split(large_file, num_lines, base_name, file_num):
	"""
	Writes out the specified num_lines to an output file
	from the given large_file.
	Returns False when it encounters the end of the file/stream.
	"""
	out_filename = construct_output_filename(base_name, file_num)

	logger.debug("Writing chunk: {}".format(out_filename))

	with open(out_filename, 'w') as out_file:
		for x in range(num_lines):
			line = large_file.readline()
			if (not line):
				return False
			else:
				out_file.write(line)

	return True


def construct_output_filename(base_name, file_num, separator='_'):
	"""
	Takes a filename "/path/to/filename.txt" and a file number x
	and returns "/path/to/filename_x.txt"

	>>> construct_output_filename("base_name.txt", 3)
	'base_name_3.txt'

	>>> construct_output_filename("base_name", 1)
	'base_name_1'

	>>> construct_output_filename("base_name.txt.txt", 1)
	'base_name.txt_1.txt'

	>>> construct_output_filename("base_name.", 1)
	'base_name_1.'
	"""
	filename, file_extension = os.path.splitext(base_name)
	return "{name}{sep}{num}{ext}".format(
		name=filename,
		sep=separator,
		num=file_num,
		ext=file_extension,
		)

def setup_logging(verbose=False):
	console_handler = logging.StreamHandler()
	console_handler.setFormatter(log_formatter)
	logger.addHandler(console_handler)

	if verbose >= 2:
		logger.setLevel(logging.DEBUG)
	elif verbose >= 1:
		logger.setLevel(logging.INFO)
	else:
		logger.setLevel(logging.WARNING)

	logger.debug("Using {} log-level".format(
		logging.getLevelName(logger.level),
		)
	)


if __name__ == "__main__":
	main()