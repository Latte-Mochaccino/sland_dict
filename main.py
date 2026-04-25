meme_dict = {"LOL": "una respuesta a algo gracioso",
"CRINGE": "algo raro o embarazoso",
"ROFL": "una respuesta a una broma",
"SHEESH": "ligera desaprobación",
"CREEPY": "aterrador, siniestro",
"AGGRO": "ponerse agresivo/enojado",
"SMH": "Desaprobación, decepción o incredulidad",
"BTW": "Añadir información a un tema o conversación"
}

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Lo siento, esta palabra no está en nuestro diccionario.")
