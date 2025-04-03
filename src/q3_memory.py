import json
import heapq
from collections import defaultdict
from typing import List, Tuple
from memory_profiler import profile

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = defaultdict(int) 

    # Iteración: Procesar archivo linea por linea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                mentioned_users = tweet.get('mentionedUsers', [])
                if mentioned_users:
                    for user in mentioned_users:
                        if username := user.get('username'):
                            mention_counts[username] += 1
            
            #manejo de errores
            except json.JSONDecodeError as e:
                print(f"Error decodeando el tweet en formato json: {e}")
            except KeyError as e:
                print(f"Error encontrando mentionedUsers o username en el objeto twitter: {e}")

    # Usar heap para buscar el top 10 users 
    return heapq.nlargest(10, mention_counts.items(), key=lambda x: x[1])
