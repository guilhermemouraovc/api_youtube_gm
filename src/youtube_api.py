from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
PLAYLIST_ID = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"  

def buscar_videos_da_playlist(api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    resultados = []
    next_page_token = None

    while True:
        req = youtube.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=PLAYLIST_ID,
            pageToken=next_page_token
        )
        res = req.execute()
        resultados += res["items"]
        next_page_token = res.get("nextPageToken")
        if not next_page_token:
            break

    print(f"Encontrados {len(resultados)} vídeos na playlist.")
    return [item["snippet"]["resourceId"]["videoId"] for item in resultados]

def pegar_estatisticas(video_ids, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    dados = []

    for i in range(0, len(video_ids), 50):
        req = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids[i:i+50])
        )
        res = req.execute()

        for item in res["items"]:
            dados.append({
                "Título": item["snippet"]["title"],
                "Data": item["snippet"]["publishedAt"],
                "Visualizações": int(item["statistics"].get("viewCount", 0)),
                "Curtidas": int(item["statistics"].get("likeCount", 0)),
                "Comentários": int(item["statistics"].get("commentCount", 0))
            })

    return pd.DataFrame(dados)

if __name__ == "__main__":
    ids = buscar_videos_da_playlist(API_KEY)
    df = pegar_estatisticas(ids, API_KEY)
    df.to_csv("dados_f1.csv", index=False)
    print(df)