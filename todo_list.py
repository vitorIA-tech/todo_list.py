# Sistema de To-Do List (Lista de Tarefas)
tarefas = []

def adicionar_tarefa(nome, categoria):
    tarefas.append({"nome": nome, "categoria": categoria, "status": "Pendente"})
    print(f"📌 Tarefa adicionada: {nome} [{categoria}]")

def concluir_tarefa(nome):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["status"] = "Concluída"
            print(f"✅ Tarefa concluída: {nome}")
            return
    print("❌ Tarefa não encontrada.")

def listar_tarefas():
    print("\n--- Minhas Tarefas ---")
    for tarefa in tarefas:
        icone = "✅" if tarefa["status"] == "Concluída" else "⏳"
        print(f"{icone} {tarefa['nome']} | Categoria: {tarefa['categoria']}")

# Simulando o uso do sistema na prática
adicionar_tarefa("Estudar lógica de programação", "Estudos")
adicionar_tarefa("Organizar documentos de admissão", "RH")
adicionar_tarefa("Revisar e-mails de clientes", "Atendimento")

concluir_tarefa("Organizar documentos de admissão")
listar_tarefas()
