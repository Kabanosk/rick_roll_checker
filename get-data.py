from checker import db
#TODO: get library for downloading video from yt by url for it

def download(url: str, path_to_store: str):
    pass


def download_videos_from_db():
    urls = db.collection('rickroll').document('urls').get().to_dict()
    for url in urls:
        download(url, './data')

if __name__ == '__main__':
    download_videos_from_db()
