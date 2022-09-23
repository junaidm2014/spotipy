import os
import argparse as args
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyBrowser:

    def __init__(self, client_id, client_secret):
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.counter = 0

    def print_playlist_tracks(self, playlist_uri):
        playlist = self.spotify.playlist(playlist_uri)
        playlist_name = playlist['name']
        songs = playlist['tracks']
        for song in songs['items']:
            album = song['track']['album']
            track = song['track']
            album = track['album']
            album_name = album['name']
            artists_list = []
            for artist in track['artists']:
                artists_list.append(artist['name'])
            song_name = track['name']
            self.counter = self.counter + 1
            to_print = ','.join([str(self.counter), playlist_name, song_name, ' '.join(artists_list), album_name])
            print(to_print)

    def print_all_data(self, user_playlists):
        for playlist_item in user_playlists['items']:
            x.print_playlist_tracks(playlist_item['uri'])

    def get_user_playlists(self, user):
        return self.spotify.user_playlists(user)


if __name__ == "__main__":
    parser = args.ArgumentParser(description='Get all my Spotify Playlists. You will need your client id, client '
                                             ' secret and spotify username and it will pull your '
                                             'play list, song name, artist(s) and album')
    parser.add_argument('-c', '--client_id', dest='client_id', type=str)
    parser.add_argument('-s', '--client_secret', dest='client_secret', type=str)
    parser.add_argument('-u', '--user', dest='user_name', type=str)
    arguments = parser.parse_args()

    x = SpotifyBrowser(arguments.client_id, arguments.client_secret)
    user_playlists = x.get_user_playlists(user=arguments.user_name)
    x.print_all_data(user_playlists)
