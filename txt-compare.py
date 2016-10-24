#!/usr/bin/env python

# third party
import click


@click.command()
@click.option('--file1', type=click.Path(), help='file path to first text file')
@click.option('--file2', type=click.Path(), help='file path to second text file')

def compare(file1, file2):
    # file1
    file1_list = newline_file_to_list(file1)
    file1_set = set(file1_list)
    file1_dups = unique_dups(file1_list)

    msg = '\nAll lines in {_file1}'.format(_file1=file1)
    print_result(msg, file1_list)

    msg = '\nDuplicate lines in {_file1}'.format(_file1=file1)
    print_result(msg, file1_dups)

    # file2
    file2_list = newline_file_to_list(file2)
    file2_set = set(file2_list)
    file2_dups = unique_dups(file2_list)

    msg = '\nAll lines in {_file2}'.format(_file2=file2)
    print_result(msg, file2_list)

    msg = '\nDuplicate lines in {_file2}'.format(_file2=file2)
    print_result(msg, file2_dups) 

    # intersection
    file_intersection = file1_set & file2_set
    msg = '\nUnique lines in {_file1} AND {_file2} - intersection'.format(
            _file1=file1, _file2=file2)
    print_result(msg, file_intersection)

    # union
    file_union = file1_set | file2_set
    msg = '\nUnique lines in {_file1} OR {_file2} - union'.format(
            _file1=file1, _file2=file2)
    print_result(msg, file_union)

    # file1 only
    file1_only = file1_set - file2_set
    msg = '\nUnique lines in {_file1} ONLY - set difference'.format(
            _file1=file1)
    print_result(msg, file1_only)

    # file2 only
    file2_only = file2_set - file1_set
    msg = '\nUnique lines in {_file2} ONLY - set difference'.format(
            _file2=file2)
    print_result(msg, file2_only)


def newline_file_to_list(file_path):
    with open(file_path, 'r') as f:
        file_list = f.read().splitlines()
    return file_list


def print_result(msg, list_or_set):
    print(msg)
    print('-' * (len(msg)-1))
    print(sorted(list_or_set))
    print()


def unique_dups(seq):
    seen = set()
    dups = set()
    for item in seq:
        if item not in seen:
            seen.add(item)
        else:
            dups.add(item)
    return list(dups)


if __name__ == '__main__':
    compare()
