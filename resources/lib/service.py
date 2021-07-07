import xbmc,xbmcaddon
import time, urllib
from urlparse import urlparse, parse_qs

# import vars

#Add src/service in load paths
# my_addon = xbmcaddon.Addon(vars.__addon_id__)
# addon_dir = xbmc.translatePath( my_addon.getAddonInfo('path') ).decode('utf-8')
# sys.path.append(os.path.join(addon_dir, 'src', 'service'))

from base_thread import BaseThread


class PollingThread(BaseThread):

    def __init__(self, gp_gui,gp, debug=False):
        super(PollingThread, self).__init__()
        self.gamepass_gui = gp_gui
        self.gp = gp
        self.debug = debug
        self.expires = 0
        self.last_refresh = time.time()
        self.log("!!!!!!!!!!!! SERVICE THREAD STARTED")
    def log(self, string):
        if self.debug:
            try:
                print '[thread service]: %s' % string
            except UnicodeEncodeError:
                # we can't anticipate everything in unicode they might throw at
                # us, but we can handle a simple BOM
                bom = unicode(codecs.BOM_UTF8, 'utf8')
                print '[thread service]: %s' % string.replace(bom, '')
            except:
                pass

    def refreshLiveUrl(self, url):
        last_played = self.gamepass_gui.last_played
        # {"id": 1, "game_start_time": None, "game_duration_time": None,"game_state": 1, "stream_type": "channel"}
        streams =  self.gp.parse_m3u8_manifest(last_played["id"], last_played["stream_type"], last_played["game_state"],
                                         last_played["game_duration_time"],
                                         last_played["game_start_time"], last_played["username"],
                                         last_played["password"])
        if streams:
            stream_url = self.gamepass_gui.select_stream_url(streams)
            if stream_url:
                # self.readExpiresFromUrl(url)
                self.log("@@@@@@@@@@@@@@@@ Playing file again new cookies: " + stream_url)
                self.gamepass_gui.play_url(str(stream_url))


    def readExpiresFromUrl(self, url):
        url_parts = urlparse(url)

        # Parse query string to dictionary
        query_params = parse_qs(url_parts.query)

        #G et the hdnea param, where the "expires" param is
        hdnea_params = query_params.get("hdnea")[0]

        hdnea_params = hdnea_params.replace('~', '&')
        self.expires = parse_qs(hdnea_params).get("exp", 0)[0]
        self.expires = int(self.expires)

    def run(self):
        while True:
            # self.log("Service Running")
            # Wait second
            xbmc.sleep(1000)
            if xbmc.Player().isPlayingVideo():
                current_playing_url = xbmc.Player().getPlayingFile()
                self.readExpiresFromUrl(current_playing_url)

                timestamp = time.time()

                # Avoid refreshing too fast, let at least one minute pass from the last refresh
                expire_timestamp = max(self.expires, self.last_refresh + 60)

                if timestamp > expire_timestamp:
                    self.refreshLiveUrl(current_playing_url)
                    self.last_refresh = timestamp

            if not self.should_keep_running():
                self.log("THREAD STOPPED NFL_GAMEPASS!!!")
                break
