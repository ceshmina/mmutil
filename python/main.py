import glob
from mutagen.flac import FLAC
import os
import shutil


def main():
    flac_paths = glob.glob(f'/music/**/*.flac', recursive=True)
    trans_map = str.maketrans({
        '/': '_',
        ' ': '_',
        ':': '_',
        '?': '_'
    })

    for path in flac_paths:
        artist, album, file = path.split('/')[2:]

        audio = FLAC(path)
        change = False

        tag_artist = audio.tags.get('albumartist', [''])[0].translate(trans_map)
        if tag_artist != '' and artist != tag_artist:
            artist = tag_artist
            change = True

        tag_album = audio.tags.get('album', [''])[0].translate(trans_map)
        if tag_album != '' and album != tag_album:
            album = tag_album
            change = True
        
        # TODO: トラック番号がintにキャストできない場合、エラーになる
        tag_track = int(audio.tags.get('tracknumber', [''])[0])
        tag_title = audio.tags.get('title', [''])[0].translate(trans_map)
        tag_file = f'{tag_track:02}_{tag_title}.flac'
        if tag_file != '' and file != tag_file:
            file = tag_file
            change = True
        
        if change:
            target_dir = f'/music/{artist}/{album}'
            target_path = f'{target_dir}/{file}'
            
            print(f'rename {path} -> {target_path}')
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(path, target_path)


if __name__ == '__main__':
    main()
