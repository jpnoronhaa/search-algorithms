import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--type", "-t", choices=['time', 'comparisons', 'assignments'], required=True)
parser.add_argument("--file", "-f", type=str, required=True, nargs='+')
args = parser.parse_args()

files_names = args.file
graph_type = args.type

def collectInputData(files_names):
    inputData = []
    for filename in files_names:
        file = open(filename)
        data = json.load(file)
        inputData.append(data)
    return inputData

inputData = collectInputData(files_names)