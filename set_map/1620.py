import sys
r = sys.stdin.readline

N, M= map(int, r().split()) 

pokedict_name = {}
pokedict_id = {}

for i in range(1,N+1):
    temp = r().strip()
    pokedict_name[temp] = i
    pokedict_id[i] = temp
    
for _ in range(M): 
    pokemon = r().strip()
    if pokemon.isdigit() :
        print(pokedict_id[int(pokemon)])
    else:
        print(pokedict_name[pokemon])