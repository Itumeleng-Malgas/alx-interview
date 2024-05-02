#!/usr/bin/python3
""" Write a script that reads stdin line by line and computes metrics """

from collections import defaultdict


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output
    """
    print("File size:", fileSize)
    for key in sorted(statusCodes.keys(), key=int):
        print("{}: {}".format(key, statusCodes[key]))


def parseLogs():
    """
    Reads logs from standard input and generates reports
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = defaultdict(int)
    codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    try:
        for line in stdin:
            lineNumber += 1
            parts = line.split()
            if len(parts) != 10:
                continue  # Skip lines that do not match the expected format
            try:
                if parts[8] in codes:
                    fileSize += int(parts[9])
                    statusCodes[parts[8]] += 1
            except ValueError:
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
                fileSize = 0
                statusCodes.clear()
        report(fileSize, statusCodes)
    except KeyboardInterrupt:
        report(fileSize, statusCodes)
        raise


if __name__ == '__main__':
    parseLogs()
