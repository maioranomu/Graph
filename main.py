import os

graph_dict = {}

# for i in range(10):
#     i += 1
#     graph_dict[i] = str(i) + "A", i

def clear():
    os.system("cls")
    
def add_graph():
    global graph_dict
    name = input("Add graph name: ")
    # print(graph_dict)
    while True:
        try:
            value = int(input("Add graph value: "))
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
    
    for number in range(maxgraph + 1):
        graphnumber += str(number) + "  "
    
    clear()
    print(f"{space_nums} {graphnumber}")
    for graph in graph_dict:
        print("\n")
        spacename = " " * ((max(namevalue) - len(graph_dict[graph][0])) + 1)
        print(space + ("#" * graph_dict[graph][1] * 3))
        print(graph_dict[graph][0] + spacename + ("#" * graph_dict[graph][1] * 3))
        print(space + ("#" * graph_dict[graph][1] * 3))
        
while True:
    clear()
    add_graph()
    show_graph()
    input("")
