#!/usr/bin/env python3
import mpv
from threading import Thread

def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))

# Property access, these can be changed at runtime
#player.observe_property('time-pos', lambda pos: print('Now playing at {:.2f}s'.format(pos)))
#player.fullscreen = True
#player.fullscreen = True
# Option access, in general these require the core to reinitialize

def play(url):
    player = mpv.MPV(log_handler=my_log, input_default_bindings=True, input_vo_keyboard=True)
    player.loop = 'inf'
    player['vo'] = 'opengl'
    player.play(url)
    player.wait_for_playback()
    del player

#player.register_key_binding('q', my_q_binding)
#player.register_key_binding('1', play1)
#player.register_key_binding('2', play2)
#player.register_key_binding('4', play3)
#player.register_key_binding('5', play4)

url1 = 'rtsp://192.168.10.80:554/user=admin&password=&channel=1&stream=0.sdp?real_stream--rtp-caching=100'
url2 = 'rtsp://192.168.10.80:554/user=admin&password=&channel=2&stream=0.sdp?real_stream--rtp-caching=100'
url3 = 'rtsp://192.168.10.80:554/user=admin&password=&channel=3&stream=0.sdp?real_stream--rtp-caching=100'
url4 = 'rtsp://192.168.10.80:554/user=admin&password=&channel=4&stream=0.sdp?real_stream--rtp-caching=100'


t1 = Thread(target=play, args=(url1,)).start()
t2 = Thread(target=play, args=(url2,)).start()
t2 = Thread(target=play, args=(url3,)).start()
t2 = Thread(target=play, args=(url4,)).start()
t1.join()
t2.join()
