import sys
import csv
import argparse
import id3model
import id3math
import linq_to_python as linq

def parse_args(args = sys.argv):
    '''Parses input arguments to Arguments class object'''

    print('Args are: {}'.format(args))
    print('setting-up parser')
    parser = argparse.ArgumentParser(args)
    parser.add_argument('-d', dest = 'decision_attribute', type=int, default = 0)
    parser.add_argument('file', metavar = 'F', nargs=1, type=str, default = None)

    print('parsing args')
    return parser.parse_args()

def read_input_data(file_path:str, decision_index:int):
    print('reading from file: {}'.format(file_path))

    with open(file_path) as file:
        stream = csv.reader(file, delimiter = ',')

        data = list()
        for row in stream:
            measure = row[decision_index]
            row.remove(row[decision_index])

            data.append(id3model.Fact(measure, row))
        
        return data


if __name__ == '__main__':
    args = parse_args()

    data = read_input_data(args.file[0], args.decision_attribute)

    decision_entropy = id3math.get_entropy(linq.select(data, lambda x: x.measure))

    print(decision_entropy)