# -*- coding: utf-8 -*-
"""

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url.
If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?


"""

import hashlib

class ShortURL:

    def __init__(self):
        self.short_to_url_map = {}
        self.m = hashlib.sha256

    def shorten(self, url):
        if url is None:
            return None

        if url in self.short_to_url_map.keys():
            return self.short_to_url_map[url]
        else:
            sha_signature = self.m(url.encode()).hexdigest()
            short_hash = sha_signature[:6]
            self.short_to_url_map[short_hash] = url

            return short_hash

    def get_hash(self, str):
        if str in self.short_to_url_map.keys():
            return self.short_to_url_map[str]
        else:
            return None


if __name__ == '__main__':
    shorturl = ShortURL()
    f = shorturl.shorten("테스트")
    assert shorturl.get_hash(f) == "테스트"
    print()




