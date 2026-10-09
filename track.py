"""
Add the required parameters, type hints, meaningful docstrings, and implementation
according to the assignment specification.
"""

class Track:

    def __init__( 
        self,
        track_id:str,
        artists:str,
        track_name:str,
        genre:str,
        mood:str,
        duration_category:str,
        danceability:float,
        energy:float,
        valence:float,
        tempo:float,
        loudness:float,
        acousticness:float,
        duration_ms:int,
        popularity:int
        ) -> None:
        self.track_id:str = track_id    
        self.artists:str = artists
        self.track_name:str = track_name
        self.genre:str = genre
        self.mood:str = mood
        self.duration_category:str = duration_category
        self.danceability:float = danceability
        self.energy:float = energy
        self.valence:float = valence
        self.tempo:float = tempo
        self.loudness:float = loudness
        self.acousticness:float = acousticness
        self.duration_ms:int = duration_ms
        self.popularity:int = popularity
        # raise NotImplementedError 

    def __str__(self) -> str:
        """ 
        This function gives information in some given format for given song.
        :param self: the object itself
        Returns a string.
        """
        return f"TrackID: {self.track_id}, Title: {self.track_name}, Artist: {self.artists}, Genre: {self.genre}"
        # raise NotImplementedError

    def artist_names(self) -> list[str]:
        # raise NotImplementedError
        return [artist.strip() for artist in self.artists.split(";")]

    def audio_features(self) -> dict[str, float]:
        # raise NotImplementedError
        return {
            "danceability": self.danceability,
            "energy": self.energy,
            "valence": self.valence,
            "tempo": self.tempo,
            "loudness": self.loudness,
            "acousticness": self.acousticness
        }
