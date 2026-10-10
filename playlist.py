"""
Add the required parameters, type hints, meaningful docstrings, and implementation
according to the assignment specification.
"""

import math

from music_analyzer import MusicAnalyzer
from typing import Optional
from track import Track


class Playlist:
 
    def __init__(self, tracks: list[Track]) -> None:
       ''' 
        Initialize tracks. 
        :param tracks: Contains a list with tracks. 
        :returns: None.
       '''
       self.tracks: list[Track] = tracks 
 
    @staticmethod
    def generate_playlist(analyzer: MusicAnalyzer, seed_track_id: str, length: int) -> "Playlist":

        ''' 
        Generates a playlist with songt most alike to seed_track_id. 
        :param analyzer: A musicAnalyzer to analyse the songs to determine the distance.
        :param seed_track_id: Is the track_id of the track where similar track are searched for.
        :param length: Is the amount of tracks in the playlist.
        :returns: a playlist. 
        '''
        playlist_tracks: list[Track] = []
        track = analyzer.library.get_track(seed_track_id)
        if track is None: 
            raise ValueError ('track not found')
        else:
            playlist_tracks.append(track)
        if length  < 1:
            raise ValueError('invaled length')
        while len(playlist_tracks) < length: 
            
            
            last_track = playlist_tracks[-1]
            smallest_distance: float = float('inf')
            best_track = None 
            for candidate in analyzer.library.tracks:
                if candidate in playlist_tracks: 
                    continue
                distance: float = analyzer.distance(last_track.track_id, candidate.track_id)
                if distance < smallest_distance: 
                    smallest_distance = distance
                    best_track = candidate 
                elif distance == smallest_distance and candidate.track_id < best_track.track_id:
                    best_track = candidate


        
            if best_track is None: 
                break 
            playlist_tracks.append(best_track)
        return Playlist(playlist_tracks)

    





       
 
    def total_duration(self) -> int:
        ''' 
        Counts the total duration of the playlist. 
        :returns: a int of the duration of the playlist.
        '''
        total: int = 0 
        for track in self.tracks:
            total += track.duration_ms
        return total 
      
 
    def feature_averages(self) -> dict[str, float]:
        ''' 
        Determines the average values of the features in the playlist en puts them in a dictionary. 
        :returns: A dictionary with the features as keys and their average as values.
        '''

        averages: dict[str, float] = {}

        
        feature_names = ["danceability", "energy","valence","tempo","loudness", "acousticness"]
        for feature in feature_names: 
             feature_values: list[float] = []
             if self.tracks == []: 
                 return {}
             for track in self.tracks: 
                 features: dict[str, float]= track.audio_features(track.track_id)
                 feature_values.append(features[feature])
             total_feature: float = sum(feature_values)
             average_feature: float = round(total_feature/len(feature_values), 3)
        
             averages[feature] = average_feature
        return averages 



        
 
    def popularity_statistics(self) -> dict[str, float]:
      ''' 
      calculates statistics about popularity. 
      :returns: a dictionary with as keys mean, median and std_dev and as values their calculated values. 
      '''
      popularity: list[int] = []
      if self.tracks == []:
          return {}
      for track in self.tracks: 
          popularity.append(track.popularity)
      mean: float = round(sum(popularity)/len(popularity), 1)
      median: float = self._median(popularity)
      standard_deviation: float =  round(self._std_dev(popularity), 1)
      popularity_numbers: dict[str, float] = {}
      popularity_numbers['mean'] = mean
      popularity_numbers['median'] = median
      popularity_numbers['std_dev'] = standard_deviation
      return popularity_numbers

         
          
 
    def dominant_mood(self) -> Optional[str]:
        ''' 
        Determines the mood that is most common in playlist. 
        :returns: None or the mood happy, sad or neutral. 
        '''
        mood: list[str] = []
        if self.tracks == []: 
            return None 
        for track in self.tracks: 
            mood.append(track.mood)
        happy_amount: int =  mood.count('Happy')
        sad_amount: int =mood.count('Sad')
        neutral_amount: int = mood.count('Neutral')
        most_common: int = max(happy_amount, sad_amount,neutral_amount)
        for i in mood: 
             if mood.count(i) == most_common: 
                   return i

        
 
    def artist_variety(self) -> int:
        ''' 
        Counts the amount of unique artist in the playlist. 
        :returns: A int of the amount of unique artist. 
        '''
        
        count_artist: set[str] = set()
        for track in self.tracks:
            artist: list[str] = track.artist_names()
            for i in artist: 
                count_artist.add(i)
        return len(count_artist)


 
    def _median(self, values: list[float]) -> float:
        ''' 
        Makes a formula to calculate the median. 
        :param values: a list of floats where the median is calculated from. 
        :returns: the median of the list rounded to one decimal. 
        '''
        if len(values) % 2 == 0: 
            values.sort()
            index_1: int = len(values) // 2
            index_2: int = len(values) // 2 -1 
            median : float = round((values[index_1] + values[index_2]) / 2, 1)
        else:
            values.sort()
            index: int = len(values)// 2
            median: float = float(values [index])
        return median
        
 
    def _std_dev(self, values: list[float]) -> float:
        """Return the sample standard deviation of the values (provided helper)."""
        count = len(values)
 
        if count < 2:
            return 0.0
 
        mean = sum(values) / count
        total = 0.0
 
        for value in values:
            difference = value - mean
            total = total + difference ** 2
 
        variance = total / (count - 1)
 
        return math.sqrt(variance)   
