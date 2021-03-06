lib_ibroadcast
==============

A simple command line script with helper functions, developed for convenient creation of playlists

Usage:

.. code-block:: python

    from lib_ibroadcast import ciBroadCast
    oiBroadCast = ciBroadCast()
    oiBroadCast.Login(uUserName='your ibroadcast email',uPassword='ypur ibroadcast password')
    # uncomment one or both
    # oiBroadCast.SelectAlbumsByAlbumName(uFilter='Metal-Hard Rock Covers*')
    # oiBroadCast.SelectTracksByFolder(uFolder='Musik/Full Albums/Sampler')
    oiBroadCast.CreatePlayList(uName='My Playlist',uDescription='My Playlist Description',bPublic=False)
    oiBroadCast.Logout()

Requirements:
- Python 3.8 minimum
- Requests library

Functions:
- InitLogger: Initializes the python logger. Can be subclassed if required
- Login: Logon to iBroadcast with your given credentials
- Logout: as it says
- GetLibrary: Reads the user library from iBroadcast
- SelectTracksByFolder: Selects all songs/track withi a given folder or part of the folder tree
- SelectAlbumsByAlbumName: Select all albums with a given album name. Basic wildcard match (*/?) is supported
- CreatePlayList: Creates a playlist from the selected albums or songs
- DeletePlayList: Deletes a playlist, not working by now

Limitations:

It is designed to perform instructions straight forward. Changes to the library or not refreshed after a change
This hasn't been heavily tested , but works fine for me





