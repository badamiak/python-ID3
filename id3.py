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
            data.append(row)
        
        return data

# def calculate_info_gain(collection:list, decision_entropy)->dict:
#     attribute_values = dict() #dictionary<index, list<index_values>>

#     facts_attributes = linq.select(collection, lambda x: x.attributes) #list<list<int>>

#     for i in range(len(facts_attributes[0])):
#         attribute_values[i] = list()
#         for attributes in facts_attributes:
#             attribute_values[i].append(attributes[i]) ###słownik <atrybut, wartości występujące>

#     info_gains = dict()

#     for key in attribute_values:

#         values_count

#         print (attribute_values[key])
#         info_gains[key] = id3math.get_entropy(attribute_values[key])

#     print (info_gains)


def get_info_gain_for_attribute(data, attribute_intex:int, decision_attribute_index:int):
    grouped = linq.group_by(data, lambda x: x[attribute_intex])

    for key in grouped:
        grouped[key] = linq.select(grouped[key], lambda x: x[decision_attribute_index])

    grouped_entropies = dict()
    count = 0
    for key in grouped:
        count += len(grouped[key])
        grouped_entropies[key] = (id3math.get_entropy(grouped[key]), len(grouped[key]))
    
    attribute_entropy = 0
    for key in grouped_entropies:
        group_len = len(grouped[key])
        attribute_entropy += grouped_entropies[key][0]*(group_len/count)
    
    return decision_entropy - attribute_entropy #info gain


if __name__ == '__main__':
    args = parse_args()

    data = read_input_data(args.file[0], args.decision_attribute)

    decision_entropy = id3math.get_entropy(linq.select(data, lambda x: x[args.decision_attribute]))

    print('dataset entropy: {}'.format(decision_entropy))

    print('info gain for attribute {}: {}'.format(0, get_info_gain_for_attribute(data,0,args.decision_attribute)))
