# Perfecto Blinds - Labor Day banners

Slider artwork for perfectoblinds.com, Labor Day 2026 (Monday 7 September).

## Files

| File | Size | Notes |
|---|---|---|
| `laborday_a.png` | 1900x634 | Option A - matches the current Banner_03 slide |
| `laborday_b.png` | 1900x634 | Option B - navy sweep, gold, trust strip |
| `laborday_c.png` | 1900x634 | Option C - full-bleed room shot |
| `laborday_a_10pct.png` | 1900x634 | Option A rendered at 10% / "Ends Thursday, Sept 10" |
| `laborday_*.jpg` | 1900x634 | Same artwork, ~175 KB instead of ~1 MB |
| `laborday_OPTIONS.png` | - | The three options side by side |
| `laborday_MOBILE.png` | - | What the slider does to a banner on a phone |

1900x634 is the exact pixel size of the existing `Banner_03_2_.png`, so these
drop into the Mageplaza banner slider with no layout change.

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

## The discount figure is a placeholder

The homepage currently shows more than one offer at the same time:

- header strip: **"Blinds Sale | Up to 10% Off | Ends: Sept 10"**
- slider Banner_03: **"SHOP 20% OFF"**
- promo blocks: "Great offer 20 % OFF", "Great offer 10 % Off",
  "More savings 10% Off", "More savings 20 % Off"

These banners were rendered at 20% because that is what the slider itself says.
The number and the end date are one-line changes - see `mkbanner.py`:

    OFFER="15%" ENDS="ENDS MONDAY, SEPT 7" python3 mkbanner.py a b c
