from operator import itemgetter
from config import artist_page, torrents_page

class Artist():

    def __init__(self, info):
        self.name = info['name']
        self.id = info['id']
        self.image = info['image']
        self.similar_artists = [a['name'] for a in info["similarArtists"]]
        self.bio = info['body']
        self.albums = info['torrentgroup']
        for album in self.albums:
            album.update({'artist_name':self.name})
        self.edit_url = artist_page + '?action=edit&artistid=%s' % self.id


class Album():

    def __init__(self, info):
        self.name = info['groupName']
        self.id = info['groupId']
        self.artist_name = info['artist_name']
        self.image = info['wikiImage']
        self.edit_url = torrents_page + '?action=editgroup&groupid=%s' % self.id