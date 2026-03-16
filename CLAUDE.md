# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 環境

- Python 3.14 + uv + `.venv`
- パッケージ管理は `uv`。依存追加時は必ず `uv add` を実行する

## よく使うコマンド

```bash
source .venv/bin/activate

# レンダリング（低画質・プレビュー付き）
manim -pql main.py SphereGeodesics

# レンダリング（高画質）
manim -pqh main.py SphereGeodesics

# フォーマット
black main.py
```

出力動画は `media/videos/main/<解像度>/SphereGeodesics.mp4` に生成される。

## コードの構成

エントリポイントは `main.py` 1ファイルのみ。

**パラメータ層**（ファイル冒頭）: `RADIUS`・`PHI_START`・`N_GEODESICS` などのモジュール定数。ユーザーはここだけ編集して再レンダリングする。

**ユーティリティ関数**:

- `spherical_to_cartesian` — 球面座標 → デカルト座標
- `tangent_basis` — 球面上の点における接ベクトル基底 `(e_phi, e_theta)` を返す
- `great_circle_curve` — 点と接ベクトルから大円を `ParametricFunction` として構築。内部で接平面への射影・正規化を行う

**シーンクラス** `SphereGeodesics(ThreeDScene)`: `construct()` が唯一のメソッド。球面・グリッド・測地線・ラベルを順番に生成してアニメーションする。

## コーディング規約

- コメントは自明でない理由・意図のみ記述する。変数名・関数名から明らかな内容はコメントしない

## コミット規約

Conventional Commits に従う。

```
<type>(<scope>): <subject>
```

よく使う type: `feat` / `fix` / `refactor` / `chore` / `docs`

## 測地線の数学

球面上の測地線は大円。出発点 `p`（単位ベクトル）と接ベクトル `v`（`p` に直交する単位ベクトル）から

```
γ(t) = r * (cos(t) * p + sin(t) * v)
```

で完全な大円を parameterize する。`N_GEODESICS` 本の測地線は接平面内の方向角を `[0, π)` で等分割して生成する（大円は向きを反転すると同じ曲線になるため `[0, 2π)` ではなく `[0, π)`）。
