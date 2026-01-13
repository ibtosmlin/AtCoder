# AtCoder 環境
[AtCoder](https://atcoder.jp/) のツール

## setup
- 設定
```
$ cd atcoder
$ pip install -e .
```

## Features
- サンプルケースを取得して、テンプレート準備
- サンプルケースのテストを実行

```sh
$ atc https://atcoder.jp/contests/abc234/tasks/abc234_a
```

## On contest
- tool/contest_id.txt の中身を変える
```sh
$ setconid abc234
```
```txt:contest_id.txt
con_root="https://atcoder.jp/contests"
con_id="abc234"
```
- コンテスト中
```sh
$ atc a
$ atc b
...
$ atc f
```

