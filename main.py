import argparse
import json
import heap
from pygnuplot import  gnuplot
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
    output_filename = '"heap-' + type + '.png"'
    ylabel = "'"
    if type == 'time':
        title = "'Gráfico do Tempo de Execução'"
        ylabel = "'Tempo (s)'"
    elif type == 'comparisons':
        title = "'Gráfico de Quantidade de Comparações'"
        ylabel = "'Comparações'"
    elif type == 'assignments':
        title = "'Gráfico de Quantidade de Atribuições'"
        ylabel = "'Atribuições'"

    graph = gnuplot.Gnuplot()

    graph.set(terminal = 'pngcairo', output = output_filename, title = title, ylabel = ylabel, xlabel = "'Tamanho da Entrada'")
    graph.set(style="line 1 lc rgb '#ff0000' lt 1 lw 2 pt 7 pi -1 ps 1.125")
    graph.set(style="line 2 lc rgb '#00ff00' lt 2 lw 2 pt 7 pi -1 ps 1.125")
    graph.set(style="line 3 lc rgb '#0000ff' lt 3 lw 2 pt 7 pi -1 ps 1.125")
    graph.set(ytics=' 0.5')



    graph.set(pointintervalbox='3')
    print(data_frame)
    graph.plot_data(data_frame, "u 3:xtic(2) title 'Melhor Caso' with linespoints ls 1",
                    "u 4:xtic(2) title 'Caso Médio' with linespoints ls 2",
                    "u 5:xtic(2) title 'Pior Caso' with linespoints ls 3")

plotGraph(outputData, graph_type)