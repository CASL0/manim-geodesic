"""
球面測地線ビジュアライザー (Manim Community)
=============================================

実行方法:
    manim -pql main.py SphereGeodesics       # 低画質プレビュー
    manim -pqh main.py SphereGeodesics       # 高画質

パラメータは下記の「調整可能なパラメータ」セクションで変更してください。
"""

from manim import *
import numpy as np

# ── 調整可能なパラメータ ──────────────────────────────────────

RADIUS: float = 2.5

# 出発点（球面座標）
# PHI_START  : 北極からの角度 [0, π]  (0=北極, π/2=赤道, π=南極)
# THETA_START: 方位角           [0, 2π]
PHI_START: float = PI / 3
THETA_START: float = PI / 4

N_GEODESICS: int = 8
STROKE_WIDTH: int = 3
SHOW_GRID: bool = True
SHOW_AXES: bool = True
CAMERA_ROTATION_RATE: float = 0.15  # 0 で停止
WAIT_TIME: int = 12

GEODESIC_COLORS: list[ManimColor] = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]
SPHERE_COLOR: ManimColor = BLUE_E
SPHERE_OPACITY: float = 0.25
GRID_COLOR: ManimColor = BLUE_B
GRID_OPACITY: float = 0.4

# ─────────────────────────────────────────────────────────────


def spherical_to_cartesian(r: float, phi: float, theta: float) -> np.ndarray:
    """球面座標 → デカルト座標"""
    return r * np.array(
        [
            np.sin(phi) * np.cos(theta),
            np.sin(phi) * np.sin(theta),
            np.cos(phi),
        ]
    )


def tangent_basis(phi: float, theta: float) -> tuple[np.ndarray, np.ndarray]:
    """
    球面上の点 (phi, theta) における正規化接ベクトル基底 (e_phi, e_theta) を返す。
    e_phi  : 南方向（phi増加方向）
    e_theta: 東方向（theta増加方向）
    """
    e_phi = np.array(
        [
            np.cos(phi) * np.cos(theta),
            np.cos(phi) * np.sin(theta),
            -np.sin(phi),
        ]
    )
    e_theta = np.array(
        [
            -np.sin(theta),
            np.cos(theta),
            0.0,
        ]
    )
    return e_phi, e_theta


def great_circle_curve(
    p_unit: np.ndarray, v_unit: np.ndarray, radius: float
) -> ParametricFunction:
    """
    単位球上の点 p_unit から方向 v_unit（接ベクトル）に出発する大円を
    ParametricFunction として返す。

    γ(t) = r * (cos(t) * p + sin(t) * v)  で t ∈ [0, 2π]
    """
    # v を接平面へ射影・正規化
    v: np.ndarray = v_unit - np.dot(v_unit, p_unit) * p_unit
    norm: float = float(np.linalg.norm(v))
    if norm < 1e-10:
        # 縮退している場合は別の方向を使う
        v = np.array([0, 0, 1.0]) - np.dot(np.array([0, 0, 1.0]), p_unit) * p_unit
        v /= np.linalg.norm(v)
    else:
        v /= norm

    def curve(t: float) -> np.ndarray:
        return radius * (np.cos(t) * p_unit + np.sin(t) * v)

    return ParametricFunction(curve, t_range=[0, TAU], color=WHITE)


class SphereGeodesics(ThreeDScene):
    """球面上の測地線（大円）を描画するシーン"""

    def construct(self) -> None:
        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

        sphere = Surface(
            lambda u, v: spherical_to_cartesian(RADIUS, v, u),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(48, 24),
            fill_opacity=SPHERE_OPACITY,
            fill_color=SPHERE_COLOR,
            stroke_width=0,
        )

        axes_group = VGroup()
        if SHOW_AXES:
            axis_len: float = RADIUS * 1.4
            for direction, color, label_text in [
                (RIGHT, RED, "x"),
                (UP, GREEN, "z"),
                (OUT, BLUE, "y"),
            ]:
                axes_group.add(
                    Arrow3D(
                        start=ORIGIN,
                        end=axis_len * direction,
                        color=color,
                        thickness=0.02,
                    )
                )

        grid_lines = VGroup()
        if SHOW_GRID:
            # 緯線（等 phi）: 30° 刻み 5本
            for phi in np.linspace(PI / 6, 5 * PI / 6, 5):
                grid_lines.add(
                    ParametricFunction(
                        lambda t, p=phi: RADIUS
                        * np.array(
                            [
                                np.sin(p) * np.cos(t),
                                np.sin(p) * np.sin(t),
                                np.cos(p),
                            ]
                        ),
                        t_range=[0, TAU],
                        color=GRID_COLOR,
                        stroke_width=0.8,
                        stroke_opacity=GRID_OPACITY,
                    )
                )

            # 経線（等 theta）: 30° 刻み 12本
            for theta in np.linspace(0, TAU, 12, endpoint=False):
                grid_lines.add(
                    ParametricFunction(
                        lambda t, th=theta: RADIUS
                        * np.array(
                            [
                                np.sin(t) * np.cos(th),
                                np.sin(t) * np.sin(th),
                                np.cos(t),
                            ]
                        ),
                        t_range=[0, PI],
                        color=GRID_COLOR,
                        stroke_width=0.8,
                        stroke_opacity=GRID_OPACITY,
                    )
                )

        p_cart: np.ndarray = spherical_to_cartesian(RADIUS, PHI_START, THETA_START)
        p_unit: np.ndarray = p_cart / RADIUS

        start_dot = Sphere(radius=0.07 * RADIUS, color=WHITE)
        start_dot.move_to(p_cart)

        # 出発点から外向きに伸びる法線マーカー
        normal_line = Line3D(
            start=p_cart,
            end=p_cart + 0.35 * p_unit,
            color=WHITE,
            thickness=0.02,
        )

        e_phi, e_theta = tangent_basis(PHI_START, THETA_START)
        geodesics = VGroup()
        for i in range(N_GEODESICS):
            # 接平面内での方向角を等分割
            alpha: float = i * PI / N_GEODESICS
            v_dir: np.ndarray = np.cos(alpha) * e_phi + np.sin(alpha) * e_theta

            geo = great_circle_curve(p_unit, v_dir, RADIUS)
            geo.set_color(GEODESIC_COLORS[i % len(GEODESIC_COLORS)])
            geo.set_stroke(width=STROKE_WIDTH)
            geodesics.add(geo)

        title = Text("球面の測地線（大円）", font_size=28)
        title.to_corner(UL)

        param_text = Text(
            f"出発点: φ={PHI_START/PI:.2f}π, θ={THETA_START/PI:.2f}π\n"
            f"測地線数: {N_GEODESICS}",
            font_size=20,
            color=GRAY_A,
        )
        param_text.next_to(title, DOWN, aligned_edge=LEFT)

        self.add_fixed_in_frame_mobjects(title, param_text)
        self.play(
            Create(sphere),
            Create(grid_lines),
            Create(axes_group),
            run_time=1.5,
        )
        self.play(
            FadeIn(start_dot, scale=2),
            Create(normal_line),
            run_time=0.8,
        )
        self.play(
            LaggedStart(
                *[Create(g) for g in geodesics],
                lag_ratio=0.15,
            ),
            run_time=2.5,
        )

        if CAMERA_ROTATION_RATE > 0:
            self.begin_ambient_camera_rotation(rate=CAMERA_ROTATION_RATE)

        self.wait(WAIT_TIME)
