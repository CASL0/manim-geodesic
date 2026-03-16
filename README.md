# manim-geodesic

[Manim Community](https://www.manim.community/) を使って球面（S²）上の測地線（大円）を 3D アニメーションで可視化するツールです。

## 必要環境

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- Cairo（`brew install cairo`）
- pkg-config（`brew install pkg-config`）

## セットアップ

```bash
git clone <repo>
cd manim-geodesic
uv sync
source .venv/bin/activate
```

## 開発ツール

```bash
black main.py      # フォーマット
pyright main.py    # 型チェック
pylint main.py     # Lint
```

## 実行

```bash
# 低画質・プレビュー付き（開発時）
manim -pql main.py SphereGeodesics

# 高画質
manim -pqh main.py SphereGeodesics
```

出力動画は `media/videos/main/<解像度>/SphereGeodesics.mp4` に生成されます。

## パラメータ

`main.py` 冒頭の定数を編集して再レンダリングするだけで見た目を変更できます。

| 変数                              | 型                     | 説明                              | デフォルト        |
| --------------------------------- | ---------------------- | --------------------------------- | ----------------- |
| `RADIUS`                          | `float`                | 球の半径                          | `2.5`             |
| `PHI_START`                       | `float`                | 出発点の極角 （0=北極, π/2=赤道） | `PI/3`            |
| `THETA_START`                     | `float`                | 出発点の方位角                    | `PI/4`            |
| `N_GEODESICS`                     | `int`                  | 描画する測地線の本数              | `8`               |
| `STROKE_WIDTH`                    | `int`                  | 測地線の線幅                      | `3`               |
| `SHOW_GRID`                       | `bool`                 | 緯線・経線グリッドの表示          | `True`            |
| `SHOW_AXES`                       | `bool`                 | 座標軸の表示                      | `True`            |
| `CAMERA_ROTATION_RATE`            | `float`                | カメラ回転速度（0 で停止）        | `0.15`            |
| `WAIT_TIME`                       | `int`                  | 回転後の待機時間（秒）            | `12`              |
| `GEODESIC_COLORS`                 | `list[ManimColor]`     | 測地線の色リスト（循環使用）      | 虹色8色           |
| `SPHERE_COLOR` / `SPHERE_OPACITY` | `ManimColor` / `float` | 球面の色・透明度                  | `BLUE_E` / `0.25` |
| `GRID_COLOR` / `GRID_OPACITY`     | `ManimColor` / `float` | グリッドの色・透明度              | `BLUE_B` / `0.4`  |

## 仕組み

球面上の測地線は大円です。出発点 **p**（単位ベクトル）と接ベクトル **v**（**p** に直交）を与えると、

```math
γ(t) = r · (cos(t) · p + sin(t) · v),  t ∈ [0, 2π]
```

で完全な大円が得られます。`N_GEODESICS` 本の測地線は接平面内の方向角を `[0, π)` で等分割して生成します（大円は向きを反転すると同じ曲線になるため）。
