
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random
import os

def get_tracks_artists(playlist_link: str) -> list[str]:

    playlist_id = playlist_link.split('/')[-1]
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id="38caf74efb5e4e5ba39bf377069c6201", client_secret= "268cbdbfeb2a47d5bad2daf65a7880c0"))
    
    playlist = sp.playlist_items(playlist_id)

    songs = playlist["tracks"]["items"]
    track_names = [song_info["track"]["name"] for song_info in songs]
    atrist_names = [song_info["track"]["artists"][0]["name"] for song_info in songs]

    return [" - ".join(elt) for elt in zip(track_names, atrist_names)]

def compare(song1: str, song2: str) -> bool:

    answer = str(input(f"{song1} (1) or {song2} (2): "))
    os.system("cls")
    return answer!="1"

def merge(left: list[str], right: list[str]) -> None:

    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):

        if not compare(left[left_index], right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result

def merge_sorted(arr: list[str]) -> list[str]:

    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sorted(left_half)
    right_half = merge_sorted(right_half)

    return merge(left_half, right_half)

if __name__=="__main__":

    playlist_link = str(input("Playlist Link: "))
    tracks = get_tracks_artists(playlist_link)

    random.shuffle(tracks)
    for song in merge_sorted(tracks):

        print(song)