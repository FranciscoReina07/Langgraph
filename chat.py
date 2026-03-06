from graph import build_graph
from config import graph_config

def stream_graph_updates(user_input: str):
    graph = build_graph()
    
    # AQUÍ ESTÁ LA MAGIA: Le damos un ID a esta conversación (puede ser "1", "chat_prueba", etc.)
    config = {"configurable": {"thread_id": "1"}}
    
    # Ahora le pasamos el input Y la configuración al grafo
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config
    ):
        for value in event.values():
            value["messages"][-1].pretty_print()

def run_chat_loop():
    while True:
        try:
            user_input = input("User: ")
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("GoodBye")
                break 
            
            stream_graph_updates(user_input)
            
        except Exception as e:
            print(f"\n ERROR ENCONTRADO: {e}") 
            print("Cerrando el chat...")
            break