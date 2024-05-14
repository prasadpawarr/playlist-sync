from pydantic_settings import BaseSettings, SettingsConfigDict


class SpotifyConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="SPOTIFY_")
    AUTH_URL: str = "https://accounts.spotify.com"
    WEB_API_URL: str = "https://api.spotify.com/v1"
    CLIENT_ID: str = "fake_id"
    CLIENT_SECRET: str = "fake_secret"


spotify_config = SpotifyConfig()
