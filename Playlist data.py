import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import pandas

# Scope
scope = 'playlist-read-collaborative'
# The important parts
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                               redirect_uri=cred.redirect_url, scope=scope))


# The playlist we are searching
# ('1139152559','5mR91NXn5HGXe7PVZhhRby')

def analyze_playlist(user_name, playlist_id):
    # Here we make an empty data frame with the variables we wish to store, these are pre-defined
    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]

    # Create the dataframe with panda
    playlist_df = pandas.DataFrame(columns=playlist_features_list)

    # Loop through every track on the playlist, extract features and append the features to the playlist_df

    playlist = sp.user_playlist_tracks(user_name, playlist_id)['items']
    for track in playlist:
        # Create empty dict to store the data
        playlist_features = {}

        # Collect the metadata
        playlist_features['artist'] = track['track']['album']['artists'][0]['name']
        playlist_features['album'] = track['track']['album']['name']
        playlist_features['track_name'] = track['track']['name']
        playlist_features['track_id'] = track['track']['id']

        # Get the audio features
        audio_features = sp.audio_features(playlist_features['track_id'])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]

        # Concatenate the dfs
        track_df = pandas.DataFrame(playlist_features, index=[0])
        playlist_df = pandas.concat([playlist_df, track_df], ignore_index=True)

    return playlist_df


data = analyze_playlist('1139152559', '5mR91NXn5HGXe7PVZhhRby')
print(data.head())

