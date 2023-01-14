#!/usr/bin/python3
"""The ``101-stats`` module

A script that parses logs based on a given input and prints to `stdout`

Input format:
`IP Address` - [`date`] "GET /projects/260 HTTP/1.1" `status code` `file size`

Each 10 lines and after a `KeyboardInterrupt` prints the following stats:
    Total file size in the format:
        File size: `total size`
    where `total size` is the sum of all previous sizes

    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        If a status code doesn’t appear, nothing is printed for the code
        Status codes are printed in ascending order
        Format:
            `status code`: `number of occurences`
"""

from sys import stdin, stdout


def log_parser():
    """Sorts a line of text from stdin and keeps a log which is then printed"""

    list_of_stat_codes = (200, 301, 400, 401, 403, 404, 405, 500)
    stat_codes_occurence = {}
    total_file_size = 0
    line_count = 0

    try:
        for data_line in stdin:
            if line_count == 10:
                print_info(total_file_size, stat_codes_occurence)
                line_count = 1
            else:
                line_count += 1

            data_line = data_line.split()

            try:
                total_file_size += int(data_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if int(data_line[-2]) in list_of_stat_codes:
                    if stat_codes_occurence.get(data_line[-2], False) is False:
                        stat_codes_occurence[data_line[-2]] = 1
                    else:
                        stat_codes_occurence[data_line[-2]] += 1
            except (IndexError, ValueError):
                pass

        print_info(total_file_size, stat_codes_occurence)

    except KeyboardInterrupt:
        print_info(total_file_size, stat_codes_occurence)
        raise


def print_info(total_file_size, stat_codes_occurence):
    """Prints the information gathered thus far from the log

    Args:
        total_file_size (int): Total size of the files read so far
        stat_codes_occurence (dict): Key/value pairs of all the status codes
            and the number of occurences in the ten line window
    """

    stdout.flush()
    stdout.write("File size: {:d}\n".format(total_file_size))
    for key in sorted(stat_codes_occurence):
        stdout.write("{:s}: {:d}\n".format(key, stat_codes_occurence[key]))
    stdout.flush()


if __name__ == "__main__":
    log_parser()
