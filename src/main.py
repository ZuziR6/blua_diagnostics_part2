from src.graph.workflow import graph

while True:
    user_input = input("Paciente: ")

    result = graph.invoke({
        "input": user_input
    })

    print(result)
