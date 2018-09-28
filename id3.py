import sys
import csv
import argparse
import id3model
import id3math
import tree
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

def get_grouped_entropies(data, attribute_intex:int, decision_attribute_index:int):
    grouped = linq.group_by(data, lambda x: x[attribute_intex])

    for key in grouped:
        grouped[key] = linq.select(grouped[key], lambda x: x[decision_attribute_index])

    grouped_entropies = dict()
    count = 0
    for key in grouped:
        count += len(grouped[key])
        grouped_entropies[key] = (id3math.get_entropy(grouped[key]), len(grouped[key]))

    return count, grouped, grouped_entropies

def get_info_gain_for_attribute(data, attribute_intex:int, decision_attribute_index:int):
    
    count, grouped, grouped_entropies = get_grouped_entropies(data, attribute_intex, decision_attribute_index)
    
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

    info_gains = linq.to_dict(range(len(data[0])-1), lambda i: get_info_gain_for_attribute(data,i,args.decision_attribute),lambda i: i)
    
    # for i in range(len(data[0])-1):
    #     info_gain = get_info_gain_for_attribute(data,i,args.decision_attribute)
    #     print('info gain for attribute {}: {}'.format(i, info_gain))

    sorted_ig = sorted(info_gains, reverse=True)
    
    print('info gains: {}'.format(info_gains))
    print('sorted gains: {}'.format(sorted_ig))
    ### Growing the tree ###


    def grow_the_tree(input_node: tree.Node, sorted_ig_index:int, input_data:list):
        if sorted_ig_index > len(sorted_ig):
            return input_node

        index = info_gains[sorted_ig[sorted_ig_index]]
        _,_,grouped_entropies = get_grouped_entropies(input_data,index,args.decision_attribute)

        node = input_node ## pass as input into recursive method
        for value in grouped_entropies:
            if grouped_entropies[value][0]==0:
                decision = linq.where(input_data, lambda x: x[index] == value)[0][args.decision_attribute]
                node.append(tree.Node('{}->{}'.format(value, decision)))
            else:
                new_node = tree.Node('{}->{}'.format(value,info_gains[sorted_ig[index+1]]))
                new_data = linq.remove_all(data, lambda x: x[index] == value)
                node.append(grow_the_tree(new_node, sorted_ig_index+1, new_data))#append recursive call
        return node

    node = grow_the_tree(tree.Node(0),0,data)
    print(node.draw())
        
        





