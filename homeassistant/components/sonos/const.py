"""Const for Sonos."""
from __future__ import annotations

import datetime

from homeassistant.components.media_player import MediaClass, MediaType
from homeassistant.const import Platform

UPNP_ST = "urn:schemas-upnp-org:device:ZonePlayer:1"

DOMAIN = "sonos"
DATA_SONOS = "sonos_media_player"
DATA_SONOS_DISCOVERY_MANAGER = "sonos_discovery_manager"
PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.MEDIA_PLAYER,
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.SWITCH,
]

SUB_FAIL_ISSUE_ID = "subscriptions_failed"
SUB_FAIL_URL = "https://www.home-assistant.io/integrations/sonos/#network-requirements"

SONOS_ARTIST = "artists"
SONOS_ALBUM = "albums"
SONOS_PLAYLISTS = "playlists"
SONOS_GENRE = "genres"
SONOS_ALBUM_ARTIST = "album_artists"
SONOS_TRACKS = "tracks"
SONOS_COMPOSER = "composers"
SONOS_RADIO = "radio"
SONOS_OTHER_ITEM = "other items"

SONOS_STATE_PLAYING = "PLAYING"
SONOS_STATE_TRANSITIONING = "TRANSITIONING"

EXPANDABLE_MEDIA_TYPES = [
    MediaType.ALBUM,
    MediaType.ARTIST,
    MediaType.COMPOSER,
    MediaType.GENRE,
    MediaType.PLAYLIST,
    SONOS_ALBUM,
    SONOS_ALBUM_ARTIST,
    SONOS_ARTIST,
    SONOS_GENRE,
    SONOS_COMPOSER,
    SONOS_PLAYLISTS,
]

CONTAINER_ALBUM_MUSICALBUM = "object.container.album.musicAlbum"
CONTAINER_GENRE_MUSICGENRE = "object.container.genre.musicGenre"
CONTAINER_PERSON_COMPOSER = "object.container.person.composer"
CONTAINER_PERSON_MUSICARTIST = "object.container.person.musicArtist"
CONTAINER_PLAYLISTCONTAINER_SAMEARTIST = "object.container.playlistContainer.sameArtist"
CONTAINER_PLAYLISTCONTAINER = "object.container.playlistContainer"
ITEM_AUDIOITEM_MUSICTRACK = "object.item.audioItem.musicTrack"

SONOS_TO_MEDIA_CLASSES = {
    SONOS_ALBUM: MediaClass.ALBUM,
    SONOS_ALBUM_ARTIST: MediaClass.ARTIST,
    SONOS_ARTIST: MediaClass.CONTRIBUTING_ARTIST,
    SONOS_COMPOSER: MediaClass.COMPOSER,
    SONOS_GENRE: MediaClass.GENRE,
    SONOS_PLAYLISTS: MediaClass.PLAYLIST,
    SONOS_TRACKS: MediaClass.TRACK,
    CONTAINER_ALBUM_MUSICALBUM: MediaClass.ALBUM,
    CONTAINER_GENRE_MUSICGENRE: MediaClass.PLAYLIST,
    CONTAINER_PERSON_COMPOSER: MediaClass.PLAYLIST,
    CONTAINER_PERSON_MUSICARTIST: MediaClass.ARTIST,
    CONTAINER_PLAYLISTCONTAINER_SAMEARTIST: MediaClass.ARTIST,
    CONTAINER_PLAYLISTCONTAINER: MediaClass.PLAYLIST,
    "object.item": MediaClass.TRACK,
    ITEM_AUDIOITEM_MUSICTRACK: MediaClass.TRACK,
    "object.item.audioItem.audioBroadcast": MediaClass.GENRE,
}

SONOS_TO_MEDIA_TYPES = {
    SONOS_ALBUM: MediaType.ALBUM,
    SONOS_ALBUM_ARTIST: MediaType.ARTIST,
    SONOS_ARTIST: MediaType.CONTRIBUTING_ARTIST,
    SONOS_COMPOSER: MediaType.COMPOSER,
    SONOS_GENRE: MediaType.GENRE,
    SONOS_PLAYLISTS: MediaType.PLAYLIST,
    SONOS_TRACKS: MediaType.TRACK,
    CONTAINER_ALBUM_MUSICALBUM: MediaType.ALBUM,
    CONTAINER_GENRE_MUSICGENRE: MediaType.PLAYLIST,
    CONTAINER_PERSON_COMPOSER: MediaType.PLAYLIST,
    CONTAINER_PERSON_MUSICARTIST: MediaType.ARTIST,
    CONTAINER_PLAYLISTCONTAINER_SAMEARTIST: MediaType.ARTIST,
    CONTAINER_PLAYLISTCONTAINER: MediaType.PLAYLIST,
    ITEM_AUDIOITEM_MUSICTRACK: MediaType.TRACK,
}

MEDIA_TYPES_TO_SONOS: dict[MediaType | str, str] = {
    MediaType.ALBUM: SONOS_ALBUM,
    MediaType.ARTIST: SONOS_ALBUM_ARTIST,
    MediaType.CONTRIBUTING_ARTIST: SONOS_ARTIST,
    MediaType.COMPOSER: SONOS_COMPOSER,
    MediaType.GENRE: SONOS_GENRE,
    MediaType.PLAYLIST: SONOS_PLAYLISTS,
    MediaType.TRACK: SONOS_TRACKS,
}

SONOS_TYPES_MAPPING = {
    "A:ALBUM": SONOS_ALBUM,
    "A:ALBUMARTIST": SONOS_ALBUM_ARTIST,
    "A:ARTIST": SONOS_ARTIST,
    "A:COMPOSER": SONOS_COMPOSER,
    "A:GENRE": SONOS_GENRE,
    "A:PLAYLISTS": SONOS_PLAYLISTS,
    "A:TRACKS": SONOS_TRACKS,
    CONTAINER_ALBUM_MUSICALBUM: SONOS_ALBUM,
    CONTAINER_GENRE_MUSICGENRE: SONOS_GENRE,
    CONTAINER_PERSON_COMPOSER: SONOS_COMPOSER,
    CONTAINER_PERSON_MUSICARTIST: SONOS_ALBUM_ARTIST,
    CONTAINER_PLAYLISTCONTAINER_SAMEARTIST: SONOS_ARTIST,
    CONTAINER_PLAYLISTCONTAINER: SONOS_PLAYLISTS,
    "object.item": SONOS_OTHER_ITEM,
    ITEM_AUDIOITEM_MUSICTRACK: SONOS_TRACKS,
    "object.item.audioItem.audioBroadcast": SONOS_RADIO,
}

LIBRARY_TITLES_MAPPING = {
    "A:ALBUM": "Albums",
    "A:ALBUMARTIST": "Artists",
    "A:ARTIST": "Contributing Artists",
    "A:COMPOSER": "Composers",
    "A:GENRE": "Genres",
    "A:PLAYLISTS": "Playlists",
    "A:TRACKS": "Tracks",
}

PLAYABLE_MEDIA_TYPES = [
    MediaType.ALBUM,
    MediaType.ARTIST,
    MediaType.COMPOSER,
    MediaType.CONTRIBUTING_ARTIST,
    MediaType.GENRE,
    MediaType.PLAYLIST,
    MediaType.TRACK,
]

SONOS_CHECK_ACTIVITY = "sonos_check_activity"
SONOS_CREATE_ALARM = "sonos_create_alarm"
SONOS_CREATE_AUDIO_FORMAT_SENSOR = "sonos_create_audio_format_sensor"
SONOS_CREATE_BATTERY = "sonos_create_battery"
SONOS_CREATE_FAVORITES_SENSOR = "sonos_create_favorites_sensor"
SONOS_CREATE_MIC_SENSOR = "sonos_create_mic_sensor"
SONOS_CREATE_SWITCHES = "sonos_create_switches"
SONOS_CREATE_LEVELS = "sonos_create_levels"
SONOS_CREATE_MEDIA_PLAYER = "sonos_create_media_player"
SONOS_FALLBACK_POLL = "sonos_fallback_poll"
SONOS_ALARMS_UPDATED = "sonos_alarms_updated"
SONOS_FAVORITES_UPDATED = "sonos_favorites_updated"
SONOS_MEDIA_UPDATED = "sonos_media_updated"
SONOS_SPEAKER_ACTIVITY = "sonos_speaker_activity"
SONOS_SPEAKER_ADDED = "sonos_speaker_added"
SONOS_STATE_UPDATED = "sonos_state_updated"
SONOS_REBOOTED = "sonos_rebooted"
SONOS_VANISHED = "sonos_vanished"

SOURCE_AIRPLAY = "AirPlay"
SOURCE_LINEIN = "Line-in"
SOURCE_SPOTIFY_CONNECT = "Spotify Connect"
SOURCE_TV = "TV"

MODELS_LINEIN_ONLY = (
    "CONNECT",
    "CONNECT:AMP",
    "PORT",
    "PLAY:5",
)
MODELS_TV_ONLY = (
    "ARC",
    "BEAM",
    "PLAYBAR",
    "PLAYBASE",
)
MODELS_LINEIN_AND_TV = ("AMP",)

AVAILABILITY_CHECK_INTERVAL = datetime.timedelta(minutes=1)
AVAILABILITY_TIMEOUT = AVAILABILITY_CHECK_INTERVAL.total_seconds() * 4.5
BATTERY_SCAN_INTERVAL = datetime.timedelta(minutes=15)
SCAN_INTERVAL = datetime.timedelta(seconds=10)
DISCOVERY_INTERVAL = datetime.timedelta(seconds=60)
SUBSCRIPTION_TIMEOUT = 1200
