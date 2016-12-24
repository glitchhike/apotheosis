def missing(artist_data):
    return artist_data['image'] == ''

def add(artist_data, lastfm, pth, config):
    image = get(artist_data['name'], lastfm)
    if image == None:
        print "Failed to get img from last.fm :("
        return
    edit(artist_data, image, pth, config)

def get(artist_name, lastfm):
    try:
        image = lastfm.get_artist(artist_name).get_cover_image(size=4)
    except:
        try:
            image = lastfm.get_artist(artist_name).get_cover_image(size=3)
        except:
            try:
                image = lastfm.get_artist(artist_name).get_cover_image(size=2)
            except:
                return None
    return image

def edit(artist_data, image, pth, config):
    print "Adding artist image from last.fm!"
    data = {'action' : 'edit',
            'auth' : config['pth']['auth'],
            'artistid' : artist_data['id'],
            'body' : artist_data['body'],
            'image' : image,
            'summary' : 'added artist bio from last.fm'}
    r = pth.session.post(config['pth']['artist_page'], data=data)