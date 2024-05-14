from fastapi import APIRouter, status
from ..models.playlists import PlaylistCreateModel
from ..services.spotify import SpotifyService
from ..constants import Platform

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/{playlist_name}", status_code=status.HTTP_201_CREATED, summary="Create a playlist"
)
def create_playlist(playlist_name: str, payload: PlaylistCreateModel):
    src_platform = payload.source_platform
    dest_platform = payload.destination_platform
    src_user = payload.source_user

    if src_platform == dest_platform:
        raise Exception("Source and Destination platforms cannot be same!")

    if src_platform == Platform.SPOTIFY:
        svc = SpotifyService()

        playlists = svc.get_user_playlists(user_id=src_user)
        for playlist in playlists:
            if playlist["name"].lower() == playlist_name.lower():
                playlist_id = playlist["id"]
                break
        else:
            raise Exception(f"Playlist {playlist["name"]} not found on {src_platform}!")

        tracks = svc.get_playlist_tracks(playlist_id=playlist_id)
        return tracks

    
    # get spotify playlist details
    # create new yt music playlist
    # for each spotify song:
    # search in yt
    # if found: add else: skip

    # playlists = spotify.get_user_playlists(user_id=playlist.from_user)
    # return playlists
