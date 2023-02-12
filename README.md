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
