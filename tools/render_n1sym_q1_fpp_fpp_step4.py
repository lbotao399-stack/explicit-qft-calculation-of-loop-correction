from pathlib import Path
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
import numpy as np


plt.rcParams.update(
    {
        "font.family": "STIXGeneral",
        "mathtext.fontset": "stix",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop.png"
OUT_PDF = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop.pdf"


def lerp(p0, p1, t):
    return (p0[0] + (p1[0] - p0[0]) * t, p0[1] + (p1[1] - p0[1]) * t)


def draw_line(ax, p0, p1, lw=2.2):
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="black", lw=lw, solid_capstyle="round", zorder=2)


def draw_arrow_segment(ax, p0, p1, t0=0.42, t1=0.63, lw=1.45, scale=13):
    a0 = lerp(p0, p1, t0)
    a1 = lerp(p0, p1, t1)
    patch = FancyArrowPatch(
        a0,
        a1,
        arrowstyle="-|>",
        mutation_scale=scale,
        linewidth=lw,
        color="black",
        shrinkA=0,
        shrinkB=0,
        zorder=4,
    )
    ax.add_patch(patch)


def draw_fermion(ax, p0, p1, direction="forward", lw=2.2):
    draw_line(ax, p0, p1, lw=lw)
    if direction == "forward":
        draw_arrow_segment(ax, p0, p1)
    else:
        draw_arrow_segment(ax, p1, p0)


def draw_wavy(ax, p0, p1, amplitude=0.045, waves=5.0, lw=2.0):
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
    length = math.hypot(dx, dy)
    if length == 0:
        return
    t = np.linspace(0, 1, 220)
    x = x0 + dx * t
    y = y0 + dy * t
    nx = -dy / length
    ny = dx / length
    phase = amplitude * np.sin(2 * np.pi * waves * t)
    ax.plot(x + nx * phase, y + ny * phase, color="black", lw=lw, zorder=2)


def node(ax, center, r=0.05):
    ax.add_patch(Circle(center, r, facecolor="black", edgecolor="black", zorder=5))


def operator_box(ax, center, w=0.26, h=0.22):
    x, y = center
    ax.add_patch(
        Rectangle((x - w / 2, y - h / 2), w, h, facecolor="white", edgecolor="black", lw=1.6, zorder=5)
    )
    ax.text(x, y, "O", ha="center", va="center", fontsize=13, zorder=6)


def label(ax, xy, text, size=12, ha="center", va="center", boxed=False):
    bbox = None
    if boxed:
        bbox = {"boxstyle": "round,pad=0.10", "fc": "white", "ec": "none", "alpha": 0.96}
    ax.text(xy[0], xy[1], text, ha=ha, va=va, fontsize=size, bbox=bbox, zorder=7)


def setup_panel(ax, title, subtitle):
    ax.set_xlim(-3.1, 3.1)
    ax.set_ylim(-1.95, 1.55)
    ax.set_aspect("equal")
    ax.axis("off")
    label(ax, (-2.95, 1.38), subtitle, size=12, ha="left")
    label(ax, (0.0, 1.38), title, size=15)


def insertion_anchor(op):
    x, y = op
    return (x + 0.13, y)


def panel_triangle(ax, mirror=False):
    setup_panel(ax, "T001" if not mirror else "T004", "12" if not mirror else "21")
    op = (-2.2, -0.95)
    v1 = (-0.45, 0.10)
    v2 = (1.10, 0.30)
    ext_a = (2.35, 0.98)
    ext_l = (2.35, -0.12)

    operator_box(ax, op)
    draw_wavy(ax, insertion_anchor(op), (-1.55, -0.95))
    draw_fermion(ax, insertion_anchor(op), (-1.55, -0.15), direction="forward")
    draw_wavy(ax, (-1.55, -0.95), v1)
    draw_fermion(ax, (-1.55, -0.15), v2 if mirror else v1, direction="forward")
    draw_wavy(ax, v1, v2)
    draw_line(ax, v2 if mirror else v1, ext_a)
    draw_fermion(ax, v2, ext_l, direction="forward")
    node(ax, v1)
    node(ax, v2)

    label(ax, ext_a, r"$A(p_1)$" if not mirror else r"$A(p_2)$", size=13)
    label(ax, ext_l, r"$\widetilde\lambda(p_2)$" if not mirror else r"$\widetilde\lambda(p_1)$", size=13)
    label(ax, (-1.12, -0.95), r"$A$", size=11, boxed=True)
    label(ax, (-1.05, -0.05), r"$\widetilde\lambda$", size=11, boxed=True)
    label(ax, (0.30, 0.58), r"$A(q)$", size=11, boxed=True)
    label(ax, (0.42, -0.18), r"$\lambda$", size=11, boxed=True)


def panel_chain_same(ax, mirror=False):
    setup_panel(ax, "T002" if not mirror else "T005", "12" if not mirror else "21")
    op = (-2.2, -0.95)
    v1 = (-0.55, 0.10)
    v2 = (1.05, 0.25)
    ext_a = (2.35, 0.95)
    ext_l = (2.35, -0.05)

    operator_box(ax, op)
    draw_fermion(ax, insertion_anchor(op), (-1.55, -0.10), direction="forward")
    draw_wavy(ax, insertion_anchor(op), (-1.55, -0.95))
    draw_fermion(ax, (-1.55, -0.10), v1, direction="forward")
    draw_wavy(ax, (-1.55, -0.95), v1)
    draw_fermion(ax, v1, v2, direction="forward")
    draw_line(ax, v2, ext_a)
    draw_fermion(ax, v2, ext_l, direction="forward")
    node(ax, v1)
    node(ax, v2)

    label(ax, ext_a, r"$A$", size=13)
    label(ax, ext_l, r"$\widetilde\lambda$", size=13)
    label(ax, (-1.10, -0.95), r"$A$", size=11, boxed=True)
    label(ax, (-1.08, -0.05), r"$\widetilde\lambda$", size=11, boxed=True)
    label(ax, (0.25, 0.48), r"$(\widetilde\lambda,\lambda)$", size=10, boxed=True)


def panel_chain_split(ax, mirror=False):
    setup_panel(ax, "T003" if not mirror else "T006", "12" if not mirror else "21")
    op = (-2.2, -0.95)
    v1 = (-0.35, 0.10)
    v2 = (1.05, 0.25)
    ext_a = (2.35, 0.95)
    ext_l = (-2.45, 0.20)
    ins_f = (-1.40, -0.25)
    ins_a = (-1.55, -0.95)

    operator_box(ax, op)
    draw_fermion(ax, insertion_anchor(op), ins_f, direction="forward")
    draw_wavy(ax, insertion_anchor(op), ins_a)
    draw_fermion(ax, ins_f, v1, direction="forward")
    draw_wavy(ax, ins_a, v2)
    draw_fermion(ax, v1, v2, direction="forward")
    draw_line(ax, v2, ext_a)
    draw_fermion(ax, v1, ext_l, direction="backward")
    node(ax, v1)
    node(ax, v2)

    label(ax, ext_a, r"$A$", size=13)
    label(ax, ext_l, r"$\widetilde\lambda$", size=13)
    label(ax, (-1.00, -0.95), r"$A$", size=11, boxed=True)
    label(ax, (-1.02, -0.05), r"$\widetilde\lambda$", size=11, boxed=True)
    label(ax, (0.32, 0.48), r"$\lambda$", size=11, boxed=True)


ROW_BUILDERS = [panel_triangle, panel_chain_same, panel_chain_split]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(3, 2, figsize=(14.4, 13.0))
    fig.subplots_adjust(left=0.04, right=0.99, top=0.985, bottom=0.03, hspace=0.20, wspace=0.08)

    for row, builder in enumerate(ROW_BUILDERS):
        builder(axes[row, 0], mirror=False)
        builder(axes[row, 1], mirror=True)

    fig.savefig(OUT, dpi=260, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(OUT)
    print(OUT_PDF)


if __name__ == "__main__":
    main()
