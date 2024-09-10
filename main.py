from datetime import datetime

import requests_cache

from steamdb.api.handlers import APIHandler

users = [
    "76561198043967700",  # Matheus
    "76561198193901450",  # Luciano
    "76561198281978558",
    "76561198068343409",
    "76561198155811707",  # Jeff
    "76561198059931650",  # Duds
    # "panicboy7",  # Gusthavo Vanity Name # TODO: https://stackoverflow.com/questions/19247887/get-steamid-by-user-nickname
    "76561198196806371",  # Gusthavo
]

if __name__ == "__main__":
    requests_cache.install_cache("github_cache", backend="sqlite", expire_after=180)

    api = APIHandler()

    for userid in users:
        print("Attempt: %s" % userid, str(datetime.now()))
        user = api.get_user(userid)

    requests_cache.uninstall_cache()
