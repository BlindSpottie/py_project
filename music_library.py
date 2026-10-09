"""
Add the required parameters, type hints, meaningful docstrings, and implementation
according to the assignment specification.
"""

import csv
from typing import Optional

from track import Track 

correct_Genres= {"Pop","Rock","Metal", "Hip-Hop", "Electronic", "Jazz","Soul","Folk","Country","Latin","World","Classical"}
correct_mood= {"Sad","Neutral","Happy"}
correct_duration_category= {"Short","Medium","Long"}

Text_Fields = ["track_id","artists",'track_name'] 
Unit_Floats = ["danceability","energy", "valence","acousticness"] #needs to be between 0.0 and 1.0
All_Fields = (Text_Fields + ["genre","mood","duration_category"] + Unit_Floats + ["tempo","loudness","duration_ms","popularity"])

class MusicLibrary:
 
    def __init__(self) -> None:
       ''' 
       initialize a musiclibrary with a empty list. 
       '''
       self.tracks = []
 
#       Helper Methods for validation rules
    def _header_normalize_validation(self,header:str) -> str:
        """
        makes a header lowercase and replace hyphen and spaces with underscores.
        eg: track-name -> track_name and track name -> track_name
        """
        return header.strip().lower().replace("-","_").replace(" ","_")

    def _normalize_category(self,value:str)->str:
        """ 
        Takes the value, strips it, makes it all lowercase and capitalizes the first letter of that word
        eg: hiP hOp -> Hip Hop
        """
        return value.strip().lower().title()

    def _txt_to_float(self, value:str) -> float:
        number = float(value)
        if number != number or number in (float("inf"),float("-inf")): #first checks for nan (not a number), second checks for inf or -inf values (normally inf and -inf will not give error)
            raise ValueError("Not a valid number")
        return number

    def _check_row(self,row:dict):
        """Checks if row is valid, if row is valid it returns the track, otherwise return None"""

        if None in row or any(row.get(i) is None for i in All_Fields):
            return None

        track_id = row["track_id"].strip()
        artists = row["artists"].strip()
        track_name = row["track_name"].strip()

        if track_id == "" or artists == "" or track_name == "":
            return None 

        genre = self._normalize_category(row["genre"]) #this turns the csv row to validated things, so pOp -> Pop etc.
        mood = self._normalize_category(row["mood"])
        duration_category = self._normalize_category(row["duration_category"])

        if (genre not in correct_Genres or mood not in correct_mood or duration_category not in correct_duration_category):
            return None

        try:
            unit = {i: self._txt_to_float(row[i]) for i in Unit_Floats}
            tempo = self._txt_to_float(row["tempo"])
            loudness = self._txt_to_float(row["loudness"])  
            duration_ms = int(row["duration_ms"])
            popularity = int(row["popularity"])

        except (ValueError,TypeError):
            return None

        if not all(0.0 <= v <= 1.0 for v in unit.values()):
            return None
        if tempo <= 0 or duration_ms <=0:
            return None
        if not 0 <= popularity <= 100:
            return None
            
        return Track(
            track_id = track_id,
            artists = artists,
            track_name = track_name,
            genre = genre,
            mood = mood,
            duration_category = duration_category,
            danceability = unit["danceability"],
            energy = unit["energy"],
            valence = unit["valence"],
            tempo = tempo,
            loudness = loudness,
            acousticness = unit["acousticness"],
            duration_ms = duration_ms,
            popularity = popularity,
        )



#"tempo","loudness","duration_ms","popularity"


    def load_from_csv(self, path: str) -> None:
        ''' 
        Loads the document. 
        :param path: is the path to the document.
        :return None
        '''
        self.tracks = []
        # path='data/spotify_tracks.csv'
        with open(path, newline="") as file_out:
            reader = csv.DictReader(file_out)
    
            reader.fieldnames = [self._header_normalize_validation(k) for k in (reader.fieldnames or [])]
            rows = list(reader)
         
        seen_ids = set()
        duplicate_ids = set()

        # find which track_ids appear more than once
        for row in rows:
            track_id = row.get("track_id")
            if track_id is None:
                continue
            track_id = track_id.strip()

            if track_id in seen_ids:
                duplicate_ids.add(track_id)
            else:
                seen_ids.add(track_id)

        # skip row that is double
        for row in rows:
            track_id = row.get("track_id")
            if track_id is None:
                continue
            track_id = track_id.strip()

            if track_id in duplicate_ids:
                continue

            track = self._check_row(row)
            if track is not None:
                self.tracks.append(track)


         
        # for row in reader: 
        #     # print(row)
        #     try:
        #         track = Track(
        #         duration = int(row['duration_ms']),
        #         popularity = int(row['popularity']),
        #         danceability = float(row['danceability']),
        #         energy = float(row['energy']),
        #         valence = float(row['valence']),
        #         tempo = float(row['tempo']),
        #         loudness = float(row['loudness']),
        #         acousticness = float(row['acousticness']),
        #         duration_category = str(row['duration_category']),
        #         mood =  str(row['mood']),
        #         genre = str(row['genre']),
        #         track_name = str(row['track_name']),
        #         artist = str(row['artist']),
        #         track_id = str(row['track_id']),
        #         )
        #     except(ValueError,KeyError):
        #         continue

        #     print(Track)

#class track: 
#     def __init__(self, duration, popularity, danceability, energy, valence, tempo, loudness, acousticness, duration_category, mood, genre, track_name, artist, track_id ):
#         self.duration = duration 
#         self.popularity = popularity
#         self.danceability = danceability
#         self.energy = energy
#         self.valence = valence 
#         self.tempo = tempo 
#         self.loudness = loudness
#         self.acousticness = acousticness
#         self.duration_category = duration_category
#         self.mood = mood
#         self.genre = genre
#         self.track_name = track_name
#         self.artist = artist
#         self.track_id = track_id

#         track = Track(duration, popularity, danceability, energy, valence, tempo, loudness, acousticness, duration_category, mood, genre, track_name, artist, track_id)
#         self.tracks = []
#         self.tracks.append(track)



 
    def __len__(self) -> int:
       ''' 
       Returns the number of stored tracks. 
       :return integer of stored tracks. 
       '''
       return len(self.tracks)
        
 
    def get_track(self, track_id: str) -> Optional[Track]:
        ''' 
        Looks if there is a track with the same track id. 
        :param track_id is a track id from a track as str
        :returns the track object if there is a track found. 
        '''
        for track in self.tracks: 
            if track.track_id == track_id:
                return track

        return None 
      


