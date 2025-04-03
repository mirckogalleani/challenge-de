from typing import List, Tuple
from collections import Counter
import emoji
import json
from memory_profiler import profile

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Función para extraer emojis del texto
    def extract_emojis(text):
        if not text:
            return []
        return [c for c in text if c in emoji.EMOJI_DATA]
    
    emoji_counter = Counter()
    
    # Iteración: Procesar archivo linea por linea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                text = tweet.get('content', '') or tweet.get('renderedContent', '')
                # extraer emojis del texto y contar los emojis
                emojis_found = extract_emojis(text)
                emoji_counter.update(emojis_found)
            
            #manejo de errores
            except json.JSONDecodeError as e:
                print(f"Error decodeando el tweet en formato json: {e}")
            except KeyError as e:
                print(f"Error encontrando content o renderedContent en el objeto twitter: {e}")
    
    #  obtener el top 10 emojis
    return emoji_counter.most_common(10)
