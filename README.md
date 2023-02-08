# mac-music-util

Macで音楽を管理するためのコード群です。(個人用)

## タグ情報を元にライブラリ整理

docker-composeが必要です。
リポジトリ直下に `.env` を作成し、Macのミュージックライブラリのパスを指定します (以下は例)

```
MUSIC_LIB='/Users/shu/Music/XLD'
```

音源のタグデータを参照して、ファイルパスを `{アルバムアーティスト}/{アルバム}/{トラック番号}_{曲名}.flac` にリネームします。
該当のタグ情報がない部分はスキップし、存在するタグのみ参照して置き換えます。

```sh
docker-compose up python
```

現状FLACのみの対応です。以下の文字はMacまたはAndroidで使用不可、または扱いが面倒なため、 `_` に置換されます。

- `/`
- 半角スペース
- `:`
- `?`

## Androidデバイスに音楽を同期

Androidデバイスを開発者モードにして、USBデバッグを有効化しておきます。また、Macにadbコマンドが必要です

```sh
brew install android-platform-tools
```

リポジトリ直下に `settings.ini` を作成し、Mac/Androidそれぞれのミュージックライブラリのパスを指定します (以下は例)

```python
[DEFAULT]
mac_music_path = '/Users/shu/Music/XLD'
walkman_music_path = '/sdcard/Music'
```

現状ではMac側に存在するすべての音源をAndroidにコピーするため時間がかかります。ファイル名が一致した場合上書きされます。

```sh
python3 sync.py
```
