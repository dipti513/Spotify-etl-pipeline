import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from datetime import datetime
import os
from config.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''
os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''


def extract_spotify_data():
    """
    Fetches data using the Search API.
    """
    try:
        client_credentials_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID, 
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        print("🔍 Searching for top tracks from 2024...")
        results = sp.search(q='year:2024', type='track', limit=50, market='US')
        
        song_list = []
        for item in results['tracks']['items']:
            song_data = {
                'track_id': item['id'],
                'track_name': item['name'],
                'artist_name': item['artists'][0]['name'], 
                'album_name': item['album']['name'],
                'popularity': item['popularity'],
                'duration_ms': item['duration_ms'],
                'explicit': item['explicit'],
                'extracted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            song_list.append(song_data)

        df = pd.DataFrame(song_list)
        
        print(f"✅ Success: Extracted {len(df)} rows using Search API.")
        return df
        
    except Exception as e:
        print(f"❌ Error in extract_spotify_data: {e}")
        return None

if __name__ == "__main__":
    extract_spotify_data()
