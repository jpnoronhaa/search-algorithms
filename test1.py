import argparse
import json
import heap
import matplotlib.pyplot as plt
import pandas as pd

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

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

def collectOutputData(inputData, type):
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
        outputData['ascending'].append(heap.heapSort(input['ascending'], type))
        outputData['random_order'].append(heap.heapSort(input['random_order'], type))
        outputData['descending'].append(heap.heapSort(input['descending'], type))
        count += 1
    return outputData

outputData = collectOutputData(inputData, graph_type)

def plotGraph(outputData, type):
    data_frame = pd.DataFrame(data=outputData)

    ylabel = ''
    if type == 'time':
        title = 'Gráfico do Tempo de Execução'
        ylabel = 'Tempo (s)'
    elif type == 'comparisons':
        title = 'Gráfico de Quantidade de Comparações'
        ylabel = 'Comparações'
    elif type == 'assignments':
        title = 'Gráfico de Quantidade de Atribuições'
        ylabel = 'Atribuições'

    plt.figure()
    plt.title(title)
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel(ylabel)
    plt.xticks(range(len(data_frame['labels'])), data_frame['labels'])

    plt.plot(data_frame['ascending'], marker='o', label='Melhor Caso')
    plt.plot(data_frame['random_order'], marker='o', label='Caso Médio')
    plt.plot(data_frame['descending'], marker='o', label='Pior Caso')

    plt.legend()
    plt.show()

plotGraph(outputData, graph_type)
