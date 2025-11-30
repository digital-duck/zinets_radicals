# Kaiti Character Generation - Quick Start

**Goal:** Generate 76 modern Kaiti-style character images automatically

---

## Prerequisites

### 1. Install Python Dependencies

```bash
pip install pillow pyyaml cairosvg
```

**What each does:**
- `pillow` - Image processing (required)
- `pyyaml` - YAML config parsing (required)
- `cairosvg` - SVG rendering (optional but recommended for Makemeahanzi)

### 2. Download Makemeahanzi Data (Recommended)

**Option A: Clone Repository**
```bash
conda activate zinets2
cd ~/projects/Proj-ZiNets
git clone https://github.com/skishore/makemeahanzi.git
```

**Option B: Download graphics.txt only**
```bash
wget https://raw.githubusercontent.com/skishore/makemeahanzi/master/graphics.txt
```

### 3. (Optional) Download Noto Serif CJK Font

**For fallback if Makemeahanzi missing characters:**

Download from: https://fonts.google.com/noto/specimen/Noto+Serif+TC

Or use system fonts (script auto-detects).

---

## Quick Usage

### Basic (Auto-detect Makemeahanzi)

```bash
cd docs/arxiv/figures/
python3 generate_kaiti_chars.py --makemeahanzi ~/projects/Proj-ZiNets/makemeahanzi/graphics.txt
```

### Specify Makemeahanzi Path

```bash
python3 generate_kaiti_chars.py --makemeahanzi ~/makemeahanzi/graphics.txt
```

### Custom Output Size

```bash
python3 generate_kaiti_chars.py --size 300
```

### Custom Font Fallback

```bash
python3 generate_kaiti_chars.py --font /path/to/NotoSerifCJKtc-Regular.otf
```

---

## Expected Output

```
Initializing Kaiti character generator...
Found Makemeahanzi data: /home/user/makemeahanzi/graphics.txt
Loading Makemeahanzi data from: /home/user/makemeahanzi/graphics.txt
Loaded 9000+ character definitions from Makemeahanzi

Processing 76 unique characters from figures-config.yaml:
============================================================
  ✓ Generated: char-人-kaiti.png
  ✓ Generated: char-女-kaiti.png
  ✓ Generated: char-母-kaiti.png
  ...
  ✓ Generated: char-鬲-kaiti.png

============================================================
GENERATION SUMMARY
============================================================
Total characters:        76
Successfully generated:  76
Failed:                  0
Missing from data:       0
Used font fallback:      0
============================================================

✓ All kaiti character images generated successfully!

Output saved to: characters/kaiti/

Next step: python3 generate_figures.py all
```

---

## Troubleshooting

### Problem: "cairosvg not installed"

**Solution:**
```bash
pip install cairosvg
```

If that fails (C dependency issues):
```bash
# Use font fallback instead (no cairosvg needed)
python3 generate_kaiti_chars.py --font /path/to/font.otf
```

### Problem: "Makemeahanzi data not found"

**Solution:** Specify path manually
```bash
python3 generate_kaiti_chars.py --makemeahanzi /path/to/graphics.txt
```

Or let it fall back to font rendering (still works!)

### Problem: "No font available for fallback"

**Solution:** Download Noto Serif CJK and specify:
```bash
python3 generate_kaiti_chars.py --font NotoSerifCJKtc-Regular.otf
```

### Problem: Some characters look wrong

**Check:**
1. Compare with oracle/bronze/seal forms (visual consistency)
2. Verify correct character in filename vs. image
3. Try regenerating that specific character
4. May need manual correction for complex characters

---

## What Gets Generated

**Files created:** 76 PNG images in `characters/kaiti/`

**Naming pattern:** `char-{hanzi}-kaiti.png`

**Examples:**
- `char-人-kaiti.png`
- `char-父-kaiti.png`
- `char-分-kaiti.png`

**Size:** 250x250 pixels (default, customize with `--size`)

**Format:** PNG, white background, black strokes

---

## Next Steps

### 1. Visual Quality Check

```bash
# View random sample
ls characters/kaiti/ | shuf | head -10
```

Open a few images to verify quality.

### 2. Generate All Figures

```bash
python3 generate_figures.py all
```

This creates:
- 15 LaTeX table files (`generated/fig-*.tex`)
- 15 Markdown preview files (`generated/fig-*.md`)

### 3. Preview Output

```bash
# View Markdown preview
cat generated/fig-2.1-evolution.md
```

### 4. Check Figure Integration

```bash
# Test LaTeX compilation
cd ../../  # Go to paper directory
pdflatex paper-2nd-living-fossil-v0.2.tex
```

---

## For More Details

See **README-kaiti.md** in project root for:
- Technical architecture
- Makemeahanzi details
- Fallback strategies
- Quality assurance guidelines
- Troubleshooting advanced issues

---

**That's it! Run the script and you're done!** ✅
