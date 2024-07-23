import random

def generate_map(width, height, tile_types, initial_chunk):
  """Generuje nową mapę o podanych wymiarach i typach kafelków, 
  opierając się na początkowym fragmencie.

  Args:
    width: Szerokość nowej mapy.
    height: Wysokość nowej mapy.
    tile_types: Lista możliwych typów kafelków (liczby całkowite).
    initial_chunk: Słownik reprezentujący fragment mapy 
                   (z kluczem "data" i listą list kafelków).

  Returns:
    Słownik reprezentujący nową mapę.
  """

  new_map = {"data": [[0 for _ in range(width)] for _ in range(height)]}
  chunk_width = len(initial_chunk["data"][0])
  chunk_height = len(initial_chunk["data"])

  for y in range(height):
    for x in range(width):
      # Sprawdzenie, czy aktualna pozycja znajduje się w obrębie początkowego fragmentu
      if x < chunk_width and y < chunk_height:
        new_map["data"][y][x] = initial_chunk["data"][y][x]
      else:
        # Wygenerowanie nowego kafelka na podstawie sąsiednich
        neighbors = []
        if x > 0:
          neighbors.append(new_map["data"][y][x - 1])
        if y > 0:
          neighbors.append(new_map["data"][y - 1][x])
        if x < width - 1:
          neighbors.append(new_map["data"][y][x + 1])
        if y < height - 1:
          neighbors.append(new_map["data"][y + 1][x])

        # Wybór losowego kafelka z sąsiadów lub losowego typu kafelka
        if neighbors:
          new_map["data"][y][x] = random.choice(neighbors)
        else:
          new_map["data"][y][x] = random.choice(tile_types)

  return new_map

# Przykładowe użycie
initial_map_chunk = {
  "map": "{\"data\":[[1,1,1,1,1],[1,3,1,1,1],[1,1,1,3,3]]}"
}

# Przekształcenie stringa JSON na słownik
import json
initial_map_chunk["data"] = json.loads(initial_map_chunk["map"])["data"]

new_map = generate_map(width=20, height=15, tile_types=[1, 3, 52, 53, 54], initial_chunk=initial_map_chunk)

# Wyświetlenie nowej mapy
for row in new_map["data"]:
  print(row)
