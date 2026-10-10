"""
Add the required parameters, type hints, meaningful docstrings, and implementation
according to the assignment specification.
"""

import math

from music_library import MusicLibrary
from track import Track


class MusicAnalyzer:
 
    def __init__(self, library: MusicLibrary) -> None:
        ''' 
         initialize a  library. 
         :param library: contains a music library with the tracks to analyse. 
         :returns: None. 
        '''
        self.library = library
 
    def feature_ranges(self) -> dict[str, tuple[float, float]]:
        ''' 
        Gets the minimum and the maximum values of the tracks.
        :parameter none 
        :returns: a dictionarie with the maximum and minimum values and a empty dictionarie if there is no track.
        '''
        ranges: dict[str, tuple[float, float]] = {}
        if not self.library.tracks:
            return {}
            
        energy_values: list[float]= [track.energy for track in self.library.tracks]
        minimum:float = min(energy_values)
        maximum:float = max(energy_values)
        ranges['energy'] = (minimum, maximum)
        danceability_values: list[float] = [track.danceability for track in self.library.tracks]
        minimum: float = min(danceability_values)
        maximum: float= max(danceability_values)
        ranges['danceability'] = (minimum, maximum)
        valence_value: list[float] = [track.valence for track in self.library.tracks]
        minimum: float= min(valence_value)
        maximum: float= max(valence_value)
        ranges['valence'] = (minimum, maximum)
        tempo_values: list[float] = [track.tempo for track in self.library.tracks]
        minimum: float = min(tempo_values)
        maximum: float = max(tempo_values)
        ranges['tempo'] = (minimum, maximum)
        loudness_values: list[float] = [track.loudness for track in self.library.tracks]
        minimum: float = min(loudness_values)
        maximum: float = max(loudness_values)
        ranges['loudness'] = (minimum, maximum)
        acousticness_value: list[float] = [track.acousticness for track in self.library.tracks]
        minimum: float= min(acousticness_value)
        maximum: float= max(acousticness_value)
        ranges['acousticness'] = (minimum, maximum)
        return ranges 
 
    def normalized_features(self, track_id: str) -> dict[str, float]:
        ''' 
        Normailizes the values of the features.
        :param track_id: Is the track_id with the feature names that are normalized. 
        :returns: A dictionarie with as key the feature name and as value the normalized float. 
        '''
        track = self.library.get_track(track_id)
        if track is None: 
            raise ValueError ('track not found')

        features: dict[str, float] = track.audio_features()
        ranges: dict[str, tuple[float, float]] = self.feature_ranges()
        normalized: dict[str, float] = {}
        for feature_name , value in features.items():
            minimum, maximum = ranges[feature_name]
            if minimum == maximum: 
                 normalized[feature_name] = 0.0 
         
            else: 
               normalized[feature_name] =(value- minimum) / (maximum - minimum)
        return normalized 


         
        
    def distance(self, track_id_a: str, track_id_b: str) -> float:
        ''' 
        Determines the distance between the values of two tracks. 
        :param track_id_a: Is the track id of track a. 
        :param track_id_b: Is the track id of track b. 
        :returns: the distance with a float. 
        '''
        track_a = self.library.get_track(track_id_a)
        track_b = self.library.get_track(track_id_b)
        if track_a is None or track_b is None:
            raise ValueError ('track not found')
        feature_a: dict[str, float] = self.normalized_features(track_id_a) 
        feature_b: dict[str, float] = self.normalized_features(track_id_b)
        distance: float = 0
        for feature in feature_a: 
             difference: float = feature_a[feature] - feature_b[feature]
             distance += difference**2 
        return math.sqrt(distance)



       
 
    def recommend(self, track_id: str, k: int) -> list[tuple[str, float]]:
        ''' 
        Recomends k numbers of tracks that are similar to the given track.
        :param track_id: Is the track id of the track where similar tracks are given for.
        :param k: Is the amount of similar tracks that are given. 
        :returns: A list with a tuple with the track id and a number how similar the track is. 
        '''
        track  = self.library.get_track(track_id)
        if track is None: 
            raise ValueError ('track is not found')
        
        if k < 0: 
            raise ValueError ( 'K can not be less than zero')
        recommendations: list[tuple[str, float]] = []
        for start_track in self.library.tracks:
            if start_track.track_id == track_id: 
                continue 
            distance = self.distance(start_track.track_id, track_id)
            recommendations.append((start_track.track_id, distance))
        recommendations = sorted(recommendations,key= lambda recommendation: (recommendation[1],recommendation[0]))
        recommendations = recommendations[:k]
        rounded_recommendations: list[tuple[str, float]] = []
        for start_track, distance in recommendations: 
            rounded_recommendations.append((start_track, round(distance,4)))

        return rounded_recommendations



