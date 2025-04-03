from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
import heapq
from memory_profiler import profile

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    date_to_users = defaultdict(lambda: defaultdict(int))
    date_tweet_counts = defaultdict(int)
    
    # Primera iteración: Cargar y procesar todos los tweets en una iteración
    with open(file_path, 'r') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                date_str = tweet.get('date', '')
                if date_str:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
                    date_only = date_obj.strftime('%Y-%m-%d')
                    # Incrementar el contador de tweets por esa fecha
                    date_tweet_counts[date_only] += 1
                    # Guardar la actividad del usuario por esa fecha
                    username = tweet.get('user', {}).get('username', '')
                    if username:
                        date_to_users[date_only][username] += 1
            except (json.JSONDecodeError, ValueError, KeyError) as e:
                print(f"Error processing the tweet: {e}")
    
    # obtener el top 10 fechas con la mayor cantidad de tweets
    top_dates = heapq.nlargest(10, date_tweet_counts.items(), key=lambda x: x[1])
    # Segunda iteración: Por cada top fecha encontrar el usuario con mas tweets
    result = []
    
    for date, count in top_dates:
        user_counts = date_to_users[date]
        print(user_counts)
        most_active_user, user_tweet_count = max(user_counts.items(), key=lambda x: x[1]) if user_counts else ("None", 0)
        result.append((date, most_active_user))   
    
    return result