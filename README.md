# LGTM画像作成ツール

※本リポジトリは、[Python実践入門
──言語の力を引き出し、開発効率を高める
](https://gihyo.jp/book/2020/978-4-297-11111-3)の第13章にある、Pythonのサンプルアプリケーション開発の実践例です。

画像に「LGTM」（Looks Good To Me）のスタンプを追加するためのPythonコマンドラインツールです。

## 機能

- 画像にLGTMスタンプを追加
- コマンドラインから簡単に使用可能
- カスタマイズ可能なスタンプの位置とサイズ

## インストール方法

```bash
pip install -e .
```

## 使用方法

```bash
lgtm [画像ファイルのパス]
```

## 依存関係

- Python 3.6以上
- Click
- Pillow
- requests

## 開発環境のセットアップ

1. リポジトリをクローン
```bash
git clone [リポジトリのURL]
cd lgtm-python
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Linuxの場合
# または
.\venv\Scripts\activate  # Windowsの場合
```

3. 依存関係のインストール
```bash
pip install -r requirements.lock
```
