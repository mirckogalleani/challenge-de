from typing import List, Tuple
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    # Primera iteración: Contar los tweets por fecha
    date_counts = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                date_str = tweet.get('date', '')
                if date_str:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
                    date_only = date_obj.strftime('%Y-%m-%d')
                    date_counts[date_only] += 1
            
            #manejo de errores
            except json.JSONDecodeError as e:
                print(f"Error decodeando el tweet en formato json: {e}")
            except KeyError as e:
                print(f"Error encontrando date en el objeto twitter: {e}")
    
    # obtener el top 10 fechas con la mayor cantidad de tweets
    top_dates = date_counts.most_common(10)
    
    # Segunda iteración: Por cada top fecha encontrar el usuario con mas tweets
    
    result = []
    for date, count in top_dates:
        user_counts = Counter()
        
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)
                    date_str = tweet.get('date', '')
                    
                    if date_str:
                        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
                        date_only = date_obj.strftime('%Y-%m-%d')
                        
                        if date_only == date:
                            username = tweet.get('user', {}).get('username', '')
                            if username:
                                user_counts[username] += 1
                except json.JSONDecodeError as e:
                    print(f"Error decodeando el tweet en formato json: {e}")
                except KeyError as e:
                    print(f"Error encontrando date o username en el objeto twitter: {e}")
        
        most_active_user, user_tweet_count = user_counts.most_common(1)[0] if user_counts else ("None", 0)
        result.append((date, most_active_user))

    return result
