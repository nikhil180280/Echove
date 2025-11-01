import time
import pygame
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def split_lyrics(text, per_line=6):
    words = text.split()
    return [' '.join(words[i:i+per_line]) for i in range(0, len(words), per_line)]

lyrics_timed = [
    (0, "Avec ou sans ami, j'aurais bâti ma vie loin du mal et des mots",
        "With or without friends, I would've built my life far from harm and hurtful words"),
    (6, "J'ai franchi les paliers, ouh, ouh, ma bonté m'a fait défaut",
        "I climbed levels, ooh, but my kindness failed me"),
    (12, "Est-ce que j'dois m'méfier de toi plus que les autres ?",
        "Should I be more careful of you than others?"),
    (15, "Ton cœur me veut mais tu n'me dis pas les choses",
        "Your heart wants me but you don't tell me things"),
    (19, "Tu n'me dis pas les choses, oh, oh, oh",
        "You don’t tell me things, oh, oh, oh"),
    (23, "Allô ? Allô ? Allô ? 9elbi, 9elbi, j'deviens paro, paro, paro",
        "Hello? Hello? My heart, my heart… I'm becoming paranoid"),
    (29, "Allô ? Allô ? Allô ? 9elbi, 9elbi, j'deviens paro, paro, paro",
        "Hello? Hello? My heart… I'm losing control"),
    (35, "Allô ? Allô ? Allô ? 9elbi, 9elbi, j'deviens paro, paro, paro",
        "Hello? My heart… I’m going paranoid"),
    (40, "Music ends but the feeling stays. Thanks for being here 🤍", 
        "End of song — the memory lingers 🤍"),
]

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("paro.mp3")
    pygame.mixer.music.play()

threading.Thread(target=play_song, daemon=True).start()

start = time.time()

for idx, (t, original, translated) in enumerate(lyrics_timed):
    while time.time() - start < t:
        time.sleep(0.01)

    if idx == len(lyrics_timed) - 1:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}{original}")
        print(f"{Fore.YELLOW}{translated}")
        time.sleep(3)
        break

    original_parts = split_lyrics(original)
    translated_parts = split_lyrics(translated)

    next_t = lyrics_timed[idx + 1][0] if idx < len(lyrics_timed) - 1 else t + 4
    delay = (next_t - t) / len(original_parts)

    for o_line, t_line in zip(original_parts, translated_parts):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{o_line}")
        print(f"{Fore.YELLOW}{t_line}")
        time.sleep(delay)
