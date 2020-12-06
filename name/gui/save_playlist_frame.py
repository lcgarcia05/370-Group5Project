""" TODO: fill in
"""
import tkinter as tk
from tkinter import StringVar

from .member_home_frame import MemberHomeFrame


class SavePlaylistFrame(MemberHomeFrame):
    """ TODO: fill in

    Args:
        tk ([type]): TODO: fill in
    """

    def grid_unmap(self):
        super().grid_unmap()
        self.new_list_entry.grid_remove()
        self.cancel_button.grid_remove()
        self.save_playlist_button.grid_remove()

    def grid_remember(self):
        super().grid_remember()
        self.get_song_info_button.grid_remove()
        self.find_similar_songs_button.grid_remove()
        self.latest_playlist_button.grid_remove()
        self.all_playlists_button.grid_remove()
        self.listening_habits_button.grid_remove()

        self.new_list_entry.grid()
        self.cancel_button.grid()
        self.save_playlist_button.grid()

    def init_lower_grid(self):
        super().init_lower_grid()

        self.cancel_button = tk.Button(
            self.lower_grid,
            text="Cancel",
            command=self.cancel_command)
        self.cancel_button.grid(row=0, column=0)


        container = tk.Frame(self.lower_grid)
        container.grid(row=0, column=2)

        self.new_list_entry = tk.Entry(container)
        self.new_list_entry.insert(0, "New Playlist Name")
        self.new_list_entry.grid(row=0, column=0)

        self.save_playlist_button = tk.Button(
            container,
            text="Save to Spotify",
            command=self.save_playlist_command)
        self.save_playlist_button.grid(row=0, column=1)

    def cancel_command(self):
        """command for the cancel button
        """
        self.switch_frame("All Playlists")

    def save_playlist_command(self):
        """command for the create similar playlist button
        """
        if self.new_list_entry.get() != "New Playlist Name":
            # assemble a playlist object
            json_plylst = {
                "name": self.new_list_entry.get(),
                "owner": { "id": self.user.spotify_id },
                "id": self.user.spotify_id,
                "tracks": { "total": len(self.parent.song_object_list)}
            }
            if self.user.save_playlist_to_spotify(json_plylst, self.parent.song_object_list) is not None:
                tk.messagebox.showinfo(title="Success", message="The playlist was saved to " +
                    "your spotify account")
            else:
                print("error")