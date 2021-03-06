from lib_ibroadcast import ciBroadCast

oiBroadCast = ciBroadCast()
oiBroadCast.Login(uUserName='your ibroadcast email',uPassword='ypur ibroadcast password')
# uncomment one or both
# oiBroadCast.SelectAlbumsByAlbumName(uFilter='Metal-Hard Rock Covers*')
# oiBroadCast.SelectTracksByFolder(uFolder='Musik/Full Albums/Sampler')
oiBroadCast.CreatePlayList(uName='My Playlist',uDescription='My Playlist Description',bPublic=False)
oiBroadCast.Logout()

