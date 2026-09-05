#!/usr/bin/env python3
"""
Phone cut of the Labor Day banner for perfectoblinds.com.

The desktop file is 1900x634. His slider scales ONE wide image down to the
phone width, so at 390px the headline lands at about 24px tall and the fine
print is unreadable. This is a portrait canvas built for that width instead:
780x860 renders at 390x430 on a phone, so the type is set relative to a
390px viewport, not to a 1900px one.

Same palette, same photo, same wording as design A - measured off his own
slider, nothing invented. OFFER and ENDS still come from the environment;
they are his numbers to give, not mine.
"""
import base64, os, re, sys

S = os.path.dirname(os.path.abspath(__file__))
W, H = 780, 940                      # renders 390x470 at 1x on a phone
# H is 940, not 860: at 860 the text column exactly filled the panel and the
# SHOP THE SALE pill sat flush on the bottom edge with its shadow clipped.
# The overflow check passed - a box ending at y=860 is inside a 860px canvas -
# so this only showed up by looking at the render.

GREEN, GOLD, BGOLD = "#006649", "#FECB3C", "#CC9600"
CHAR, PANEL = "#212121", "#f4f1ec"

OFFER = os.environ.get("OFFER", "20%")
ENDS = os.environ.get("ENDS", "ENDS MONDAY, SEPT 14")
PHOTO = os.environ.get(
    "PHOTO_A", "shots/EclipseShutters_TrackPearl_TrippleTrack_OA-web.jpg")


def b64(rel):
    ext = "png" if rel.lower().endswith(".png") else "jpeg"
    with open(os.path.join(S, rel), "rb") as f:
        return "data:image/%s;base64,%s" % (ext, base64.b64encode(f.read()).decode())


def render(tpl, mapping):
    """Token substitution - CSS is full of % signs, so printf is the wrong tool."""
    for k, v in mapping.items():
        tpl = tpl.replace("{{%s}}" % k, str(v))
    left = re.findall(r"\{\{(\w+)\}\}", tpl)
    if left:
        raise SystemExit("unsubstituted tokens: %s" % sorted(set(left)))
    return tpl


HEAD = render("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:{{W}}px;height:{{H}}px;overflow:hidden;background:#fff}
  .stage{position:relative;width:{{W}}px;height:{{H}}px;overflow:hidden;
         font-family:'Poppins',Arial,sans-serif}
  .dots{position:absolute;width:96px;height:96px;
        background-image:radial-gradient(currentColor 3px,transparent 3px);
        background-size:24px 24px;opacity:.28}
</style>
""", dict(W=W, H=H))


# Photo occupies the top, the warm panel the bottom, with the fade landing in
# between. An earlier try put the text OVER the photo with a flat tint - at
# this size the shutter slats read straight through the type.
BODY = render("""
<style>
 .m-photo{position:absolute;left:0;top:0;width:{{W}}px;height:400px}
 .m-photo img{position:absolute;inset:0;width:100%;height:100%;
              object-fit:cover;object-position:64% 54%}
 .m-fade{position:absolute;left:0;top:0;width:{{W}}px;height:400px;
   background:linear-gradient(180deg,rgba(244,241,236,0) 0%,
     rgba(244,241,236,0) 48%,rgba(244,241,236,.55) 72%,
     rgba(244,241,236,.94) 90%,{{PANEL}} 100%)}
 .m-panel{position:absolute;left:0;top:392px;width:{{W}}px;height:{{BOT}}px;
   background:{{PANEL}}}
 .m-warm{position:absolute;left:0;top:392px;width:{{W}}px;height:{{BOT}}px;
   background:linear-gradient(160deg,rgba(255,255,255,.60) 0%,
     rgba(255,255,255,0) 58%,rgba(198,192,183,.34) 100%)}
 .m-d1{right:34px;top:34px;color:#fff}
 .m-txt{position:absolute;left:0;top:392px;width:{{W}}px;height:{{BOT}}px;
        display:flex;flex-direction:column;align-items:center;
        justify-content:center;text-align:center;padding:0 46px}
 .m-eyebrow{font-size:32px;font-weight:700;letter-spacing:.30em;color:{{GREEN}};
            text-transform:uppercase}
 .m-rule{width:88px;height:6px;background:{{BGOLD}};border-radius:3px;margin:16px 0 20px}
 .m-off{font-size:128px;font-weight:800;line-height:.92;color:{{CHAR}};
        letter-spacing:-.03em;white-space:nowrap}
 .m-off em{font-style:normal;color:{{GREEN}}}
 .m-sub{font-size:36px;font-weight:600;color:{{CHAR}};margin-top:14px;white-space:nowrap}
 .m-note{font-size:26px;font-weight:400;font-style:italic;color:#5d5952;
         margin-top:12px;line-height:1.35}
 .m-cta{margin-top:26px;background:{{GREEN}};color:#fff;font-size:28px;font-weight:600;
        letter-spacing:.09em;padding:20px 54px;border-radius:44px;
        text-transform:uppercase;box-shadow:0 8px 22px rgba(0,102,73,.30)}
 /* the date sits on the photo so the panel keeps one clean column of type */
 .m-flash{position:absolute;left:50%;top:52px;transform:translateX(-50%) rotate(-2deg);
          background:{{GOLD}};color:{{CHAR}};font-size:29px;font-weight:700;
          letter-spacing:.08em;padding:18px 34px;border-radius:10px;
          white-space:nowrap;box-shadow:0 10px 26px rgba(0,0,0,.28)}
</style>
<div class="stage">
  <div class="m-photo"><img src="{{PA}}"></div>
  <div class="m-fade"></div>
  <div class="dots m-d1"></div>
  <div class="m-flash">{{ENDS}}</div>
  <div class="m-panel"></div>
  <div class="m-warm"></div>
  <div class="m-txt">
    <div class="m-eyebrow">Labor&nbsp;Day Sale</div>
    <div class="m-rule"></div>
    <div class="m-off">{{OFFER}} <em>OFF</em></div>
    <div class="m-sub">Sitewide &nbsp;&middot;&nbsp; On All Products</div>
    <div class="m-note">Free shipping to your door<br>Free in-home consultation</div>
    <div class="m-cta">Shop the Sale</div>
  </div>
</div>
""", dict(W=W, H=H, BOT=H - 392, GREEN=GREEN, GOLD=GOLD, BGOLD=BGOLD,
          CHAR=CHAR, PANEL=PANEL, PA=b64(PHOTO), OFFER=OFFER, ENDS=ENDS))


def build(suffix):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    with sync_playwright() as p:
        br = p.chromium.launch()
        ctx = br.new_context(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg = ctx.new_page()
        html = ("<!doctype html><html><head><meta charset='utf-8'>" + HEAD +
                "</head><body>" + BODY + "</body></html>")
        f = os.path.join(S, "banner_m.html")
        open(f, "w").write(html)
        pg.goto("file://" + f, wait_until="load", timeout=120000)
        pg.evaluate("()=>document.fonts.ready")
        pg.wait_for_timeout(2500)
        # fail loudly rather than silently shipping Arial
        bad = pg.evaluate("""()=>{const o=[];
          document.querySelectorAll('.m-off,.m-eyebrow,.m-cta').forEach(e=>{
            const cs=getComputedStyle(e), fam=cs.fontFamily.split(',')[0].replace(/'/g,'');
            if(!document.fonts.check(cs.fontWeight+' 40px "'+fam+'"')) o.push(e.className+':'+fam);});
          return o;}""")
        if bad:
            raise SystemExit("webfont did not load for: %s" % bad)
        over = pg.evaluate("""()=>{const o=[];
          document.querySelectorAll('.stage *').forEach(e=>{const b=e.getBoundingClientRect();
            if(b.width&&(b.right>%d+1||b.left<-1||b.bottom>%d+1||b.top<-1))
              o.push(e.className+' '+[b.left,b.top,b.right,b.bottom].map(Math.round).join(','));});
          return o;}""" % (W, H))
        if over:
            print("   WARN overflow:", over)
        png = os.path.join(S, "laborday_m%s.png" % suffix)
        pg.screenshot(path=png, clip={"x": 0, "y": 0, "width": W, "height": H})
        im = Image.open(png)
        print("  %-28s %s  %d KB" % (os.path.basename(png), im.size,
                                     os.path.getsize(png) // 1024))
        ctx.close(); br.close()
        return png


if __name__ == "__main__":
    print("offer=%s  ends=%s  canvas=%dx%d" % (OFFER, ENDS, W, H))
    build(os.environ.get("SUFFIX", ""))
