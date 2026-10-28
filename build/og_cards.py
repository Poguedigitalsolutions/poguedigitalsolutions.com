"""Social preview cards (1200 x 630) for blog posts, so each LinkedIn, Facebook, or X share
shows that post's own title instead of the same founder photo on every post.

page_blog.py calls card(slug, title, category) for each post. The card is written to
img/og/<slug>.png only when its pixels change, so rebuilding does not touch unchanged files.
To use a hand-made banner instead, add  image: img/your-banner.jpg  to the post's front matter.
"""
import io, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(__file__)
W, H = 1200, 630
INK, NAVY = (6, 11, 20), (15, 37, 68)
GOLD, GOLD_BRIGHT = (212, 175, 55), (242, 214, 128)
TITLE_FONT = os.path.join(HERE, "fonts", "Caladea-Bold.ttf")
LABEL_FONT = os.path.join(HERE, "fonts", "Inter-SemiBold.otf")
LOGO = os.path.join(HERE, "..", "img", "logo-horizontal.png")
OUT_DIR = "img/og"

MARGIN = 84          # keeps all text well inside the canvas so nothing crops
TITLE_TOP = 150
TITLE_BOTTOM = 470   # the logo row sits below this line


def _background():
    # diagonal ink to navy gradient
    vert = Image.linear_gradient("L").resize((W, H))
    horiz = Image.linear_gradient("L").rotate(90).transpose(Image.FLIP_LEFT_RIGHT).resize((W, H))
    grad = Image.blend(horiz, vert, 0.4)
    bg = Image.composite(Image.new("RGB", (W, H), NAVY), Image.new("RGB", (W, H), INK), grad)
    # soft gold glow in the top right corner
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W - 420, -300, W + 260, 300), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    return Image.composite(Image.new("RGB", (W, H), GOLD), bg, glow)


def _wrap(draw, text, font, width):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= width or not line:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def _fit_title(draw, title):
    width = W - 2 * MARGIN
    for size in range(72, 34, -2):
        font = ImageFont.truetype(TITLE_FONT, size)
        lines = _wrap(draw, title, font, width)
        line_h = int(size * 1.18)
        if len(lines) <= 4 and line_h * len(lines) <= TITLE_BOTTOM - TITLE_TOP:
            return font, lines, line_h
    return font, lines[:4], line_h


def render(title, category):
    img = _background()
    d = ImageDraw.Draw(img)

    label = ImageFont.truetype(LABEL_FONT, 22)
    eyebrow = category.upper()
    x = MARGIN
    for ch in eyebrow:  # letter-spaced, like the site's eyebrows
        d.text((x, 96), ch, font=label, fill=GOLD_BRIGHT)
        x += d.textlength(ch, font=label) + 3
    d.line((MARGIN, 134, MARGIN + 64, 134), fill=GOLD, width=3)

    font, lines, line_h = _fit_title(d, title)
    y = TITLE_TOP + ((TITLE_BOTTOM - TITLE_TOP) - line_h * len(lines)) // 2
    for ln in lines:
        d.text((MARGIN, y), ln, font=font, fill=(255, 255, 255))
        y += line_h

    # logo bottom left, byline bottom right
    logo = Image.open(LOGO).convert("RGBA")
    logo = logo.resize((300, int(logo.height * 300 / logo.width)), Image.LANCZOS)
    img.paste(logo, (MARGIN - 30, H - logo.height - 18), logo)
    by = ImageFont.truetype(LABEL_FONT, 22)
    text = "John M Pogue  ·  poguedigitalsolutions.com"
    d.text((W - MARGIN - d.textlength(text, font=by), H - 92), text, font=by, fill=(255, 255, 255, 200))
    return img


def card(slug, title, category):
    """Write img/og/<slug>.png if it changed. Returns the site-relative path."""
    os.makedirs(OUT_DIR, exist_ok=True)
    path = f"{OUT_DIR}/{slug}.png"
    buf = io.BytesIO()
    render(title, category).save(buf, "PNG", optimize=True)
    data = buf.getvalue()
    if not os.path.exists(path) or open(path, "rb").read() != data:
        open(path, "wb").write(data)
    return path
