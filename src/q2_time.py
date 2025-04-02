from typing import List, Tuple
import re
import json
import emoji
from collections import Counter
import heapq
from memory_profiler import profile

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Función para extraer emojis del texto
    def extract_emojis(text):
        if not text:
            return []
        return [c for c in text if c in emoji.EMOJI_DATA]

    # Iteración: Procesar archivo linea por linea
    all_emojis = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                text = tweet.get('content', '') or tweet.get('renderedContent', '')
                if not text:
                    continue
                # extraer emojis del texto
                emoji_matches = extract_emojis(text)
                all_emojis.extend(emoji_matches)

            except json.JSONDecodeError as e:
                print(f"Error processing the tweet: {e}")
        #contar emojis
        emoji_counter = Counter(all_emosjis)

    # Usar heap para buscar el top 10 emojis
    return heapq.nlargest(10, emoji_counter.items(), key=lambda x: x[1])