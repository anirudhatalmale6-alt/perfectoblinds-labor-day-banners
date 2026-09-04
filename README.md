# Perfecto Blinds - Labor Day banners

Slider artwork for perfectoblinds.com, Labor Day 2026 (Monday 7 September).

Confirmed by the client: **20% off, sitewide, on all products**, ending
**Monday 14 September**.

## Files

| File | Size | Notes |
|---|---|---|
| `laborday_a_sept14.jpg` | 1900x634 | **This is the live one.** 147 KB |
| `laborday_a_sept14.png` | 1900x634 | Same artwork, lossless, 1014 KB |
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

## Still to fix on the site itself

The homepage shows more than one offer at the same time. Once the 20% banner
goes up, these will contradict it:

- header strip: **"Blinds Sale | Up to 10% Off | Ends: Sept 10"**
- promo blocks: "Great offer 20 % OFF", "Great offer 10 % Off",
  "More savings 10% Off", "More savings 20 % Off"

## Re-rendering

The offer and the end date are parameters, not baked in:

    OFFER="20%" ENDS="ENDS MONDAY, SEPT 14" SUFFIX="_sept14" python3 mkbanner.py a

JPEGs are written at quality 86, progressive, optimized - that is the setting
that gives 147 KB at a measured mean difference of 1.63/255 from the PNG.
