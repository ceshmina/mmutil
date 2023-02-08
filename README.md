# walkman-util

Macでウォークマン管理するためのコード群です。(個人用)

## setup

ウォークマンを開発者モードにして、USBデバッグを有効化しておきます。また、Macにadbコマンドが必要です

```sh
brew install android-platform-tools
```

リポジトリ直下に `settings.ini` を作成し、Mac/ウォークマンそれぞれのミュージックライブラリのパスを指定します (以下は例)

```python
[DEFAULT]
mac_music_path = '/Users/shu/Music/XLD'
walkman_music_path = '/sdcard/Music'
```

## sync

現状ではMac側に存在するすべての音源をウォークマンにコピーするため時間がかかります。ファイル名が一致した場合上書きされます。

```sh
python3 sync.py
```
