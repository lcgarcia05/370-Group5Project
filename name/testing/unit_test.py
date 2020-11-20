import os
import time
import pytest
from proof_of_concept import Playlist
from proof_of_concept import Song
from proof_of_concept import User
# as we work on our app going forward, import classes from the appropriate folder(s)
from name.backend_classes import SongSimilarity
from name.backend_classes import SpotifyAPIManager


# Tests for the User class
def test_setUserType_v1():
    """
    Test ID: User01. Normally setUserType would be called from within the Spotify API
    after a User has linked/ unlinked their account. For this unit test, we simply check that
    the User type is modified correctly.
    """
    user = User(type="Guest")
    user.setUserType(type="Member")

    assert user.type == "Member"


def test_setUserType_v2():
    """
    Test ID: User02. Check that the user type is updated correctly from "Member" to "Guest".
    """
    user = User(type="Member")
    user.setUserType(type="Guest")

    assert user.type == "Guest"


def test_isGuest_v1():
    """
    Test ID: User03. Check that the method returns True when the User type is Guest.
    """
    user = User(type="Guest")
    assert user.isGuest() == True


def test_isGuest_v2():
    """
    Test ID: User04. Check that the method returns False when the User type is not Guest.
    """
    user = User(type="Member")

    assert user.isGuest() == False


# Tests for the SongSimilarity class
def test_compare_all():
    """ Test ID: SongSim01. Check that the method
    returns a value between 0 and 1.
    """
    songSimilarityCalculator = SongSimilarity(["exampleSong"], ["duration_ms"])
    result = songSimilarityCalculator.compare_all()

    assert (result >= 0 and result <= 1)


# Tests for the SpotifyAPIManager class
def test_linkSpotifyAccount():
    """ Test ID: Spotify14. Tests that the method returns
    True when valid credentials are provided, False if authorization
    is cancelled.
    """
    spotifyAPIManager = SpotifyAPIManager()
    print("Enter these valid credentials into the popup window:")
    print("email: cmpt370.group5@gmail.com")
    print("password: pennywise_1640")
    result = spotifyAPIManager.link_spotify_account()
    assert result == True


def test_get_user_id_v1():
    """ Test ID: Spotify08. Tests that the method returns
    None when the user is not logged in to Spotify.
    """
    spotifyAPIManager = SpotifyAPIManager()
    result = spotifyAPIManager.get_user_id()
    assert result == None


def test_get_user_id_v2():
    """ Test ID: Spotify07. Should return the current member
    ID when logged in to Spotify. 
    """
    # wait a second before running this test so that the API
    # doesn't reject the connection
    time.sleep(2)
    spotifyAPIManager = SpotifyAPIManager()
    account_link = spotifyAPIManager.link_spotify_account()
    assert account_link == True
    result = spotifyAPIManager.get_user_id()
    # the user id for the cmpt370 spotify account
    assert result == "vha6pttyppu7tnrc0l1j4k4de"
    # in the last test, clear the cache
    clear_cache()


# Cleanup
def clear_cache():
    """ delete the cache """
    if os.path.exists(".cache"):
        os.remove(".cache")
    else:
        print("The file does not exist")
