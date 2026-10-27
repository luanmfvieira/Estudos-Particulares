import requests

requisicao = requests.get('https://teste-ff3ac-default-rtdb.firebaseio.com/.json') #colocar json no final apenas no firebase
print(requisicao)
print(requisicao.json()) #dicionario

#informacoes = '{"Nome": "Erick"}'

#requisicao = requests.post('https://teste-ff3ac-default-rtdb.firebaseio.com/.json', data=informacoes)
#print(requisicao)
#print(requisicao.json())


informacoes = '{"Nome": "Dayse", "Sobrenome": "Silva", "Idade": 22}'

requisicao = requests.patch('https://teste-ff3ac-default-rtdb.firebaseio.com/-OVht4PO3Wc3taBhsHvV.json', data=informacoes)
print(requisicao)
print(requisicao.json())

