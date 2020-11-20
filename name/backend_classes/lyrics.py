import name.backend_classes.genius_api_manager as genius_manager


class Lyrics(object):
    """A class which obtains a song's lyrics and can return
    all necessary information.
    """
    def __init__(self, song_name, song_artist):
        """Initializes the lyrics objects by getting information
        from the lyrics api manager
        song_name: name of the song
        song_artist: artist associated with the song
        """

        # Call the genius_api_manager and get lyrics
        lyrics_object = genius_manager.Genius_Api_Manager(song_name, song_artist)

        self.__song_lyrics = lyrics_object.search_for_lyrics()
        self.__song_name = song_name
        self.__song_artist = song_artist
        self.__num_words = 0
        self.__num_chorus = 0
        self.__num_verse = 0
        self.__variability_score = 0

    def get_lyrics(self):
        """Get song lyrics and return as a string"""

        return self.__song_lyrics

    def get_num_words(self):
        """Calculates the number of words in the song's lyrics and
        ignores any irrelevant headers
        """
        number_words = 0

        words = self.__song_lyrics.split()
        for word in words:
            if(word[0] is not "["):
                number_words += 1

        return number_words

    def get_num_verse(self):
        """Calculates the total number of verses in the song"""

        number_verses = 0

        words = self.__song_lyrics.split()
        for word in self.__song_lyrics:
            if("[Verse" in word):
                number_verses += 1

        return number_verses
    
    def get_num_chorus(self):
        """Calculates the total number of choruses in the song"""

        number_chorus = 0

        for word in self.__song_lyrics:
            if("[Chorus]" in word):
                number_chorus += 1

        return number_chorus

    def get_variability(self):
        """Calculates variability, whatever that means"""
        return 0

    def __analyze_lyrics(self):
        """Analyze the song using ancient esoteric methods"""
        return 0


