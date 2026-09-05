# Perfecto Blinds - Labor Day banners

Slider artwork for perfectoblinds.com, Labor Day 2026 (Monday 7 September).

Confirmed by the client: **20% off, sitewide, on all products**, ending
**Monday 14 September**.

## Files

| File | Size | Notes |
|---|---|---|
| `laborday_a_sept14.jpg` | 1900x634 | **Live - desktop and tablet.** 147 KB |
| `laborday_m_sept14.jpg` | 780x940 | **Live - phones only.** 86 KB |
| `laborday_a_sept14.png` | 1900x634 | Same artwork, lossless, 1014 KB |
| `laborday_m_sept14.png` | 780x940 | Phone cut, lossless, 426 KB |
| `laborday_a.jpg` | 1900x634 | Earlier draft, "Ends Monday, Sept 7" |
| `laborday_a.png` | 1900x634 | as above, PNG |
| `laborday_a_sept10.jpg` | 1900x634 | Earlier draft, "Ends Thursday, Sept 10" |
| `laborday_a_sept10.png` | 1900x634 | as above, PNG |
| `laborday_b.png` / `.jpg` | 1900x634 | Option B - navy sweep, gold, trust strip |
| `laborday_c.png` / `.jpg` | 1900x634 | Option C - full-bleed room shot |
| `laborday_OPTIONS.png` | - | The three options side by side |
| `laborday_MOBILE.png` | - | What the slider does to a banner on a phone |

1900x634 is the exact pixel size of the existing `Banner_03_2_.png`, so these
drop into the Mageplaza banner slider with no layout change.

## The phone cut

The slider scales one wide image down to whatever width the screen is. At 390px
a 1900x634 banner renders about 130px tall and the headline lands at roughly
24px - technically legible, practically ignored. `laborday_m_sept14.jpg` is a
portrait canvas, 780x940, which renders 390x470 on a phone. The type is sized
against a 390px viewport rather than a 1900px one, so the headline arrives at
about 64px instead of 24px.

Both files are served from one banner record, so there is still only one slide
to manage. The browser picks which one to download - the phone never fetches the
wide file and the desktop never fetches the tall one:

```html
<picture>
  <source media="(max-width: 767px)" srcset="{{media url="wysiwyg/laborday_m_sept14.jpg"}}">
  <img src="{{media url="wysiwyg/laborday_a_sept14.jpg"}}" alt="..." />
</picture>
```

767px is the usual phone/tablet boundary, so tablets keep the wide banner and
only phones get the tall one.

## PNG or JPEG

Use the JPEG. The two banners currently in the slider are 1516 KB and 1581 KB
PNG - about 3 MB of banner before anything else on the homepage loads. The JPEG
here is 147 KB. Measured mean per-pixel difference against the PNG is
**1.63 / 255**, i.e. not visible on a photographic banner.

## Where the colours came from

Sampled from the two banners already in the slider, not chosen freehand:

| | Hex | Source |
|---|---|---|
| Brand green | `#006649` | heading + ORDER NOW pill, Banner_03 |
| Gold | `#FECB3C` | "CUSTOM BLINDS" type, Banner-free_shipping |
| Deep gold | `#CC9600` | 20% OFF speech-bubble outline, Banner_03 |
| Navy | `#061532` | right-hand panel, Banner-free_shipping |
| Teal | `#235659` | trust strip, Banner-free_shipping |
| Charcoal | `#212121` | body headline colour |

Type is Poppins and Oswald - both already loaded by the Porto theme.

Photography is the store's own catalog imagery (Eclipse shutters, Graber
pleated shades), so there is no third-party licensing question.

## Contradicting offers - cleared

The homepage used to show several offers at once, which would have argued with
the 20% banner. All of these are gone from the live page as of 4 September:

- header strip: "Blinds Sale | Up to 10% Off | Ends: Sept 10"
- promo blocks: "Great offer 20 % OFF", "Great offer 10 % Off",
  "More savings 10% Off", "More savings 20 % Off"

## Re-rendering

The offer and the end date are parameters, not baked in:

    OFFER="20%" ENDS="ENDS MONDAY, SEPT 14" SUFFIX="_sept14" python3 mkbanner.py a
    OFFER="20%" ENDS="ENDS MONDAY, SEPT 14" SUFFIX="_sept14" python3 mkbanner_m.py

`mkbanner.py` renders the wide file, `mkbanner_m.py` the phone one. Both refuse
to render if the webfonts did not load, so a run never silently ships Arial.

JPEGs are written at quality 86, progressive, optimized. Measured against the
PNG that gives 147 KB at 1.63/255 mean difference for the wide file, and 86 KB
at 1.92/255 for the phone file.
