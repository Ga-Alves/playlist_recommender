import  requests

print('---------------------------------------------------------')
print("| Informe músicas para receber uma playlist customizada |")
print('---------------------------------------------------------')
print('|   insira /send para finalizar o envio                 |')
print('---------------------------------------------------------')


body = {
    "songs": []
}
music = input()
while music != '/send':
    body['songs'].append(music)
    music = input()


print("Aguarde enquanto processamos seu dados!")
print()
res = requests.post('http://localhost:52023/api/recommend', json=body)
print("Sua playlist: ")
decodeRes =  res.json()
print("API version: ", decodeRes['version'])
print("Latest Model Update Date: ", decodeRes['model_date'])
print("Songs: ")
songs = decodeRes['songs']
for (i, song) in enumerate(songs):
    print(f'{i+1} {song}')