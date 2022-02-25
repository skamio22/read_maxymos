import glob
import matplotlib.pyplot as plt
import read_maxymos

files = glob.glob('*.csv')
if len(files) > 0:
    dc = read_maxymos.read_maxymos(files[0])
    x = dc['x']
    y = dc['y']
    print('Read file: {}'.format(dc['file']))
    print('Program: {} / cycle: {} / result: {}'.format(dc['program'], dc['cycle'], dc['result']))
    print('Data Length: {}'.format(x.size))
    plt.plot(x, y, label=dc['name'], color='green' if dc['result'] == 'OK' else 'red')
    plt.title(dc['date'])
    plt.xlabel(dc['unit_x'])
    plt.ylabel(dc['unit_y'])
    plt.legend()
    plt.show()
else:
    print('No files found')
