import random

memes = {
    "animales": [
        "https://i.imgur.com/1.jpg",
        "https://i.imgur.com/2.jpg"
    ],
    "programacion": [
        "https://i.imgur.com/3.jpg",
        "https://i.imgur.com/4.jpg"
    ],
    "random": [
        "https://i.imgur.com/5.jpg"
    ]
}

def get_meme(categoria):
    if categoria in memes:
        return random.choice(memes[categoria])
    else:
        return "categoia no encontrada"
