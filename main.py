import os

graph_dict = {}

# for i in range(15):
#     i += 1
#     graph_dict[i] = str(i), float(i)

def clear():
    os.system("cls")
    
def add_graph():
    global graph_dict
    name = input("Add graph name: ")
    while True:
        try:
            value = float(input("Add graph value: "))
            break
        except ValueError:
            print("Invalid input, please enter a number.")
            
    graph_dict[len(graph_dict) + 1] = [name, value]
     
def show_graph():
    namelist = []
    namevalue = []
    graphvalue = []
        
    for graph in graph_dict:
        namelist.append(graph_dict[graph][0])
        graphvalue.append(graph_dict[graph][1])
        maxgraph = max(graphvalue)
        
    for name in namelist:
        namevalue.append(len(name))
        
    space_nums = " " * (max(namevalue) - 1)
    space = " " * (max(namevalue) + 1)
    graphnumber = ""
    marker = ""
    
    for number in range(int(maxgraph + 2)):
        
        if len(str(number)) == 1:
            graphnumber += str(number) + "   "
        elif len(str(number)) == 2:
            graphnumber += str(number) + "  "
        elif len(str(number)) == 3:
            graphnumber += str(number) + " "
        else:
            graphnumber += str(number)   
        
    for number in range(int(maxgraph + 2)):
        marker += "|" + "   "
        
    clear()
    print(f"{space_nums} {graphnumber}")
    print(f"{space_nums} {marker}")
    for graph in graph_dict:
        each = graph_dict[graph][1] / 0.25
        print("\n")
        spacename = " " * ((max(namevalue) - len(graph_dict[graph][0])) + 1)
        print(space + ("#" * int(each)))
        print(graph_dict[graph][0] + spacename + ("#" * int(each)) , str(graph_dict[graph][1]))
        print(space + ("#" * int(each)))
        
while True:
    clear()
    add_graph()
    show_graph()
    input("")
    clear()
