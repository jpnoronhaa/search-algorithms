import argparse
import json
import os
import functions
import matplotlib.pyplot as plt
import pandas as pd

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--type", "-t", choices=['time', 'comparisons', 'assignments'], help="Graph type")
parser.add_argument("--folder", "-f", type=str, help="Folder path")
parser.add_argument("--file", nargs='+', help="File path(s)")
args = parser.parse_args()

folder_path = args.folder
file_paths = args.file
graph_type = args.type

def collectInputData(folder_path, file_paths):
    inputData = []
    if folder_path:
        file_names = os.listdir(folder_path)
        file_names = sorted(file_names)
        for filename in file_names:
            file_path = os.path.join(folder_path, filename)
            # print(filename)
            with open(file_path) as file:
                data = json.load(file)
                inputData.append(data)
    elif file_paths:
        for file_path in file_paths:
            print(file_path)
            with open(file_path) as file:
                data = json.load(file)
                inputData.append(data)
    return inputData

def collectOutputData(inputData, graph_type):
    outputData = {
        "labels": [],
        "ascending": [],
        "random_order": [],
        "descending": [],
    }

    labelsArray = []

    for i in range(3):
        label = "10" + get_super(str(i+3))
        labelsArray.append(label)
    
    for i in range(8):
        label = str(i+2) + " * 10" + get_super("5")
        labelsArray.append(label)

    label = "10" + get_super("6")
    labelsArray.append(label)

    count = 0
    for input in inputData:
        outputData['labels'].append(labelsArray[count])
        outputData['ascending'].append(functions.selection_sort(input['ascending'], graph_type))
        outputData['random_order'].append(functions.selection_sort(input['random_order'], graph_type))
        outputData['descending'].append(functions.selection_sort(input['descending'], graph_type))
        count += 1
    return outputData

def plotGraph(outputData, graph_type):
    data_frame = pd.DataFrame(data=outputData)

    ylabel = ''
    if graph_type == 'time':
        title = 'Gráfico do Tempo de Execução'
        ylabel = 'Tempo (s)'
    elif graph_type == 'comparisons':
        title = 'Gráfico de Quantidade de Comparações'
        ylabel = 'Comparações'
    elif graph_type == 'assignments':
        title = 'Gráfico de Quantidade de Atribuições'
        ylabel = 'Atribuições'

    plt.figure()
    plt.title(title)
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel(ylabel)
    plt.xticks(range(len(data_frame['labels'])), data_frame['labels'])

    plt.plot(data_frame['ascending'], marker='o', label='Crescente')
    plt.plot(data_frame['random_order'], marker='o', label='Aleatório')
    plt.plot(data_frame['descending'], marker='o', label='Decrescente')

    plt.legend()
    plt.show()

inputData = collectInputData(folder_path, file_paths)
outputData = collectOutputData(inputData, graph_type)
plotGraph(outputData, graph_type)
