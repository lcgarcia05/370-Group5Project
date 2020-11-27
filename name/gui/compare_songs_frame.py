""" Compare songs frame corresponding to the storyboards page 2
"""
import tkinter as tk

from .home_page_frame import HomePageFrame
from name.backend_classes.checking_song_similarity import CheckingSongSimilarity

class CompareSongsFrame(HomePageFrame):
    """ TODO: fill in

    Args:
        tk ([type]): TODO: fill in
    """
    def __init__(self, parent, container):
        super().__init__(parent, container)
        self.container = container
        self.parent = parent

    def grid_forget(self):
        super().grid_forget()
        self.get_stats_button.grid_forget()

    def init_upper_grid(self):
        super().init_upper_grid()
        self.compare_songs_button["state"] = tk.DISABLED
        self.create_playlist_button["state"] = tk.NORMAL

    def init_lower_grid(self):
        super().init_lower_grid()
        self.similar_songs_button.grid_forget()

        self.get_stats_button = tk.Button(self.lower_grid, command=self.song_stats_cmd)
        self.get_stats_button["text"] = "Get Stats"
        self.get_stats_button.grid(row=0, column=2)

    def song_stats_cmd(self):
        """ command for song stats btn
        """
        self.switch_frame("Song Stats")

        # Return similarities of the two or more selected songs
        self.formatted_filters = self.convert_filters_list(self.selected_filters)
        sim_scores_obj = CheckingSongSimilarity(self.formatted_filters)
        sim_score = sim_scores_obj.get_songs_similarity_score(self.song_object_list)

        # Update the srcolledText widget in the song stats frame with the
        # returned data
        d = [int(sim_score), self.song_object_list]
        print(int(sim_score))
        self.parent.frames[self.parent.get_frame_id("Song Stats")].display_data(d)
