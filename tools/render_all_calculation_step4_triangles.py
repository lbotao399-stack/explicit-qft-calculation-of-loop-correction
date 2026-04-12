from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "step4" / "calculation_triangles"


plt.rcParams.update(
    {
        "font.family": "STIXGeneral",
        "mathtext.fontset": "stix",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


@dataclass(frozen=True)
class TrianglePanel:
    pattern: str
    op_top: str
    op_bottom: str
    top_probe: str
    bottom_probe: str
    top_vertex: str
    bottom_vertex: str
    vertical_label: str
    vertical_style: str = "gauge"
    top_probe_style: str | None = None
    bottom_probe_style: str | None = None
    top_momentum: str | None = None
    bottom_momentum: str | None = None


@dataclass(frozen=True)
class TriangleFigure:
    stem: str
    rows: tuple[tuple[str, TrianglePanel, TrianglePanel], ...]


def vec(xy):
    return np.asarray(xy, dtype=float)


def cubic_points(p0, c0, c1, p1, n=220):
    p0 = vec(p0)
    c0 = vec(c0)
    c1 = vec(c1)
    p1 = vec(p1)
    t = np.linspace(0.0, 1.0, n)
    s = 1.0 - t
    pts = (
        (s**3)[:, None] * p0
        + (3.0 * s**2 * t)[:, None] * c0
        + (3.0 * s * t**2)[:, None] * c1
        + (t**3)[:, None] * p1
    )
    return t, pts


def cubic_tangents(p0, c0, c1, p1, n=220):
    p0 = vec(p0)
    c0 = vec(c0)
    c1 = vec(c1)
    p1 = vec(p1)
    t = np.linspace(0.0, 1.0, n)
    s = 1.0 - t
    tan = (
        (3.0 * s**2)[:, None] * (c0 - p0)
        + (6.0 * s * t)[:, None] * (c1 - c0)
        + (3.0 * t**2)[:, None] * (p1 - c1)
    )
    return t, tan


def unit_normals(tangent):
    length = np.linalg.norm(tangent, axis=1, keepdims=True)
    length[length == 0.0] = 1.0
    tangent = tangent / length
    return np.stack([-tangent[:, 1], tangent[:, 0]], axis=1)


def curve_label(ax, pts, frac, text, normal_offset=0.10, tangential_offset=0.0, size=9.0):
    idx = int(frac * (len(pts) - 1))
    idx0 = max(0, idx - 1)
    idx1 = min(len(pts) - 1, idx + 1)
    tangent = pts[idx1] - pts[idx0]
    norm = np.linalg.norm(tangent)
    if norm == 0.0:
        tangent = np.asarray([1.0, 0.0])
        norm = 1.0
    tangent = tangent / norm
    normal = np.asarray([-tangent[1], tangent[0]])
    xy = pts[idx] + normal_offset * normal + tangential_offset * tangent
    ax.text(
        xy[0],
        xy[1],
        rf"${text}$",
        ha="center",
        va="center",
        fontsize=size,
        bbox={"boxstyle": "round,pad=0.07", "fc": "white", "ec": "none", "alpha": 0.96},
        zorder=8,
    )


def endpoint_label(ax, xy, text, dx=0.0, dy=0.0, size=10.3):
    ax.text(xy[0] + dx, xy[1] + dy, rf"${text}$", ha="center", va="center", fontsize=size, zorder=8)


def draw_plain_curve(ax, p0, c0, c1, p1, lw=1.8, ls="-"):
    _, pts = cubic_points(p0, c0, c1, p1)
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=lw, ls=ls, solid_capstyle="round", zorder=2)
    return pts


def draw_fermion_curve(ax, p0, c0, c1, p1, lw=1.8, direction="forward"):
    pts = draw_plain_curve(ax, p0, c0, c1, p1, lw=lw)
    n = len(pts)
    i0 = int(0.48 * (n - 1))
    i1 = int(0.64 * (n - 1))
    start = pts[i0]
    end = pts[i1]
    if direction != "forward":
        start, end = end, start
    arrow = FancyArrowPatch(
        tuple(start),
        tuple(end),
        arrowstyle="-|>",
        mutation_scale=10.5,
        linewidth=1.0,
        color="black",
        shrinkA=0,
        shrinkB=0,
        zorder=4,
    )
    ax.add_patch(arrow)
    return pts


def draw_gauge_curve(ax, p0, c0, c1, p1, lw=1.55, amplitude=0.035, waves=5.0):
    t, pts = cubic_points(p0, c0, c1, p1, n=360)
    _, tan = cubic_tangents(p0, c0, c1, p1, n=360)
    normals = unit_normals(tan)
    env = np.sin(np.pi * t) ** 0.9
    phase = amplitude * env * np.sin(2.0 * np.pi * waves * t)
    curve = pts + normals * phase[:, None]
    ax.plot(curve[:, 0], curve[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)
    return pts


def draw_dashed_curve(ax, p0, c0, c1, p1, lw=1.8):
    return draw_plain_curve(ax, p0, c0, c1, p1, lw=lw, ls=(0, (5.5, 4.0)))


def line_style_from_label(label: str) -> str:
    if r"\phi" in label:
        return "scalar"
    if r"\psi" in label or r"\lambda" in label:
        return "fermion"
    if "f_{++}" in label or label.startswith("A") or r"\nabla" in label or "e^{" in label:
        return "plain"
    return "plain"


def draw_curve(ax, style: str, p0, c0, c1, p1):
    if style == "fermion":
        return draw_fermion_curve(ax, p0, c0, c1, p1)
    if style == "gauge":
        return draw_gauge_curve(ax, p0, c0, c1, p1)
    if style == "scalar":
        return draw_dashed_curve(ax, p0, c0, c1, p1)
    return draw_plain_curve(ax, p0, c0, c1, p1)


def operator_box(ax, center, w=0.36, h=0.32):
    x, y = center
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor="white", edgecolor="black", lw=1.4, zorder=5))
    ax.text(x, y, "O", ha="center", va="center", fontsize=12, zorder=6)


def node(ax, center, r=0.045):
    ax.add_patch(Circle(center, r, facecolor="black", edgecolor="black", zorder=6))


def setup_panel(ax, row_title: str, pattern: str):
    ax.set_xlim(-3.0, 3.1)
    ax.set_ylim(-2.05, 1.95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(-2.86, 1.72, row_title, ha="left", va="center", fontsize=11.2)
    ax.text(0.10, 1.72, f"Pattern {pattern}", ha="center", va="center", fontsize=14.0)


def draw_triangle_panel(ax, row_title: str, panel: TrianglePanel):
    setup_panel(ax, row_title, panel.pattern)

    op = np.asarray([-2.25, -0.10])
    v_top = np.asarray([0.15, 0.88])
    v_bot = np.asarray([0.15, -1.08])
    ext_top = np.asarray([2.45, 1.38])
    ext_bot = np.asarray([2.45, -1.58])

    operator_box(ax, op)

    p_op_top = draw_plain_curve(ax, op + np.asarray([0.18, 0.12]), (-1.45, 0.18), (-0.55, 0.62), v_top)
    p_op_bot = draw_plain_curve(ax, op + np.asarray([0.18, -0.12]), (-1.40, -0.40), (-0.58, -0.92), v_bot)
    p_vertical = draw_curve(ax, panel.vertical_style, v_top, (0.68, 0.44), (0.68, -0.62), v_bot)
    p_top_ext = draw_curve(
        ax,
        panel.top_probe_style or line_style_from_label(panel.top_probe),
        v_top,
        (0.88, 1.04),
        (1.70, 1.24),
        ext_top,
    )
    p_bot_ext = draw_curve(
        ax,
        panel.bottom_probe_style or line_style_from_label(panel.bottom_probe),
        v_bot,
        (0.90, -1.28),
        (1.70, -1.46),
        ext_bot,
    )

    node(ax, v_top)
    node(ax, v_bot)

    curve_label(ax, p_op_top, 0.42, panel.op_top, normal_offset=0.16, size=9.0)
    curve_label(ax, p_op_bot, 0.43, panel.op_bottom, normal_offset=-0.16, size=9.0)
    curve_label(ax, p_vertical, 0.50, panel.vertical_label, normal_offset=0.15, size=9.3)

    if panel.top_momentum:
        curve_label(ax, p_op_top, 0.70, panel.top_momentum, normal_offset=-0.13, size=8.6)
    if panel.bottom_momentum:
        curve_label(ax, p_op_bot, 0.70, panel.bottom_momentum, normal_offset=0.13, size=8.6)

    endpoint_label(ax, ext_top, panel.top_probe, dy=0.10)
    endpoint_label(ax, ext_bot, panel.bottom_probe, dy=-0.10)

    ax.text(v_top[0] + 0.28, v_top[1] + 0.18, rf"${panel.top_vertex}$", fontsize=9.3, ha="left", va="center", zorder=8)
    ax.text(v_bot[0] + 0.28, v_bot[1] - 0.18, rf"${panel.bottom_vertex}$", fontsize=9.3, ha="left", va="center", zorder=8)


def render_figure(spec: TriangleFigure):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    nrows = len(spec.rows)
    fig, axes = plt.subplots(nrows, 2, figsize=(15.5, 3.7 * nrows))
    if nrows == 1:
        axes = np.asarray([axes])
    fig.subplots_adjust(left=0.035, right=0.985, top=0.98, bottom=0.04, hspace=0.12, wspace=0.04)

    for row_idx, (row_title, left_panel, right_panel) in enumerate(spec.rows):
        draw_triangle_panel(axes[row_idx, 0], row_title, left_panel)
        draw_triangle_panel(axes[row_idx, 1], "", right_panel)

    png = OUT_DIR / f"{spec.stem}.png"
    pdf = OUT_DIR / f"{spec.stem}.pdf"
    fig.savefig(png, dpi=250, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    plt.close(fig)
    return png, pdf


def figures() -> Iterable[TriangleFigure]:
    n1_q = r"i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}"
    n1_qq = r"i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\widetilde\lambda^{\dot\rho}"
    n4_q = r"i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}"

    yield TriangleFigure(
        stem="n1_q1_fpp_barlambda_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"\bar\lambda_{\dot\beta}", r"\bar\lambda(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"\bar\lambda_{\dot\beta}", n1_q, r"\bar\lambda(p_2)", r"\bar\lambda(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_fpp_fpp_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"f_{++}", r"f_{++}(p_1)", r"\widetilde\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"f_{++}", n1_q, r"\widetilde\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_fpp_nabla_barlambda_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}", r"\bar\lambda(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}", n1_q, r"\bar\lambda(p_2)", r"\bar\lambda(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_nabla_fpp_fpp_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"\nabla_{+\dot\theta}f_{++}", r"f_{++}(p_1)", r"\widetilde\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"\nabla_{+\dot\theta}f_{++}", n1_q, r"\widetilde\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_nabla_fpp_barlambda_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_qq, r"\bar\lambda_{\dot\beta}", r"\bar\lambda(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"\bar\lambda_{\dot\beta}", n1_qq, r"\bar\lambda(p_2)", r"\bar\lambda(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_nabla_fpp_nabla_barlambda_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_qq, r"\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}", r"\bar\lambda(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}", n1_qq, r"\bar\lambda(p_2)", r"\bar\lambda(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_fpp_expw_fpp_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"e^{w\cdot\nabla_+}f_{++}", r"f_{++}(p_1)", r"\widetilde\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"f_{++}", r"e^{w\cdot\nabla_+}\!\left(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\right)", r"\widetilde\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_expw_fpp_fpp_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", r"e^{w\cdot\nabla_+}\!\left(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\right)", r"f_{++}", r"f_{++}(p_1)", r"\widetilde\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"e^{w\cdot\nabla_+}f_{++}", n1_q, r"\widetilde\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n1_q1_fpp_expw_barlambda_triangle_pair",
        rows=(
            (
                "anomalous triangle",
                TrianglePanel("12", n1_q, r"e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}", r"\bar\lambda(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}", n1_q, r"\bar\lambda(p_2)", r"\bar\lambda(p_1)", r"V_{A\lambda\widetilde\lambda}", r"V_{A\lambda\widetilde\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n4_q1_fpp_fpp_triangle_families",
        rows=(
            (
                "gauge triangle",
                TrianglePanel("12", n4_q, r"f_{++}", r"f_{++}(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\bar\lambda}", r"V_{A\lambda\bar\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"f_{++}", n4_q, r"\bar\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\bar\lambda}", r"V_{A\lambda\bar\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
            (
                "matter-fermion triangle",
                TrianglePanel("12", r"f_{++}", n4_q, r"\psi_+^i(p_2)", r"\bar\phi_i(p_1)", r"V_{A\psi\bar\psi}", r"V_{\lambda\psi\bar\phi}", r"\psi(q)", vertical_style="fermion", top_momentum=r"q-p_2", bottom_momentum=r"k_1=q+p_1"),
                TrianglePanel("21", n4_q, r"f_{++}", r"\bar\phi_i(p_2)", r"\psi_+^i(p_1)", r"V_{\lambda\psi\bar\phi}", r"V_{A\psi\bar\psi}", r"\psi(q)", vertical_style="fermion", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
            (
                "matter-scalar triangle",
                TrianglePanel("12", r"f_{++}", n4_q, r"\bar\phi_i(p_1)", r"\psi_+^i(p_2)", r"V_{A\phi\bar\phi}", r"V_{\lambda\psi\bar\phi}", r"\bar\phi(q)", vertical_style="scalar", top_momentum=r"q-p_2", bottom_momentum=r"k_1=q+p_1"),
                TrianglePanel("21", n4_q, r"f_{++}", r"\psi_+^i(p_1)", r"\bar\phi_i(p_2)", r"V_{\lambda\psi\bar\phi}", r"V_{A\phi\bar\phi}", r"\bar\phi(q)", vertical_style="scalar", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )

    yield TriangleFigure(
        stem="n4_q1_fpp_expw_fpp_triangle_families",
        rows=(
            (
                "gauge triangle",
                TrianglePanel("12", n4_q, r"e^{w\cdot\nabla_+}f_{++}", r"f_{++}(p_1)", r"\bar\lambda(p_2)", r"V_{A\lambda\bar\lambda}", r"V_{A\lambda\bar\lambda}", r"A(q)", top_momentum=r"k_1=q+p_1", bottom_momentum=r"q-p_2"),
                TrianglePanel("21", r"f_{++}", r"e^{w\cdot\nabla_+}\!\left(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\right)", r"\bar\lambda(p_2)", r"f_{++}(p_1)", r"V_{A\lambda\bar\lambda}", r"V_{A\lambda\bar\lambda}", r"A(q)", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
            (
                "matter-fermion triangle",
                TrianglePanel("12", r"e^{w\cdot\nabla_+}f_{++}", n4_q, r"\psi_+^i(p_2)", r"\bar\phi_i(p_1)", r"V_{A\psi\bar\psi}", r"V_{\lambda\psi\bar\phi}", r"\psi(q)", vertical_style="fermion", top_momentum=r"q-p_2", bottom_momentum=r"k_1=q+p_1"),
                TrianglePanel("21", n4_q, r"f_{++}", r"\bar\phi_i(p_2)", r"\psi_+^i(p_1)", r"V_{\lambda\psi\bar\phi}", r"V_{A\psi\bar\psi}", r"\psi(q)", vertical_style="fermion", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
            (
                "matter-scalar triangle",
                TrianglePanel("12", r"e^{w\cdot\nabla_+}f_{++}", n4_q, r"\bar\phi_i(p_1)", r"\psi_+^i(p_2)", r"V_{A\phi\bar\phi}", r"V_{\lambda\psi\bar\phi}", r"\bar\phi(q)", vertical_style="scalar", top_momentum=r"q-p_2", bottom_momentum=r"k_1=q+p_1"),
                TrianglePanel("21", n4_q, r"f_{++}", r"\psi_+^i(p_1)", r"\bar\phi_i(p_2)", r"V_{\lambda\psi\bar\phi}", r"V_{A\phi\bar\phi}", r"\bar\phi(q)", vertical_style="scalar", top_momentum=r"k_1=q+p_2", bottom_momentum=r"q-p_1"),
            ),
        ),
    )


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for spec in figures():
        png, pdf = render_figure(spec)
        print(png)
        print(pdf)


if __name__ == "__main__":
    main()
