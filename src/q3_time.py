from typing import List, Tuple
import json
from collections import Counter
import heapq

from memory_profiler import profile

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:

    mentioned_user_counter = Counter()
    # Iteración: Procesar archivo linea por linea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                mentioned_users = tweet.get('mentionedUsers', [])
                if mentioned_users: 
                    
                    mentioned_user_counter.update(username for user in mentioned_users if (username := user.get('username')))

            #manejo de errores
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing the tweet: {e}")
    return mentioned_user_counter.most_common(10)
