from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


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

smoothWin = 100
farray = [0] * smoothWin


def smooth(x):
    farray.pop(0)
    farray.append(x)
    fx = np.mean(farray)
    return fx


xn, hdr = read_txt('src.txt')
rawdata = xn.reshape((99999,))
# t = np.linspace(-1, 1, 201)
# x = (np.sin(2*np.pi*0.75*t*(1-t) + 2.1) +
#      0.1*np.sin(2*np.pi*1.25*t + 1) +
#      0.18*np.cos(2*np.pi*3.85*t))
# xn = x + np.random.randn(len(t)) * 0.08

b = [0.0000046818, 0, -0.0000140454, 0, 0.0000140454, 0, -0.0000046818]
a = [1, -5.85422751575530, 14.3770740015921, -18.9564010023544, 14.1524743840052, -5.67275169886819, 0.953866160622467]

zi = signal.lfilter_zi(b, a)
dss = zi
datarealfilter = []
rectify = []
smoothd = []
datawholelfilter, _ = signal.lfilter(b, a, rawdata, zi=dss)
smwin = 400
def filter():
    for i in rawdata:
        z, dss = signal.lfilter(b, a, [i], zi=dss)
        datarealfilter.append(z)
        rectify.append(np.abs(z))
        smoothd.append(smooth(np.abs(z)))
filter()
datawholefilter = signal.filtfilt(b, a, rawdata)

fig, ax = plt.subplots(6, 1, sharex=True)
ax[0].plot(rawdata, label="raw data")
ax[1].plot(datawholefilter, label="data whole filter")
ax[2].plot(datawholelfilter, label="data whole lfilter")
ax[3].plot(datarealfilter, label="data real lfilter")
ax[4].plot(rectify, label="rectify")
ax[5].plot(smoothd, label="smooth")

ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[3].legend()
ax[4].legend()
# ax[5].legend()

plt.show()
