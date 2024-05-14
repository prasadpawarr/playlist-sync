from pydantic import BaseModel
from ..constants import Platform


class PlaylistCreateModel(BaseModel):
    source_platform: Platform = Platform.SPOTIFY
    source_user: str
    
    destination_platform: Platform = Platform.YTMUSIC
    destination_user: str


    