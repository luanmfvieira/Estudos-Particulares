import json

dados = {
    "nome": "Luan",
    "idade": 24,
    "estudante": True,
    "cursos": ["Python", "JavaScript"]
}

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)
