import instaloader
import pandas as pd

L = instaloader.Instaloader()

try:
    L.login("andre_rodriguesp4","André91283594")
    print("Login bem-sucedido!")
except instaloader.exceptions.InstaloaderException as e:
    print(f"Erro no login: {e}.")
    exit()

profile_name = input("Digite o usuário: ")

profile = instaloader.Profile.from_username(L.context, profile_name)

data = []

for post in profile.get_posts():
    data.append({
        'post_id' : post.mediaid,
        'date' : post.date,
        'caption' : post.caption,
        'likes' : post.likes,
        'comments' : post.comments,
        'url' : post.url
    })

print(data)