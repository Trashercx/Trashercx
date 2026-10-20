"""
Generador de assets pixel-art (SVG) para el README de perfil.

Ejecutar:  python scripts/gen_pixel_assets.py

Todos los textos se dibujan con una fuente bitmap 5x7 propia (rects),
asi que no dependen de fuentes externas y se ven igual en cualquier navegador.
Las animaciones usan SMIL, que GitHub renderiza dentro de <img>.
"""
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

# ---------- Paleta 8-bit ----------
BG = "#0A0E27"      # fondo profundo
PANEL = "#0F1733"   # paneles
GREEN = "#00FF87"
BLUE = "#60A5FA"
YELLOW = "#FFD93D"
PINK = "#FF5E8A"
WHITE = "#F5F5F5"
GREY = "#8FA3B8"
SHADOW = "#05071A"

# ---------- Fuente bitmap 5x7 ----------
FONT = {
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".####", "#....", "#....", "#....", "#....", "#....", ".####"],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".####", "#....", "#....", "#.###", "#...#", "#...#", ".####"],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "#####"],
    "J": ["....#", "....#", "....#", "....#", "#...#", "#...#", ".###."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "0": [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"],
    "3": ["#####", "...#.", "..#..", "...#.", "....#", "#...#", ".###."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": ["..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "...#.", ".##.."],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
    ".": [".....", ".....", ".....", ".....", ".....", ".##..", ".##.."],
    ":": [".....", ".##..", ".##..", ".....", ".##..", ".##..", "....."],
    "-": [".....", ".....", ".....", "#####", ".....", ".....", "....."],
    "/": ["....#", "....#", "...#.", "..#..", ".#...", "#....", "#...."],
    ">": ["#....", ".#...", "..#..", "...#.", "..#..", ".#...", "#...."],
    "?": [".###.", "#...#", "....#", "...#.", "..#..", ".....", "..#.."],
    "&": [".##..", "#..#.", "#..#.", ".##..", "#.#.#", "#..#.", ".##.#"],
    "!": ["..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."],
    "+": [".....", "..#..", "..#..", "#####", "..#..", "..#..", "....."],
    "|": ["..#..", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
}


def text_width(s, scale):
    return (len(s) * 6 - 1) * scale


def text(s, x, y, scale, color):
    """Dibuja texto pixelado y devuelve un <g>. Fusiona pixeles contiguos por fila."""
    rects = []
    for ci, ch in enumerate(s.upper()):
        glyph = FONT.get(ch, FONT["?"])
        for r, row in enumerate(glyph):
            c = 0
            while c < 5:
                if row[c] == "#":
                    start = c
                    while c < 5 and row[c] == "#":
                        c += 1
                    rects.append(
                        f'<rect x="{x + (ci * 6 + start) * scale}" y="{y + r * scale}" '
                        f'width="{(c - start) * scale}" height="{scale}"/>'
                    )
                else:
                    c += 1
    return f'<g fill="{color}">' + "".join(rects) + "</g>"


def text_shadow(s, x, y, scale, color, shadow=SHADOW, off=None):
    off = off or max(2, scale // 2)
    return text(s, x + off, y + off, scale, shadow) + text(s, x, y, scale, color)


def rect(x, y, w, h, color, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" {extra}/>'


def svg(w, h, body, bg=None):
    bgr = rect(0, 0, w, h, bg) if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" shape-rendering="crispEdges">\n{bgr}{body}\n</svg>\n'
    )


def pixel_frame(x, y, w, h, t, color, fill=None, shadow=True):
    """Marco con esquinas 'redondeadas' al estilo pixel (sin el pixel de cada esquina)."""
    out = ""
    if shadow:
        out += rect(x + t, y + t, w, h, SHADOW)
    if fill:
        out += rect(x + t, y + t, w - 2 * t, h - 2 * t, fill)
    out += rect(x + t, y, w - 2 * t, t, color)
    out += rect(x + t, y + h - t, w - 2 * t, t, color)
    out += rect(x, y + t, t, h - 2 * t, color)
    out += rect(x + w - t, y + t, t, h - 2 * t, color)
    return out


def blink(dur="1s", values="1;1;0;0"):
    return (
        f'<animate attributeName="opacity" values="{values}" dur="{dur}" '
        f'calcMode="discrete" repeatCount="indefinite"/>'
    )


def sprite(rows, cmap, x, y, u):
    out = ""
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch in cmap:
                out += rect(x + c * u, y + r * u, u, u, cmap[ch])
    return out


def heart(x, y, u, color=PINK):
    rows = [".##.##.", "#######", "#######", ".#####.", "..###..", "...#..."]
    return sprite(rows, {"#": color}, x, y, u)


def cloud(x, y, u, color="#B9C8EA"):
    rows = ["...###....", ".########.", "##########"]
    return sprite(rows, {"#": color}, x, y, u)


CUY_BODY = [
    "......OOOOO.....",
    "....OOOOOOOOO...",
    "...OOOOOOOWWWW..",
    "..OOOOOOOWWWWWW.",
    "..OOOOOOWWWKWWW.",
    "..OOOOOWWWWWWWP.",
    "..OOOOOOWWWWWW..",
    "...OOOOOOWWWW...",
]
CUY_LEGS = ["....OO....OO....", "...OO......OO..."]
CUY_COLORS = {"O": "#E8803A", "W": "#FFF4E6", "K": "#2B1B12", "P": "#F28CA6"}


def cuy(x, y, u, frame=0):
    """Sprite de cuy (16x9) mirando a la derecha. frame 0/1 alterna las patas."""
    return sprite(CUY_BODY + [CUY_LEGS[frame]], CUY_COLORS, x, y, u)


def cuy_running(x, y, u):
    f0, f1 = cuy(x, y, u, 0), cuy(x, y, u, 1)
    return (
        f'<g>{f0}<animate attributeName="opacity" values="1;0" dur="0.3s" calcMode="discrete" repeatCount="indefinite"/></g>'
        f'<g>{f1}<animate attributeName="opacity" values="0;1" dur="0.3s" calcMode="discrete" repeatCount="indefinite"/></g>'
    )


# =====================================================================
# 1) HEADER
# =====================================================================
def header():
    W, H = 1200, 300
    rnd = random.Random(27001)
    u = 6
    ground_y = 252
    body = ""
    # cielo en bandas (degradado pixelado)
    bands = ["#070A1F", "#0A0E27", "#0E1535", "#132047", "#1A2C5C", "#223A74"]
    bh = ground_y // len(bands) + 1
    for i, col in enumerate(bands):
        body += rect(0, i * bh, W, bh, col)
    # estrellas (algunas titilan)
    for _ in range(90):
        sx, sy = rnd.randrange(0, W, u), rnd.randrange(0, 200, u)
        col = rnd.choice([WHITE, WHITE, "#C9D7F2", YELLOW])
        if rnd.random() < 0.35:
            d = rnd.uniform(1.2, 3.5)
            body += (
                f'<rect x="{sx}" y="{sy}" width="{u}" height="{u}" fill="{col}">'
                f'<animate attributeName="opacity" values="1;0.15;1" dur="{d:.1f}s" repeatCount="indefinite"/></rect>'
            )
        else:
            body += rect(sx, sy, u, u, col, 'opacity="0.8"')
    # luna
    moon = ["..####..", ".######.", "########", "########", "########", "########", ".######.", "..####.."]
    mx, my, mu = 950, 48, 7
    body += sprite(moon, {"#": "#FFF1B8"}, mx, my, mu)
    body += rect(mx + 3 * mu, my + 2 * mu, mu, mu, "#E8D48A") + rect(mx + 5 * mu, my + 4 * mu, mu, mu, "#E8D48A")
    # nubes flotando
    for (cx, cy, cu, dur) in [(80, 60, 7, 70), (520, 40, 5, 95), (860, 95, 6, 80)]:
        body += (
            f"<g>{cloud(cx, cy, cu)}"
            f'<animateTransform attributeName="transform" type="translate" from="-200 0" to="{W + 100} 0" dur="{dur}s" repeatCount="indefinite"/></g>'
        )
    # skyline con ventanas
    x = 0
    while x < W:
        bw = rnd.choice([24, 30, 36, 42, 48, 60])
        bh_ = rnd.choice([36, 48, 60, 72, 90, 108])
        col = rnd.choice(["#0B1230", "#0D1538", "#101A42"])
        body += rect(x, ground_y - bh_, bw, bh_, col)
        for wy in range(ground_y - bh_ + 6, ground_y - 6, 12):
            for wx in range(x + 6, x + bw - 6, 12):
                if rnd.random() < 0.45:
                    wc = rnd.choice([YELLOW, "#FFE98A", BLUE])
                    if rnd.random() < 0.15:
                        body += (
                            f'<rect x="{wx}" y="{wy}" width="6" height="6" fill="{wc}">'
                            f'<animate attributeName="opacity" values="1;0;1" dur="{rnd.uniform(2, 6):.1f}s" calcMode="discrete" repeatCount="indefinite"/></rect>'
                        )
                    else:
                        body += rect(wx, wy, 6, 6, wc)
        x += bw + rnd.choice([0, 6])
    # antena con luz roja
    body += rect(600, ground_y - 140, 6, 40, "#1A2448")
    body += (
        f'<rect x="600" y="{ground_y - 146}" width="6" height="6" fill="{PINK}">'
        f'<animate attributeName="opacity" values="1;0" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/></rect>'
    )
    # suelo
    body += rect(0, ground_y, W, 6, "#5BE36B")
    body += rect(0, ground_y + 6, W, 8, "#2E9E4A")
    body += rect(0, ground_y + 14, W, H - ground_y - 14, "#4B3426")
    for _ in range(70):
        body += rect(
            rnd.randrange(0, W, 6), rnd.randrange(ground_y + 18, H - 6, 6), 6, 6,
            rnd.choice(["#3A281D", "#5E4232"]),
        )
    # HUD superior
    body += text_shadow("PLAYER 1", 28, 24, 3, YELLOW)
    hearts_w = 3 * 7 * 3 + 2 * 6
    body += text("HP", W - 28 - hearts_w - 14 - text_width("HP", 3), 22, 3, WHITE)
    for i in range(3):
        body += heart(W - 28 - hearts_w + i * (7 * 3 + 6), 20, 3)
    # titulo con doble sombra (verde + oscura)
    title = "OSCAR BURGA"
    ts = 10
    tx = (W - text_width(title, ts)) // 2
    body += text(title, tx + 8, 86 + 8, ts, SHADOW)
    body += text(title, tx + 4, 86 + 4, ts, GREEN)
    body += text(title, tx, 86, ts, WHITE)
    # subtitulo
    sub = "CLOUD ARCHITECT // BACKEND ENGINEER"
    ss = 4
    body += rect(0, 168, W, 48, BG, 'opacity="0.78"')
    body += rect(0, 168, W, 2, GREEN, 'opacity="0.5"') + rect(0, 214, W, 2, GREEN, 'opacity="0.5"')
    body += text_shadow(sub, (W - text_width(sub, ss)) // 2, 178, ss, GREEN)
    # cuy corriendo sobre el cesped
    cu = 4
    body += (
        f"<g>{cuy_running(0, ground_y - 9 * cu, cu)}"
        f'<animateTransform attributeName="transform" type="translate" from="-80 0" to="{W + 40} 0" dur="22s" repeatCount="indefinite"/></g>'
    )
    (OUT / "header.svg").write_text(svg(W, H, body), encoding="utf-8")


# =====================================================================
# 2) TITULOS DE SECCION
# =====================================================================
def section(name, label, color=GREEN, tag=None):
    W, H = 1200, 64
    body = pixel_frame(2, 2, W - 8, H - 8, 4, color, fill=PANEL)
    body += f'<g>{text(">", 26, 18, 4, YELLOW)}{blink("0.9s")}</g>'
    body += text_shadow(label, 26 + 6 * 4 + 6, 18, 4, WHITE)
    if tag:
        tw = text_width(tag, 3)
        body += rect(W - 40 - tw - 16, 20, tw + 16, 29, color)
        body += text(tag, W - 40 - tw - 8, 24, 3, BG)
    else:
        for i in range(4):
            body += rect(W - 40 - i * 22, 26, 14, 14, color if i % 2 == 0 else BLUE)
    (OUT / f"section-{name}.svg").write_text(svg(W, H, body), encoding="utf-8")


# =====================================================================
# 3) ETIQUETAS (inventario)
# =====================================================================
def label(name, txt, color):
    W, H = 240, 40
    body = pixel_frame(1, 1, W - 5, H - 5, 3, color, fill=PANEL)
    body += rect(4, 4, 10, H - 11, color)
    body += text(txt, 26, 11, 3, WHITE)
    (OUT / f"label-{name}.svg").write_text(svg(W, H, body), encoding="utf-8")


# =====================================================================
# 4) FICHA DE PERSONAJE
# =====================================================================
def character_sheet():
    W, H = 600, 380
    body = pixel_frame(2, 2, W - 8, H - 8, 4, GREEN, fill=PANEL)
    body += rect(6, 6, W - 16, 44, BG)
    body += text_shadow("CHARACTER SHEET", 22, 18, 3, YELLOW)
    for i in range(3):
        body += rect(W - 36 - i * 18, 22, 12, 12, [GREEN, BLUE, PINK][i])
    rows = [
        ("NAME", "OSCAR BURGA", WHITE),
        ("CLASS", "CLOUD ARCHITECT", GREEN),
        ("ROLE", "BACKEND ENGINEER", BLUE),
        ("SPEC", "SECURITY / ISO 27001", PINK),
        ("BASE", "LIMA - PERU", YELLOW),
    ]
    y = 68
    for k, v, col in rows:
        body += text(k, 22, y, 2, GREY)
        body += text(v, 22 + 7 * 6 * 2, y, 2, col)
        y += 26
    for x in range(22, W - 22, 12):
        body += rect(x, y + 2, 6, 3, "#223058")
    y += 18
    body += text("SKILLS", 22, y, 2, GREY)
    y += 22
    # (nombre, nivel sobre 10, color)  <- ajusta aqui tus niveles
    skills = [
        ("CLOUD", 9, GREEN),
        ("BACKEND", 8, BLUE),
        ("SECURITY", 8, PINK),
        ("DEVOPS", 8, YELLOW),
    ]
    segs, sw, sh, gap = 10, 28, 14, 4
    bar_x = 22 + 9 * 6 * 2
    for i, (name, lvl, col) in enumerate(skills):
        body += text(name, 22, y + 1, 2, WHITE)
        body += rect(bar_x - 3, y - 3, segs * (sw + gap) - gap + 6, sh + 6, BG)
        for s in range(segs):
            sx = bar_x + s * (sw + gap)
            if s < lvl - 1:
                body += rect(sx, y, sw, sh, col)
            elif s == lvl - 1:
                body += (
                    f'<rect x="{sx}" y="{y}" width="{sw}" height="{sh}" fill="{col}">'
                    f'<animate attributeName="opacity" values="1;0.25;1" dur="{1.1 + 0.2 * i:.1f}s" repeatCount="indefinite"/></rect>'
                )
            else:
                body += rect(sx, y, sw, sh, "#1E2A4F")
        body += text(f"LV{lvl}", bar_x + segs * (sw + gap) + 8, y + 1, 2, GREY)
        y += 30
    (OUT / "character-sheet.svg").write_text(svg(W, H, body), encoding="utf-8")


# =====================================================================
# 5) DIVISOR
# =====================================================================
def divider():
    W, H = 1200, 12
    body = ""
    for i, x in enumerate(range(0, W, 12)):
        body += rect(x, 0 if i % 2 == 0 else 6, 12, 6, GREEN if i % 3 else BLUE)
    (OUT / "divider.svg").write_text(svg(W, H, body), encoding="utf-8")


# =====================================================================
# 6) FOOTER
# =====================================================================
def footer():
    W, H = 1200, 150
    rnd = random.Random(7)
    body = rect(0, 0, W, H, BG)
    for _ in range(40):
        body += rect(rnd.randrange(0, W, 6), rnd.randrange(0, 90, 6), 6, 6, WHITE, 'opacity="0.6"')
    ground_y = 112
    body += rect(0, ground_y, W, 6, "#5BE36B")
    body += rect(0, ground_y + 6, W, 8, "#2E9E4A")
    body += rect(0, ground_y + 14, W, H - ground_y - 14, "#4B3426")
    q = "CONTINUE?"
    body += text_shadow(q, (W - text_width(q, 4)) // 2, 24, 4, WHITE)
    yx = W // 2 - 110
    body += f'<g>{text(">", yx - 26, 66, 3, YELLOW)}{blink("0.8s")}</g>'
    body += text("YES", yx, 66, 3, GREEN)
    body += text("NO", W // 2 + 60, 66, 3, GREY)
    body += cuy(W - 140, ground_y - 9 * 4, 4, 0)
    body += text("THANKS FOR PLAYING", 28, 90, 2, GREY)
    (OUT / "footer.svg").write_text(svg(W, H, body), encoding="utf-8")


if __name__ == "__main__":
    header()
    section("player", "PLAYER 1 - ABOUT ME", GREEN, "LVL ARCHITECT")
    section("sheet", "CHARACTER SHEET & SKILL TREE", BLUE)
    section("inventory", "INVENTORY - TECH STACK", YELLOW)
    section("scores", "HIGH SCORES - GITHUB STATS", PINK)
    section("worldmap", "WORLD MAP - CONTRIBUTIONS", GREEN)
    label("cloud", "CLOUD", GREEN)
    label("backend", "BACKEND", BLUE)
    label("data", "DATA", PINK)
    label("tools", "TOOLS", YELLOW)
    character_sheet()
    divider()
    footer()
    print("OK ->", OUT)
    for p in sorted(OUT.glob("*.svg")):
        print(f"  {p.name:28s} {p.stat().st_size / 1024:6.1f} KB")
