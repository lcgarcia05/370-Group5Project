""" TODO: fill in
"""
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from .name_frame import NameFrame

from name.backend_classes.persistent_storage import PersistentStorage


class GroupHomeFrame(NameFrame):
    """ TODO: fill in

    Args:
        tk ([type]): TODO: fill in
    """
    def __init__(self, parent, container, user):
        super().__init__(parent, container, user)

    def grid_unmap(self):
        super().grid_unmap()
        self.edit_playlist_button.grid_remove()
        self.save_playlist_button.grid_remove()
        self.playlist_dropdown.grid_remove()
        self.new_playlist_button.grid_remove()
        self.group_song_stats_button.grid_remove()
        self.edit_group_button.grid_remove()

    def grid_remember(self):
        super().grid_remember()
        self.edit_playlist_button.grid()
        self.save_playlist_button.grid()
        self.playlist_dropdown.grid()
        self.new_playlist_button.grid()
        self.group_song_stats_button.grid()
        self.edit_group_button.grid()

        self.display_data(self.parent.song_object_list)

        ps = PersistentStorage(self.user.spotify_id)
        playlists = ps.get_group_playlists(self.parent.active_group.group_id)

        print(playlists)

    def display_data(self, song_list):
        """display the given song list in the latest playlist treeview

        Args:
            song_list (list): list of songs that will appear in the treeview
        """
        # clear the treeview first to avoid ghosting
        self.song_treeview.delete(*self.song_treeview.get_children())
        artists_string_list = []
        for song in song_list:
            for artist in song.song_artist:
                artists_string_list.append(artist.name)
            artists_string = ", ".join(artists_string_list)

            artists_string_list.clear()

            self.song_treeview.insert("", "end", values=(song.song_name,
                                        song.album_details.name, artists_string))

    def init_lower_grid(self):
        super().init_lower_grid()

        self.edit_playlist_button = tk.Button(
            self.lower_grid,
            text="Edit",
            command=self.edit_playlist_command
        )
        self.edit_playlist_button.grid(row=0, column=0, sticky="e")

        self.save_playlist_button = tk.Button(
            self.lower_grid,
            text="Save to group",
            command=self.save_playlist_command
        )
        self.save_playlist_button.grid(row=0, column=1, sticky="w")

    def init_middle_grid(self):
        super().init_middle_grid()

        self.song_treeview = ttk.Treeview(self.middle_grid)
        self.song_treeview["columns"] = ("Title", "Album", "Artist")

        # set up widths of columns
        self.song_treeview.column("#0", width=1, minwidth=1, stretch="no")
        self.song_treeview.column("Title", width=300, minwidth=300, stretch="yes")
        self.song_treeview.column("Album", width=150, minwidth=150, stretch="yes")
        self.song_treeview.column("Artist", width=150, minwidth=150, stretch="yes")

        #set up headings for the columns
        self.song_treeview.heading("Title", text="Title", anchor="w")
        self.song_treeview.heading("Album", text="Album", anchor="w")
        self.song_treeview.heading("Artist", text="Artist(s)", anchor="w")
        self.song_treeview.grid(row=0, column=0, sticky="nsew")

        container_1 = tk.Frame(self.middle_grid)
        container_1.grid(row=0, column=2, sticky="n")

        self.group_song_stats_button = tk.Button(
            container_1,
            text="Get Group\nSong Stats",
            command=self.group_song_stats_command)
        self.group_song_stats_button.grid(row=0, column=0)

        self.edit_group_button = tk.Button(
            container_1,
            text="Edit\nGroup",
            command=self.edit_group_command
        )
        self.edit_group_button.grid(row=1, column=0)

    def init_upper_grid(self):
        super().init_upper_grid()
                # TODO: add the proper filters to the dropdown list
        container_0 = tk.Frame(self.upper_grid)
        container_0.grid(row=1, column=1)

        self.l_group_name = tk.Label(container_0)
        self.l_group_name.grid(row=0, column=1)
        self.l_group_name.configure(font=("Helvetica BOLD", 18))

        self.l_playlist_select = tk.Label(container_0, text="Playlist Select:")
        self.l_playlist_select.grid(row=1, column=0)

        variable = StringVar(container_0)
        variable.set("Last Created Playlist") # default value
        self.playlist_dropdown = tk.OptionMenu(
            container_0,
            variable,
            "Last Created Playlist",
            "playlist 1",
            "playlist 2",
            "playlist 3",
            command=self.playlist_dropdown_command)
        self.playlist_dropdown.grid(row=1, column=1)

        self.new_playlist_button = tk.Button(
            container_0,
            text="New Playlist",
            command=self.new_playlist_command
        )
        self.new_playlist_button.grid(row=1, column=2)

    def display_group(self, group):
        self.parent.active_group = group
        self.l_group_name["text"] = group.group_name

    def edit_playlist_command(self):
        """ command for the edit playlist button
        """
        self.switch_frame("Edit Group Playlist")

    def edit_group_command(self):
        """ comamnd for the edit group button
        """
        self.switch_frame("Edit Group")
        id = self.parent.get_frame_id("Edit Group")
        self.parent.frames[id].display_group(self.parent.active_group)

    def group_song_stats_command(self):
        """ command for the get group song stats button
        """
        self.switch_frame("Group Stats")

    def new_playlist_command(self):
        """ command for the new playlist button command
        """
        self.switch_frame("Edit Group Playlist")

    def playlist_dropdown_command(self):
        """ command for the playlist dropdown
        """
        return 1

    def save_playlist_command(self):
        """ command for the save playlist button
        """
        self.switch_frame("Save Playlist")
