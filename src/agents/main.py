from langgraph.graph import StateGraph, START, END

#Definimos una función (nodo)
def nodo_vacio(state: dict):
    return state

#Construimos el grafo
builder = StateGraph(dict)

#Le añadimos nuestro nodo vacío
builder.add_node("mi_nodo", nodo_vacio)

#Conectamos el inicio con el nodo, y el nodo con el final
builder.add_edge(START, "mi_nodo")
builder.add_edge("mi_nodo", END)

# Compilamos el grafo
agent = builder.compile()

def main():
    print("Hello from lang-graph!")

if __name__ == "__main__":
    main()