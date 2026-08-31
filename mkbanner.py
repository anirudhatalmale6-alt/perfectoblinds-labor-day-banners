#!/usr/bin/env python3
"""
Labor Day banners for perfectoblinds.com.

Every colour is measured off his own live slider, nothing invented:
  brand green  #006649   heading + ORDER NOW pill on his current Banner_03
  gold         #FECB3C   the "CUSTOM BLINDS" type on Banner-free_shipping
  bubble gold  #CC9600   the 20% OFF speech-bubble outline on Banner_03
  navy         #061532   free_shipping right-hand panel
  teal         #235659   free_shipping trust strip
  charcoal     #212121   his body headline colour
  canvas       1900x634  exactly Banner_03_2_.png, so it drops into the slider
  photos       his own catalog imagery - no licensing question
  type         Poppins + Oswald, the two families his theme already loads

OFFER and ENDS come from the environment. They are deliberately NOT baked in:
they are the client's numbers to give, not mine to invent.
"""
import base64, os, re, sys

S = os.path.dirname(os.path.abspath(__file__))
W, H = 1900, 634

GREEN, GOLD, BGOLD = "#006649", "#FECB3C", "#CC9600"
NAVY, TEAL, CHAR = "#061532", "#235659", "#212121"
PANEL = "#f4f1ec"          # the warm neutral his Banner_03 fades to

OFFER = os.environ.get("OFFER", "20%")
ENDS = os.environ.get("ENDS", "ENDS MONDAY, SEPT 7")
SHUTTERS = "shots/EclipseShutters_TrackPearl_TrippleTrack_OA-web.jpg"
SHADES = "shots/graber-0681-pleated-shades-rs22-v1.png"
PHOTO_A = os.environ.get("PHOTO_A", SHUTTERS)
PHOTO_B = os.environ.get("PHOTO_B", SHADES)
PHOTO_C = os.environ.get("PHOTO_C", SHUTTERS)


def b64(rel):
    ext = "png" if rel.lower().endswith(".png") else "jpeg"
    with open(os.path.join(S, rel), "rb") as f:
        return "data:image/%s;base64,%s" % (ext, base64.b64encode(f.read()).decode())


def render(tpl, mapping):
    """Token substitution. CSS is full of % signs, so printf formatting is the
    wrong tool - one `38%` in a gradient blows the whole template up."""
    for k, v in mapping.items():
        tpl = tpl.replace("{{%s}}" % k, str(v))
    left = re.findall(r"\{\{(\w+)\}\}", tpl)
    if left:
        raise SystemExit("unsubstituted tokens: %s" % sorted(set(left)))
    return tpl


HEAD = render("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Oswald:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:{{W}}px;height:{{H}}px;overflow:hidden;background:#fff}
  .stage{position:relative;width:{{W}}px;height:{{H}}px;overflow:hidden;
         font-family:'Poppins',Arial,sans-serif}
  /* the dot grid his Banner_03 uses in the corners */
  .dots{position:absolute;width:74px;height:74px;
        background-image:radial-gradient(currentColor 2px,transparent 2px);
        background-size:18px 18px;opacity:.30}
</style>
""", dict(W=W, H=H))


# ---------------------------------------------------------------- design A
# Native to his existing Banner_03: warm panel left, photo right, green
# eyebrow, charcoal headline, gold flash, green CTA pill.
# The photo is FULL-BLEED with a single overlay gradient on top of it. An
# earlier version put the photo in its own right-hand box and faded inside
# that box, which left a visible vertical seam where the box began.
def design_a():
    return render("""
<style>
 .a-photo{position:absolute;inset:0}
 .a-photo img{position:absolute;inset:0;width:100%;height:100%;
              object-fit:cover;object-position:74% 56%}
 .a-veil{position:absolute;inset:0;background:linear-gradient(90deg,
   {{PANEL}} 0%, {{PANEL}} 33%, rgba(244,241,236,.98) 41%,
   rgba(244,241,236,.72) 51%, rgba(244,241,236,.30) 62%,
   rgba(244,241,236,.06) 73%, rgba(244,241,236,0) 82%)}
 /* a whisper of his warm gradient over the flat panel so it isn't dead flat */
 .a-warm{position:absolute;left:0;top:0;width:60%;height:100%;
   background:linear-gradient(150deg,rgba(255,255,255,.55) 0%,rgba(255,255,255,0) 55%,rgba(198,192,183,.30) 100%)}
 .a-txt{position:absolute;left:112px;top:0;height:{{H}}px;width:840px;
        display:flex;flex-direction:column;justify-content:center}
 .a-eyebrow{font-size:30px;font-weight:700;letter-spacing:.30em;color:{{GREEN}};
            text-transform:uppercase;margin-bottom:16px}
 .a-rule{width:74px;height:5px;background:{{BGOLD}};margin-bottom:22px;border-radius:3px}
 .a-off{font-size:118px;font-weight:800;line-height:.94;color:{{CHAR}};letter-spacing:-.025em}
 .a-off em{font-style:normal;color:{{GREEN}}}
 .a-sub{font-size:37px;font-weight:600;color:{{CHAR}};margin-top:12px;letter-spacing:-.005em}
 .a-note{font-size:25px;font-weight:400;font-style:italic;color:#5d5952;margin-top:14px}
 .a-cta{margin-top:34px;align-self:flex-start;
        background:{{GREEN}};color:#fff;font-size:23px;font-weight:600;letter-spacing:.09em;
        padding:19px 50px;border-radius:40px;text-transform:uppercase;
        box-shadow:0 8px 22px rgba(0,102,73,.30)}
 .a-flash{position:absolute;right:120px;top:70px;background:{{GOLD}};color:{{CHAR}};
          font-size:22px;font-weight:700;letter-spacing:.10em;padding:15px 30px;
          border-radius:8px;transform:rotate(-3deg);
          box-shadow:0 10px 26px rgba(0,0,0,.26)}
 .a-d1{left:44px;top:52px;color:{{GREEN}}}
</style>
<div class="stage">
  <div class="a-photo"><img src="{{PA}}"></div>
  <div class="a-veil"></div>
  <div class="a-warm"></div>
  <div class="dots a-d1"></div>
  <div class="a-txt">
    <div class="a-eyebrow">Labor&nbsp;Day Sale</div>
    <div class="a-rule"></div>
    <div class="a-off">{{OFFER}} <em>OFF</em></div>
    <div class="a-sub">All Custom Blinds &amp; Shades</div>
    <div class="a-note">Free shipping right to your door &nbsp;&middot;&nbsp; Free in-home consultation</div>
    <div class="a-cta">Shop the Sale</div>
  </div>
  <div class="a-flash">{{ENDS}}</div>
</div>
""", dict(H=H, GREEN=GREEN, GOLD=GOLD, BGOLD=BGOLD, CHAR=CHAR, PANEL=PANEL,
          PA=b64(PHOTO_A), OFFER=OFFER, ENDS=ENDS))


# ---------------------------------------------------------------- design B
# The bolder one, built from his Banner-free_shipping language: photo left,
# navy panel right behind a sweeping curve, gold headline, teal trust strip.
# The date moved out of the eyebrow - at this letter-spacing it wrapped onto
# a second line and broke the right-aligned block.
def design_b():
    trust = ["Free Samples", "Free Shipping", "Free Design Consultation",
             "Satisfaction Guarantee"]
    items = "".join("<span>%s</span>" % t for t in trust)
    return render("""
<style>
 .b-stage{background:{{NAVY}}}
 .b-photo{position:absolute;top:0;left:0;width:1120px;height:{{H}}px}
 .b-photo img{position:absolute;inset:0;width:100%;height:100%;
              object-fit:cover;object-position:44% 50%}
 /* the sweep, same gesture as the curve on his free-shipping banner */
 .b-gold-edge{position:absolute;top:0;right:0;width:1188px;height:{{H}}px;
          background:{{BGOLD}};clip-path:ellipse(88% 128% at 86.5% 50%)}
 .b-curve{position:absolute;top:0;right:0;width:1180px;height:{{H}}px;
          background:{{NAVY}};clip-path:ellipse(88% 128% at 86% 50%)}
 .b-txt{position:absolute;right:96px;top:0;height:{{H}}px;width:820px;
        display:flex;flex-direction:column;justify-content:center;align-items:flex-end;
        text-align:right;padding-bottom:60px}
 .b-eyebrow{font-size:29px;font-weight:600;letter-spacing:.32em;color:#fff;opacity:.90;
            text-transform:uppercase;margin-bottom:14px;white-space:nowrap}
 .b-off{font-size:112px;font-weight:800;line-height:.95;color:{{GOLD}};letter-spacing:-.02em;
        text-shadow:0 6px 20px rgba(0,0,0,.35);white-space:nowrap}
 .b-sub{font-size:35px;font-weight:500;color:#fff;margin-top:10px;white-space:nowrap}
 .b-note{font-size:22px;font-weight:400;color:#c4cbd8;margin-top:12px;letter-spacing:.02em}
 .b-row{display:flex;align-items:center;gap:22px;margin-top:30px}
 .b-cta{background:{{GOLD}};color:{{NAVY}};font-size:23px;font-weight:700;
        letter-spacing:.09em;padding:19px 48px;border-radius:40px;text-transform:uppercase;
        box-shadow:0 10px 26px rgba(0,0,0,.35);white-space:nowrap}
 .b-ends{color:#fff;font-size:19px;font-weight:600;letter-spacing:.11em;white-space:nowrap;
         border:2px solid rgba(255,255,255,.50);padding:15px 24px;border-radius:40px}
 .b-strip{position:absolute;left:0;bottom:0;width:{{W}}px;height:76px;background:{{TEAL}};
          display:flex;align-items:center;gap:64px;padding-left:66px}
 .b-strip span{color:#fff;font-size:20px;font-weight:600;letter-spacing:.05em;
               position:relative;padding-left:30px}
 .b-strip span:before{content:"";position:absolute;left:0;top:50%;
   transform:translateY(-50%) rotate(-45deg);width:16px;height:9px;
   border-left:3px solid {{GOLD}};border-bottom:3px solid {{GOLD}}}
</style>
<div class="stage b-stage">
  <div class="b-photo"><img src="{{PB}}"></div>
  <div class="b-gold-edge"></div>
  <div class="b-curve"></div>
  <div class="b-txt">
    <div class="b-eyebrow">Labor&nbsp;Day Sale</div>
    <div class="b-off">{{OFFER}} OFF</div>
    <div class="b-sub">All Custom Blinds &amp; Shades</div>
    <div class="b-note">Measured, made and shipped to your door</div>
    <div class="b-row">
      <div class="b-ends">{{ENDS}}</div>
      <div class="b-cta">Shop the Sale</div>
    </div>
  </div>
  <div class="b-strip">{{ITEMS}}</div>
</div>
""", dict(W=W, H=H, NAVY=NAVY, GOLD=GOLD, BGOLD=BGOLD, TEAL=TEAL,
          PB=b64(PHOTO_B), OFFER=OFFER, ENDS=ENDS, ITEMS=items))


# ---------------------------------------------------------------- design C
# Full-bleed room shot, Oswald condensed headline, slim red/white/blue bar as
# the only flag reference. The scrim falls off STEEPLY - a gentle one left a
# half-tinted haze across the middle of the photo that just looked muddy.
def design_c():
    return render("""
<style>
 .c-photo{position:absolute;inset:0}
 .c-photo img{position:absolute;inset:0;width:100%;height:100%;
              object-fit:cover;object-position:56% 58%}
 .c-scrim{position:absolute;inset:0;background:linear-gradient(90deg,
   rgba(6,21,50,.95) 0%, rgba(6,21,50,.93) 30%, rgba(6,21,50,.80) 42%,
   rgba(6,21,50,.38) 52%, rgba(6,21,50,.10) 61%, rgba(6,21,50,0) 70%)}
 .c-vig{position:absolute;inset:0;
   background:linear-gradient(180deg,rgba(6,21,50,.22) 0%,rgba(6,21,50,0) 30%,rgba(6,21,50,.18) 100%)}
 .c-txt{position:absolute;left:118px;top:0;height:{{H}}px;width:900px;
        display:flex;flex-direction:column;justify-content:center}
 .c-flag{display:flex;width:132px;height:8px;border-radius:4px;overflow:hidden;margin-bottom:26px}
 .c-flag i{flex:1}
 .c-eyebrow{font-family:'Oswald',Arial,sans-serif;font-size:32px;font-weight:400;
            letter-spacing:.40em;color:#fff;text-transform:uppercase;margin-bottom:10px}
 .c-off{font-family:'Oswald',Arial,sans-serif;font-size:132px;font-weight:600;line-height:.92;
        color:{{GOLD}};letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;
        text-shadow:0 6px 24px rgba(0,0,0,.40)}
 .c-sub{font-size:33px;font-weight:500;color:#fff;margin-top:16px;white-space:nowrap}
 .c-note{font-size:22px;font-weight:300;color:#cdd4e0;margin-top:12px}
 .c-row{display:flex;align-items:center;gap:26px;margin-top:34px}
 .c-cta{background:{{GOLD}};color:{{NAVY}};font-size:22px;font-weight:700;letter-spacing:.09em;
        padding:18px 46px;border-radius:40px;text-transform:uppercase;white-space:nowrap}
 .c-ends{color:#fff;font-size:20px;font-weight:600;letter-spacing:.12em;white-space:nowrap;
         border:2px solid rgba(255,255,255,.55);padding:15px 26px;border-radius:40px}
</style>
<div class="stage">
  <div class="c-photo"><img src="{{PC}}"></div>
  <div class="c-scrim"></div>
  <div class="c-vig"></div>
  <div class="c-txt">
    <div class="c-flag"><i style="background:#b22234"></i><i style="background:#fff"></i><i style="background:#3c3b6e"></i></div>
    <div class="c-eyebrow">Labor Day Sale</div>
    <div class="c-off">{{OFFER}} Off</div>
    <div class="c-sub">All Custom Blinds, Shades &amp; Shutters</div>
    <div class="c-note">Free shipping &nbsp;&middot;&nbsp; Free samples &nbsp;&middot;&nbsp; Free in-home consultation</div>
    <div class="c-row">
      <div class="c-cta">Shop the Sale</div>
      <div class="c-ends">{{ENDS}}</div>
    </div>
  </div>
</div>
""", dict(H=H, GOLD=GOLD, NAVY=NAVY, PC=b64(PHOTO_C), OFFER=OFFER, ENDS=ENDS))


DESIGNS = {"a": design_a, "b": design_b, "c": design_c}


def build(names, suffix=""):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    out = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        ctx = br.new_context(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg = ctx.new_page()
        for n in names:
            html = ("<!doctype html><html><head><meta charset='utf-8'>" + HEAD +
                    "</head><body>" + DESIGNS[n]() + "</body></html>")
            f = os.path.join(S, "banner_%s.html" % n)
            open(f, "w").write(html)
            pg.goto("file://" + f, wait_until="load", timeout=120000)
            pg.evaluate("()=>document.fonts.ready")
            pg.wait_for_timeout(2500)
            # fail loudly rather than silently shipping Arial
            bad = pg.evaluate("""()=>{const o=[];
              document.querySelectorAll('.a-off,.b-off,.c-off,.a-eyebrow,.b-eyebrow,.c-eyebrow').forEach(e=>{
                const cs=getComputedStyle(e), fam=cs.fontFamily.split(',')[0].replace(/'/g,'');
                if(!document.fonts.check(cs.fontWeight+' 40px "'+fam+'"')) o.push(e.className+':'+fam);});
              return o;}""")
            if bad:
                raise SystemExit("webfont did not load for: %s" % bad)
            # nothing may spill outside the canvas
            over = pg.evaluate("""()=>{const o=[];
              document.querySelectorAll('.stage *').forEach(e=>{const b=e.getBoundingClientRect();
                if(b.width&&(b.right>%d+1||b.left<-1||b.bottom>%d+1||b.top<-1))
                  o.push(e.className+' '+[b.left,b.top,b.right,b.bottom].map(Math.round).join(','));});
              return o;}""" % (W, H))
            if over:
                print("   WARN overflow:", over)
            png = os.path.join(S, "laborday_%s%s.png" % (n, suffix))
            pg.screenshot(path=png, clip={"x": 0, "y": 0, "width": W, "height": H})
            im = Image.open(png)
            print("  %-28s %s  %d KB" % (os.path.basename(png), im.size,
                                         os.path.getsize(png) // 1024))
            out.append(png)
        ctx.close(); br.close()
    return out


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if a in DESIGNS] or ["a", "b", "c"]
    print("offer=%s  ends=%s  canvas=%dx%d" % (OFFER, ENDS, W, H))
    build(names, os.environ.get("SUFFIX", ""))
