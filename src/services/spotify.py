from src.config import spotify_config
from requests import post, get
from requests.auth import HTTPBasicAuth


class SpotifyService:
    def __init__(self) -> None:
        self.web_api_url = spotify_config.WEB_API_URL
        self.auth_url = spotify_config.AUTH_URL
        self.auth = HTTPBasicAuth(
            spotify_config.CLIENT_ID, spotify_config.CLIENT_SECRET
        )
        self.token = self.get_token()
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_token(self) -> str:
        payload = {"grant_type": "client_credentials"}
        url = self.auth_url + "/api/token"
        response = post(url=url, auth=self.auth, data=payload)

        response.raise_for_status()
        return response.json()["access_token"]

    def get_user_playlists(self, user_id: str):
        endpoint = f"/users/{user_id}/playlists"
        url = self.web_api_url + endpoint

        response = get(url=url, headers=self.headers)
        response.raise_for_status()

        playlists_response = response.json()
        playlists = playlists_response["items"]
        return playlists

    def get_playlist_tracks(self, playlist_id: str):
        endpoint = f"/playlists/{playlist_id}/tracks"
        url = self.web_api_url + endpoint
        params = {"fields": "items(track(name,album(name),artists(name)))"}
        response = get(url=url, headers=self.headers, params=params)
        response.raise_for_status()

        playlist_response = response.json()
        playlist_tracks = playlist_response["items"]

        return playlist_tracks
