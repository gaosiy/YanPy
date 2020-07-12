"""
Functions for reading and write data.
"""


import numpy as np


def read_txt(filename, sampling_rate=0):
    """
    Reading data from txt file, each column will be loaded as a signal.
    By default, header information will be read from the first line of input data file. The first line should contain
    [sampling rate, channels]. If your data file doesn't have header information in its first line, you need to give
    sampling_rate as input.

    :param str filename: filename of the data.
    :param float sampling_rate: sampling rate (Hz)
    :return: data matrix, header('sampling_rate', 'n_points', 'n_channels')
    :rtype: numpy.array, dict
    """
    with open(filename, 'r') as data_file:
        lines = data_file.readlines()

    if sampling_rate == 0:
        hdr_line = lines[0]
        hdr_line = hdr_line.split()

        hdr = {'sampling_rate': float(hdr_line[0])}

        del lines[0]
    else:
        hdr = {'sampling_rate': sampling_rate}

    firstline = lines[0]
    firstline = firstline.split()

    hdr['n_points'] = len(lines)
    hdr['n_channels'] = len(firstline)

    data = np.zeros([hdr['n_points'], hdr['n_channels']])

    for i in range(hdr['n_points']):
        row = lines[i]
        row = row.rstrip('\n')
        row = row.split()
        for j in range(hdr['n_channels']):
            data[i, j] = float(row[j])

    return data, hdr


def save_txt(data, sampling_rate, filename):
    """
    Save data matrix into a .txt file. The first line will contain the sampling rate.

    :param numpy.array data: data matrix
    :param float sampling_rate: sampling rate
    :param str filename: file name
    """
    shape = np.shape(data)

    with open(filename, 'x') as data_file:
        data_file.write(str(sampling_rate)+'\n')
        for i in range(shape[0]):
            for j in range(shape[1]):
                data_file.write(str(data[i, j]))
                data_file.write('  ')
            data_file.write('\n')
