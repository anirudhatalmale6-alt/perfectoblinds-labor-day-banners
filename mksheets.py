#!/usr/bin/env python3
"""Two review sheets for the client. Built offline from files already on disk -
no further requests to his store, which has started answering 429."""
from PIL import Image, ImageDraw, ImageFont
import os

S = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(sz, bold=False):
    return ImageFont.truetype(FB if bold else F, sz)


# ------------------------------------------------- sheet 1: the three options
def sheet_options():
    w, gap, pad = 1150, 22, 34
    items = [("A", "laborday_a.png",
              "Matches your current slide - warm panel, brand green, gold flash"),
             ("B", "laborday_b.png",
              "Bolder - navy sweep and gold, with your free-shipping trust strip"),
             ("C", "laborday_c.png",
              "Full-bleed room shot, condensed type, slim flag accent")]
    thumbs = []
    for k, f, cap in items:
        im = Image.open(os.path.join(S, f)).convert("RGB")
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        thumbs.append((k, im, cap))
    hh = 74
    H = pad + sum(hh + t[1].height + gap for t in thumbs) + pad + 34
    sheet = Image.new("RGB", (w + pad * 2, H), "#ffffff")
    d = ImageDraw.Draw(sheet)
    y = pad
    for k, im, cap in thumbs:
        d.rectangle([pad, y, pad + w, y + hh - 12], fill="#f2f0ec")
        d.rectangle([pad, y, pad + 8, y + hh - 12], fill="#006649")
        d.text((pad + 26, y + 9), "OPTION %s" % k, font=font(23, True), fill="#006649")
        d.text((pad + 26, y + 40), cap, font=font(18), fill="#4a4640")
        y += hh
        sheet.paste(im, (pad, y))
        d.rectangle([pad, y, pad + w - 1, y + im.height - 1], outline="#d8d4ce")
        y += im.height + gap
    d.text((pad, H - 30),
           "All three are 1900 x 634 - the exact size of your current Banner_03 slide, "
           "so they drop straight into the slider.",
           font=font(17), fill="#6b6660")
    p = os.path.join(S, "laborday_OPTIONS.png")
    sheet.save(p)
    print("  laborday_OPTIONS.png", sheet.size, os.path.getsize(p) // 1024, "KB")


# ------------------------------------- sheet 2: what the slider does on a phone
def sheet_mobile():
    """The slider scales one image to the viewport width. At 390px that shrinks
    everything by 4.9x. Show his CURRENT slide the same way, so this reads as a
    property of the slider and not as a fault in the new artwork."""
    PHONE = 390
    rows = [("Your current slide", "cur_b03.png"),
            ("New Labor Day banner (Option A)", "laborday_a.png")]
    W, pad = 940, 36
    imgs = []
    for label, f in rows:
        im = Image.open(os.path.join(S, f)).convert("RGB")
        sc = PHONE / im.width
        imgs.append((label, im.resize((PHONE, round(im.height * sc)), Image.LANCZOS),
                     im.width, sc))
    H = pad + 96 + sum(46 + i[1].height + 30 for i in imgs) + 96
    sheet = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(sheet)
    d.text((pad, pad), "How the slider renders on a phone", font=font(30, True), fill="#212121")
    d.text((pad, pad + 44),
           "The slider scales one image to the screen width. Shown here at actual size on a 390px phone.",
           font=font(18), fill="#5d5952")
    y = pad + 100
    for label, im, ow, sc in imgs:
        d.text((pad, y), "%s  -  %dpx wide scaled to %dpx  (%.2fx)" % (label, ow, PHONE, sc),
               font=font(19, True), fill="#006649")
        y += 34
        sheet.paste(im, (pad, y))
        d.rectangle([pad, y, pad + im.width - 1, y + im.height - 1], outline="#c9c5bf")
        y += im.height + 42
    # be exact rather than vague: I know my own type sizes, so state what they
    # become after the 0.21x scale instead of saying "hard to read".
    d.text((pad, H - 66),
           "At 0.21x the headline still works (118px becomes 24px) - but the small",
           font=font(18, True), fill="#8a2b2b")
    d.text((pad, H - 42),
           "print drops to about 5px and is gone. Your current slide has the same issue.",
           font=font(18, True), fill="#8a2b2b")
    d.text((pad, H - 18),
           "I can cut a taller phone version with bigger type if you want it.",
           font=font(18), fill="#5d5952")
    p = os.path.join(S, "laborday_MOBILE.png")
    sheet.save(p)
    print("  laborday_MOBILE.png", sheet.size, os.path.getsize(p) // 1024, "KB")


sheet_options()
sheet_mobile()
