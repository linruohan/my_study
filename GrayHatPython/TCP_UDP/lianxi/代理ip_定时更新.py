# -*- coding: utf-8 -*-

import re
import urllib.request
import json
import os
import time
import socket


class ProxyIp(object):

    def __init__(self):
        self.path = os.path.split(os.path.realpath(__file__))[0]

    # Get latest proxy ip and download to json
    def update_ip(self):
        print ('Update Ip')
        url = 'http://www.ip3366.net/free/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        matches = re.findall(r'(\d+.\d+.\d+.\d+)</td>\s+<td>(\d+)</td>\s+<td>.*?</td>\s+<td>(HTTPS?)</td>',
            response.read().decode("gbk"),re.I)
        print(matches)
        ls = []
        for match in matches:
            if self.is_open(match[0], match[1]):
                ls.append({'ip':match[0], 'port':match[1], 'protocol': match[2]})

        with open('%s/ip.json' % self.path, 'w') as f:
            json.dump(ls, f)
        return ls

    # whether the ips is last or old.
    def is_last(self):
        m_time = int(os.path.getmtime('%s/ip.json' % self.path))
        now_time = int(time.time())
        return (now_time - m_time) > 60*60*4  # 4 hours

    @staticmethod
    def is_open(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(ip, int(port))
            return True
        except:
            print ('Faild IP: %s:%s' % (ip, port))
            return False

    def get_proxy_ips(self):
        if not self.is_last():
            return self.update_ip()
        else:
            with open('%s/ip.json' % self.path, 'r') as f:
                return json.load(f)

if __name__ == '__main__':
    p=ProxyIp()
    p.update_ip()
    p.get_proxy_ips()