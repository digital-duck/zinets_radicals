# Kaiti (Modern) Character Generation Guide

**Purpose:** Generate modern Kaiti-style (楷体) character images for Paper #2 figures
**Target:** 76 characters across 13 sections
**Output:** `characters/kaiti/char-{hanzi}-kaiti.png`
**Status:** Ready for batch generation

---

## Why "Kaiti" Not "Modern"

**Explicit naming principle (Python philosophy):**
- ❌ "modern" - too vague (what style? print? handwritten? digital?)
- ✅ "kaiti" - explicit style specification (楷体 = standard script, modern hand-written style)

**File naming convention:**
```
char-{hanzi}-oracle.png  # Oracle bone script (~1200 BCE)
char-{hanzi}-bronze.png  # Bronze inscription script (~1200-700 BCE)
char-{hanzi}-seal.png    # Seal script (Qin dynasty, 221-206 BCE)
char-{hanzi}-kaiti.png   # Kaiti/Regular script (modern standard)
```

**Examples:**
- `char-人-kaiti.png`
- `char-父-kaiti.png`
- `char-分-kaiti.png`

---

## Resource Evaluation & Recommendation

### Previous Experience: Makemeahanzi ✅

**You mentioned using this in another project - excellent choice!**

**Makemeahanzi:**
- GitHub: https://github.com/skishore/makemeahanzi
- **Data format:** JSON with SVG stroke paths
- **Coverage:** ~9,000+ characters
- **Quality:** High (based on KanjiVG data)
- **Advantages:** Programmatic, consistent, stroke data available
- **Your experience:** Already familiar, proven workflow

**Why this is perfect for your workflow:**
- You've used it before (no learning curve)
- JSON data structure (easy Python processing)
- SVG paths (can render to PNG at any resolution)
- Consistent styling across all characters
- Open source, well-maintained

### Alternative Resources (For Reference)

**1. Hanzi Writer**
- Website: https://hanziwriter.org/
- **Pros:** Beautiful animations, interactive, SVG export
- **Cons:** Primarily web-based, less suitable for batch processing
- **Use case:** Manual generation, quality check, visualization

**2. Python + Font Libraries**
- Pillow + Noto Serif CJK font
- **Pros:** Simple, fast batch processing, high quality
- **Cons:** Static rendering (no stroke order data)
- **Use case:** Quick generation when stroke data not needed

**3. Noto Serif CJK Fonts (Google)**
- Download: https://fonts.google.com/noto/specimen/Noto+Serif+SC
- **Pros:** Free, excellent quality, multiple weights
- **Cons:** Just font rendering, not stroke-by-stroke
- **Use case:** Fallback or supplementary to Makemeahanzi

### Recommendation: Makemeahanzi + Noto Serif CJK Hybrid

**Primary method:** Makemeahanzi (since you have experience)
**Backup method:** Python + Noto font (for any missing characters)

**Workflow:**
1. Use Makemeahanzi for all 76 characters
2. If any character missing from Makemeahanzi → fallback to Noto font rendering
3. Quality check: compare against oracle/bronze/seal forms for accuracy

---

## Technical Approach with Makemeahanzi

### Data Structure

**Makemeahanzi provides JSON files like:**
```json
{
  "character": "人",
  "strokes": [
    "M 350 750 Q 380 720 ...",  // SVG path data
    "M 550 150 Q 520 180 ..."
  ],
  "medians": [...],
  "radStrokes": [0, 1]
}
```

### Rendering Pipeline

**Step 1: Load character data**
```python
import json

with open('graphics.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['character'] == '人':
            strokes = data['strokes']
            # Process strokes
```

**Step 2: Render SVG paths to PNG**
```python
import cairosvg
from io import BytesIO

# Create SVG with strokes
svg_content = f'''
<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
  <g transform="scale(1, -1) translate(0, -900)">
    {stroke_paths}
  </g>
</svg>
'''

# Render to PNG
png_bytes = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
```

**Step 3: Save with consistent sizing**
```python
from PIL import Image
from io import BytesIO

img = Image.open(BytesIO(png_bytes))
img = img.resize((250, 250), Image.LANCZOS)  # Consistent size
img.save(f'characters/kaiti/char-{hanzi}-kaiti.png')
```

### Quality Considerations

**Resolution:**
- Target: 250x250px minimum (300x300px better for print)
- Your LaTeX uses `width=1.2cm` so resolution will scale nicely
- Higher resolution = better quality in PDF output

**Stroke Weight:**
- Makemeahanzi default is good for standard viewing
- Can adjust SVG stroke-width if needed (2-3 for standard, 1-2 for thin)

**Centering:**
- Makemeahanzi data is pre-centered in 1024x1024 viewBox
- Maintain aspect ratio when resizing
- Add padding if needed for consistent spacing

**Background:**
- White background (`#FFFFFF`)
- Black strokes (`#000000`)
- Matches oracle/bronze/seal image style

---

## Batch Generation Workflow

### Prerequisites

**Install dependencies:**
```bash
pip install cairosvg pillow pyyaml
```

**Download Makemeahanzi data:**
```bash
# Clone repository
git clone https://github.com/skishore/makemeahanzi.git

# Data file location
# makemeahanzi/graphics.txt (JSON lines format)
```

### Automated Script

**See `generate_kaiti_chars.py` (created separately)**

**What the script does:**
1. Reads `figures-config.yaml`
2. Extracts all unique hanzi characters (76 total)
3. Looks up each character in Makemeahanzi data
4. Renders SVG strokes to PNG
5. Saves as `char-{hanzi}-kaiti.png`
6. Reports any missing characters

**Usage:**
```bash
cd docs/arxiv/figures/
python3 generate_kaiti_chars.py
```

**Expected output:**
```
Loading Makemeahanzi data from: /path/to/graphics.txt
Loaded 9,000+ character definitions

Processing 76 characters from figures-config.yaml:

✓ Generated: char-人-kaiti.png
✓ Generated: char-娘-kaiti.png
✓ Generated: char-母-kaiti.png
...
✓ Generated: char-鬲-kaiti.png

Summary:
========================================
Total characters:        76
Successfully generated:  76
Missing from data:       0
========================================

All kaiti character images generated!
Saved to: characters/kaiti/
```

---

## Fallback Strategy

### If Character Missing from Makemeahanzi

**Rare, but possible for:**
- Variant forms
- Rare characters
- Very ancient characters

**Fallback: Use Noto Serif CJK font**

```python
from PIL import Image, ImageDraw, ImageFont

def generate_with_font(hanzi, output_path):
    """Fallback: render using Noto Serif CJK font"""

    # Load font
    font = ImageFont.truetype("NotoSerifCJKsc-Regular.otf", 180)

    # Create image
    img = Image.new('RGB', (250, 250), 'white')
    draw = ImageDraw.Draw(img)

    # Center the character
    bbox = draw.textbbox((0, 0), hanzi, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (250 - text_width) / 2 - bbox[0]
    y = (250 - text_height) / 2 - bbox[1]

    # Draw
    draw.text((x, y), hanzi, font=font, fill='black')

    # Save
    img.save(output_path)
    print(f"✓ Generated (font fallback): {output_path}")
```

**When to use:**
- Makemeahanzi doesn't have the character
- Need quick placeholder for testing
- Character is too rare for stroke data

---

## Quality Assurance

### Visual Inspection Checklist

**For each generated image:**

1. **Correct character?** ✅
   - Compare hanzi in filename vs. rendered image
   - Verify against oracle/bronze/seal forms

2. **Proper centering?** ✅
   - Character centered in 250x250 frame
   - Consistent padding around character
   - Not clipped at edges

3. **Stroke quality?** ✅
   - Clean, sharp strokes (not pixelated)
   - Proper stroke weight (not too thin or thick)
   - Smooth curves (no jagged edges)

4. **Consistent style?** ✅
   - All characters use same stroke style
   - Same visual weight across characters
   - Uniform sizing (large chars not overwhelming, small chars not tiny)

5. **Readable at target size?** ✅
   - Test: resize to 1.2cm width (your LaTeX size)
   - Should be clearly readable
   - Details preserved at small size

### Comparison Test

**Side-by-side comparison:**
- Oracle → Bronze → Seal → Kaiti
- Visual evolution should be clear
- Kaiti should be recognizably "same character"

**Example: 人 (person)**
```
Oracle: Stick figure (clear human form)
Bronze: Simplified stick figure
Seal:   More abstract, standardized
Kaiti:  Modern 人 (two strokes, recognizable)
```

**If evolution is NOT clear:**
- Check if correct historical forms selected
- Verify kaiti rendering matches modern standard
- May need manual adjustment

### Automated Checks

**Script includes validation:**
- File size check (too small = failed render)
- Image dimensions (must be 250x250)
- Non-empty image (not blank white)
- Character coverage (76/76 generated)

---

## Integration with Figure Generation

### Updated Workflow

**Step 1: Generate kaiti images (this guide)**
```bash
python3 generate_kaiti_chars.py
# Output: 76 PNG files in characters/kaiti/
```

**Step 2: Verify YAML updated (kaiti not modern)**
```yaml
files:
  oracle: "char-人-oracle.png"
  bronze: "char-人-bronze.png"
  seal: "char-人-seal.png"
  kaiti: "char-人-kaiti.png"  # Updated naming!
```

**Step 3: Update generate_figures.py (if needed)**
- Check references to "modern" → change to "kaiti"
- Update file paths: `characters/modern/` → `characters/kaiti/`
- Update column headers: "Modern" → "Kaiti" or "Modern (Kaiti)"

**Step 4: Generate all figures**
```bash
python3 generate_figures.py all
```

**Step 5: Review output**
```bash
# Check LaTeX output
cat generated/fig-2.1-evolution.tex

# Check Markdown preview
cat generated/fig-2.1-evolution.md
```

**Step 6: Compile LaTeX (test)**
```bash
# In your paper directory
pdflatex paper-2nd-living-fossil-v0.2.tex
# Check if images load correctly
```

### Expected Figure Structure

**LaTeX table:**
```latex
\begin{tabular}{|c|c|c|c|l|}
\hline
\textbf{Oracle} & \textbf{Bronze} & \textbf{Seal} & \textbf{Kaiti} & \textbf{Character} \\
\hline
\includegraphics[width=1.2cm]{figures/characters/oracle/char-人-oracle.png} &
\includegraphics[width=1.2cm]{figures/characters/bronze/char-人-bronze.png} &
\includegraphics[width=1.2cm]{figures/characters/seal/char-人-seal.png} &
\includegraphics[width=1.2cm]{figures/characters/kaiti/char-人-kaiti.png} &
人 (ren) - Person, human \\
\hline
\end{tabular}
```

**Markdown table:**
```markdown
| Oracle | Bronze | Seal | Kaiti | Character |
|--------|--------|------|-------|-----------|
| ![oracle](characters/oracle/char-人-oracle.png) | ![bronze](characters/bronze/char-人-bronze.png) | ![seal](characters/seal/char-人-seal.png) | ![kaiti](characters/kaiti/char-人-kaiti.png) | 人 (ren) - Person, human |
```

---

## Character-Specific Considerations

### Complex Characters

**Some characters are intricate (e.g., 鬲, 器):**
- May need larger rendering size (300x300 or 400x400)
- Then downsize to 250x250 for consistency
- Check readability at small size
- May need to adjust stroke weight

### Variant Forms

**Some characters have multiple modern forms:**
- Traditional vs. Simplified (e.g., 網 vs. 网)
- Regional variants (Taiwan, Hong Kong, Mainland)

**Decision:**
- Use **Traditional forms** for consistency with oracle/bronze/seal
- These are "living fossil" characters - traditional preserves ancient structure
- Simplified forms often lose semantic components (e.g., 愛 → 爱 loses 心 heart)

**Exception:**
- If your paper discusses simplification (Section 2.x), show both
- Otherwise: traditional only

### Missing Historical Forms

**Characters like 娘, 爸, 銀, 钱 (late-developed):**
- May have NO oracle or bronze forms
- Kaiti is the ONLY available historical form
- This is fine - your paper notes these as "(unavailable)"

**Table handling:**
```
Oracle: (unavailable)
Bronze: (unavailable)
Seal:   [seal form image]
Kaiti:  [kaiti form image]
```

---

## Troubleshooting

### Problem: Character not in Makemeahanzi data

**Solution:**
- Use Noto font fallback (see above)
- Or: manually create SVG using Hanzi Writer
- Or: use high-quality screenshot from online tool

### Problem: Generated image is blank

**Causes:**
- SVG parsing error
- Missing font in fallback
- File path issue

**Debug:**
```python
# Add verbose logging
print(f"Processing: {hanzi}")
print(f"Strokes found: {len(strokes)}")
print(f"SVG content: {svg_content[:200]}...")
```

### Problem: Character appears too small/large

**Solution:**
- Adjust viewBox scaling in SVG
- Use different font size in fallback
- Post-process: resize with padding

### Problem: Inconsistent stroke weight

**Solution:**
- Set uniform stroke-width in SVG generation
- Use same font for all fallback characters
- May need to normalize Makemeahanzi output

### Problem: Images look pixelated in PDF

**Solution:**
- Increase render resolution (500x500 → downsize to 250x250)
- Use vector SVG if LaTeX supports it
- Check PDF viewer zoom (may look pixelated at 400% but fine at 100%)

---

## Performance Notes

### Batch Generation Speed

**Expected timing:**
- Loading Makemeahanzi data: ~2-5 seconds (9,000+ characters)
- Processing each character: ~0.1-0.2 seconds
- Total for 76 characters: ~10-20 seconds

**Optimization:**
- Load Makemeahanzi data once, reuse for all characters
- Use multiprocessing for 10x speedup (if needed)
- Cache rendered SVGs (if regenerating frequently)

### Storage

**Disk space:**
- Each PNG: ~5-15 KB (250x250, simple character)
- 76 characters: ~500 KB - 1 MB total
- Negligible storage impact

---

## Maintenance & Updates

### When to Regenerate

**Scenarios:**
- Changed resolution (e.g., 250x250 → 300x300)
- Updated styling (stroke weight, padding)
- Added new characters to study
- Fixed errors in specific characters

**How to regenerate:**
```bash
# Regenerate all
python3 generate_kaiti_chars.py

# Or regenerate specific character
python3 generate_kaiti_chars.py --char 人
```

### Version Control

**Include in git:**
- ✅ `generate_kaiti_chars.py` (script)
- ✅ `README-kaiti.md` (this guide)
- ✅ `figures-config.yaml` (character list)

**Exclude from git (.gitignore):**
- ❌ `characters/kaiti/*.png` (generated files, can recreate)
- ❌ `makemeahanzi/` (external dependency, large)

**Exception:**
- If paper submission requires all images → include in submission archive
- For version control: regenerate from script as needed

---

## Resources & References

### Makemeahanzi
- **GitHub:** https://github.com/skishore/makemeahanzi
- **Data format:** JSON lines (graphics.txt)
- **Coverage:** 9,000+ characters
- **License:** LGPL (compatible with academic use)

### Noto Serif CJK (Fallback Font)
- **Download:** https://fonts.google.com/noto/specimen/Noto+Serif+SC
- **Variants:** SC (Simplified), TC (Traditional), JP (Japanese), KR (Korean)
- **License:** SIL Open Font License (free for any use)
- **Recommendation:** Use TC (Traditional) for consistency with ancient forms

### Hanzi Writer (Manual/Visual Check)
- **Website:** https://hanziwriter.org/
- **Use case:** Visual verification, animation preview
- **Export:** SVG (can convert to PNG if needed)

### Alternative: KanjiVG
- **Website:** https://kanjivg.tagaini.net/
- **Relation:** Makemeahanzi builds on KanjiVG data
- **Use case:** If you need raw SVG files directly

### Python Libraries
- **cairosvg:** SVG → PNG rendering
- **Pillow:** Image manipulation, resizing
- **pyyaml:** Config file parsing

---

## Summary Workflow

**Complete kaiti generation process:**

1. ✅ Clone/download Makemeahanzi data
2. ✅ Install Python dependencies (`cairosvg`, `pillow`, `pyyaml`)
3. ✅ Run `generate_kaiti_chars.py`
4. ✅ Visual quality check (random sampling)
5. ✅ Update `generate_figures.py` if needed (modern → kaiti)
6. ✅ Generate all figures (`python3 generate_figures.py all`)
7. ✅ Review Markdown previews (`cat generated/*.md`)
8. ✅ Test LaTeX compilation (`pdflatex` with figure includes)
9. ✅ Final paper integration

**Time estimate:**
- Setup (first time): 15-30 minutes
- Generation: 30 seconds
- Quality check: 5-10 minutes
- **Total: ~30-45 minutes for complete workflow**

**Result:**
- 76 high-quality kaiti character images
- Consistent styling across all characters
- Ready for Paper #2 figure integration
- Reproducible (script + config)

---

## Why This Approach Works

**Advantages of Makemeahanzi:**
- ✅ You have prior experience (no learning curve)
- ✅ Programmatic (fully automated)
- ✅ High quality (based on curated KanjiVG data)
- ✅ Consistent (same stroke style for all)
- ✅ Open source (no licensing issues)
- ✅ Well-maintained (active project)

**Advantages of explicit "kaiti" naming:**
- ✅ Clear what style is used (not ambiguous "modern")
- ✅ Extensible (could add 'xingshu', 'caoshu' variants later)
- ✅ Pythonic (explicit is better than implicit)
- ✅ Professional (shows careful consideration)

**Integration with existing workflow:**
- ✅ Matches oracle/bronze/seal naming convention
- ✅ Compatible with `generate_figures.py` (minor update)
- ✅ Works with LaTeX/Markdown output
- ✅ Supports your Paper #2 structure

---

**Ready to generate! See `generate_kaiti_chars.py` for the automated script.**

*Last updated: 2025-01-30*
*Makemeahanzi version: Latest (check GitHub for updates)*
