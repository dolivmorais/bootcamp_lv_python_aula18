import requests
from pydantic import BaseModel

"""
requests.get # select
requests.post # insert
requests.put # update
requests.delete # delete"""


class PokemosSchema(BaseModel): # contrato de dados, schema de dados, view da minha api
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemons(id: int):
    response = requests.get(f"https://www.pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data["types"] # list
    types_list = []

    for type_info in data_types:
        types_list.append(type_info["type"]["name"])
    types = ", ".join(types_list)
    return PokemosSchema(nome=data["name"],type=types)

if __name__ == "__main__":
    print(pegar_pokemons(25))
    print(pegar_pokemons(23))
    print(pegar_pokemons(20))

"""
# for para pegar todos os pokemons
for i in range(1, 152):
    URL = "https://www.pokeapi.co/api/v2/pokemon/" + f"{i}/"
    response = requests.get(URL)
    data = response.json()
    types_list = []
    for type_info in data["types"]:
        types_list.append(type_info["type"]["name"])
    types = ", ".join(types_list)
    print(data["name"], types)
"""
