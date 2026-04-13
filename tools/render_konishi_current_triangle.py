from __future__ import annotations

from pathlib import Path

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


def add_box(ax, center, text, w=0.56, h=0.34, fs=12):
    x, y = center
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor="white", edgecolor="black", lw=1.4, zorder=5))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, zorder=6)


def add_node(ax, xy, r=0.04):
    ax.add_patch(Circle(xy, r, facecolor="black", edgecolor="black", zorder=7))


def bezier(p0, p1, bend=(0.0, 0.0), n=200):
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)
    mid = 0.5 * (p0 + p1) + np.asarray(bend, dtype=float)
    t = np.linspace(0.0, 1.0, n)
    pts = ((1 - t) ** 2)[:, None] * p0 + (2 * (1 - t) * t)[:, None] * mid + (t**2)[:, None] * p1
    return pts


def draw_plain(ax, p0, p1, bend=(0.0, 0.0), lw=1.8):
    pts = bezier(p0, p1, bend=bend)
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)
    return pts


def draw_scalar(ax, p0, p1, bend=(0.0, 0.0), lw=1.8):
    pts = bezier(p0, p1, bend=bend, n=320)
    tang = np.gradient(pts, axis=0)
    norm = np.linalg.norm(tang, axis=1, keepdims=True)
    norm[norm == 0] = 1.0
    tang = tang / norm
    normal = np.stack([-tang[:, 1], tang[:, 0]], axis=1)
    t = np.linspace(0.0, 1.0, len(pts))
    env = np.sin(np.pi * t) ** 0.85
    wave = 0.03 * env * np.sin(2 * np.pi * 5 * t)
    curve = pts + normal * wave[:, None]
    ax.plot(curve[:, 0], curve[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)
    return pts


def draw_fermion(ax, p0, p1, bend=(0.0, 0.0), lw=1.8, direction="forward"):
    pts = draw_plain(ax, p0, p1, bend=bend, lw=lw)
    i0 = int(0.45 * (len(pts) - 1))
    i1 = int(0.60 * (len(pts) - 1))
    start = pts[i0]
    end = pts[i1]
    if direction != "forward":
        start, end = end, start
    ax.add_patch(
        FancyArrowPatch(
            tuple(start),
            tuple(end),
            arrowstyle="-|>",
            mutation_scale=10.0,
            lw=1.0,
            color="black",
            zorder=4,
        )
    )
    return pts


def put_label(ax, pts, frac, text, dx=0.0, dy=0.0, fs=9.4):
    idx = int(frac * (len(pts) - 1))
    x, y = pts[idx]
    ax.text(
        x + dx,
        y + dy,
        rf"${text}$",
        fontsize=fs,
        ha="center",
        va="center",
        bbox={"boxstyle": "round,pad=0.06", "fc": "white", "ec": "none", "alpha": 0.96},
        zorder=8,
    )


def endpoint_label(ax, xy, text, dx=0.0, dy=0.0, fs=10.2):
    ax.text(xy[0] + dx, xy[1] + dy, rf"${text}$", fontsize=fs, ha="center", va="center", zorder=8)


def draw_panel(ax, title, derivative_on_upper_scalar: bool):
    ax.set_xlim(-3.2, 3.3)
    ax.set_ylim(-2.15, 2.05)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.text(0.0, 1.82, title, fontsize=15.0, ha="center", va="center")

    current = (-2.25, 0.95)
    operator = (-2.15, -1.00)
    yukawa = (1.15, 0.00)
    ext_cur = (0.20, 1.70)
    ext_yuk = (2.80, 0.70)

    add_box(ax, current, r"$\partial\!\cdot\!J_-(q)$", w=0.92, h=0.36, fs=12.0)
    add_box(ax, operator, r"$K_+(p)$", w=0.62, h=0.34, fs=12.0)
    add_node(ax, yukawa)

    upper_label = r"(\partial_{-\dot\alpha}\phi^\dagger)" if derivative_on_upper_scalar else r"\phi^\dagger"
    lower_label = r"\phi" if derivative_on_upper_scalar else r"(\partial_{-\dot\alpha}\phi)"

    p_cur_ext = draw_fermion(ax, (current[0] + 0.46, current[1] + 0.02), ext_cur, bend=(0.10, 0.18), direction="forward")
    p_op_yuk = draw_fermion(ax, (operator[0] + 0.33, operator[1] + 0.10), yukawa, bend=(0.15, -0.10), direction="forward")
    p_cur_yuk = draw_scalar(ax, (current[0] + 0.46, current[1] - 0.10), yukawa, bend=(-0.05, 0.42))
    p_op_cur = draw_scalar(ax, (operator[0] + 0.30, operator[1] + 0.12), (current[0] + 0.20, current[1] - 0.16), bend=(-0.72, 0.10))
    p_yuk_ext = draw_fermion(ax, yukawa, ext_yuk, bend=(0.20, 0.22), direction="forward")

    put_label(ax, p_cur_ext, 0.68, r"\bar\lambda(p_1)", dx=-0.02, dy=0.14)
    put_label(ax, p_op_yuk, 0.50, r"\psi_+(k)", dx=0.00, dy=0.18)
    put_label(ax, p_cur_yuk, 0.54, upper_label, dx=0.00, dy=0.18)
    put_label(ax, p_op_cur, 0.54, lower_label, dx=-0.05, dy=-0.16)
    put_label(ax, p_yuk_ext, 0.56, r"\bar\lambda(p_2)", dx=0.02, dy=-0.16)

    endpoint_label(ax, (2.00, -0.26), r"V_{\bar\lambda}", dy=-0.04, fs=10.0)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 4.9))
    fig.subplots_adjust(left=0.03, right=0.985, top=0.95, bottom=0.06, wspace=0.04)
    draw_panel(axes[0], "T1", derivative_on_upper_scalar=True)
    draw_panel(axes[1], "T2", derivative_on_upper_scalar=False)
    png_path = OUT_DIR / "n1_general_konishi_current_triangle_pair.png"
    pdf_path = OUT_DIR / "n1_general_konishi_current_triangle_pair.pdf"
    fig.savefig(png_path, dpi=220)
    fig.savefig(pdf_path)
    plt.close(fig)
    print(png_path)
    print(pdf_path)


if __name__ == "__main__":
    main()
