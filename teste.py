import time
import json
from pygnuplot import  gnuplot
import pandas as pd


comparisons = 0
assignment = 0
start = time.time()
end = time.time()
total_time = end - start

class GraphData:
    ascending = []
    descending = []
    random_order = []

final_data = GraphData()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    global comparisons
    global assignment

    comparisons += 1
    if l < n and arr[i] < arr[l]:
        assignment += 1
        largest = l

    comparisons += 1
    if r < n and arr[largest] < arr[r]:
        assignment += 1
        largest = r

    comparisons += 1
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)
    

def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)



def collect_data(final_data):
    for i in range(3, 7):
        filename = 'numbers-10-'+str(i)+'.json'
        file = open(filename)
        data = json.load(file)

        global comparisons
        global assignment
        global start
        global end
        global total_time

        comparisons = 0
        assignment = 0
        start = time.time()
        arr = data['ascending']
        heapSort(arr)
        end = time.time()
        total_time = end - start
        final_data.ascending.append({
            'comparisons': comparisons,
            'assignment': assignment,
            'total_time': total_time,
        })


        comparisons = 0
        assignment = 0
        start = time.time()
        arr = data['descending']
        heapSort(arr)
        end = time.time()
        total_time = end - start
        final_data.descending.append({
            'comparisons': comparisons,
            'assignment': assignment,
            'total_time': total_time,
        })


        comparisons = 0
        assignment = 0
        start = time.time()
        arr = data['random_order']
        heapSort(arr)
        end = time.time()
        total_time = end - start
        final_data.random_order.append({
            'comparisons': comparisons,
            'assignment': assignment,
            'total_time': total_time,
        })

# def generate_graph_time(data: GraphData):
#     g = gnuplot.Gnuplot(debug=1, terminal = 'pngcairo font "arial,10" fontscale 1.0 size 600, 400', output = '"simple.1.png"')

#     pontos_vetor1 = []
#     pontos_vetor2 = []
#     pontos_vetor3 = []

#     for i in range(4):
#         pontos_vetor1.append((10**(i+3), data.ascending[i]['total_time']))

#     for i in range(4):
#         pontos_vetor2.append((10**(i+3), data.descending[i]['total_time']))
    
#     for i in range(4):
#         pontos_vetor3.append((10**(i+3), data.random_order[i]['total_time']))

#     linha1 = gnuplot.Gnuplot.Data(data=pontos_vetor1, with_="linespoints", title="Vetor 1")
#     linha2 = gnuplot.Gnuplot.Data(data=pontos_vetor2, with_="linespoints", title="Vetor 2")
#     linha3 = gnuplot.Gnuplot.Data(data=pontos_vetor3, with_="linespoints", title="Vetor 3")

#     g.plot(linha1, linha2, linha3)

# collect_data(final_data)
# print(len(final_data.ascending))
# generate_graph_time(final_data)


# df = pd.DataFrame(data =  [[1, 2],[2, 3],[3, 2],[4, 6],[5, 10],[6, 11],[7, 14]])

df = pd.DataFrame(data={"label_column": ['a', 'b', 'c', 'd', 'e', 'f'], "col2": [10, 11, 12, 5, 14, 15], "col3": [9, 15, 4, 6, 20, 30]})
df2 = pd.DataFrame(data={"label_column": ['a'], "col2": [10], "col3": [2]})


# df1 = pd.DataFrame(data = [[1, 2],[2, 3],[3, 2],[4, 6],[5, 10],[6, 11],[7, 14]])

g = gnuplot.Gnuplot()
# Note that the first parameter is df and there is no "data.file" in
# the following commmand.

g.set(terminal = 'pngcairo', output = '"simple.1.png"')
g.set(style="line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 pi -1 ps 1.125")
g.set(pointintervalbox='3')
g.set(yrange='[0:100]')
g.set(style="line 2 lc rgb '#9912ad' lt 1 lw 2 pt 7 pi -1 ps 0.5")
g.plot_data(df2, " u 3:xtic(2) title 'Line1' with linespoints ls 1", " u 4:xtic(2) title 'Line1' with linespoints ls 1 ")
