# Image Collection Quick Reference

**Status: 40% Complete** 🎯

## File Naming Convention

### Standard Format
```
char-{hanzi}-{script}.png
```

**Examples:**
- `char-人-oracle.png` (single variant)
- `char-木-bronze.png`
- `char-水-seal.png`

### Multiple Variants (if you find multiple forms)
```
char-{hanzi}-{script}-{N}.png
```

**Examples:**
- `char-馬-oracle-1.png` (first variant)
- `char-馬-oracle-2.png` (second variant)
- `char-馬-oracle-3.png` (third variant)

## Directory Structure

Save images to:
```
figures/characters/oracle/char-{hanzi}-oracle.png
figures/characters/bronze/char-{hanzi}-bronze.png
figures/characters/seal/char-{hanzi}-seal.png
figures/characters/modern/char-{hanzi}-modern.png
```

## Workflow Steps

### 1. Download Image
Visit: https://hanziyuan.net/
Search for character, download historical form

### 2. Save with Correct Name
```bash
# Save to correct directory with character-based name
mv downloaded_image.png characters/oracle/char-人-oracle.png
```

### 3. Update YAML Status (Optional)
Edit `figures-config.yaml`:
```yaml
- hanzi: "人"
  status: "collected"  # Change from "pending" to "collected"
```

### 4. Check Progress Anytime
```bash
python3 generate_figures.py status
```

### 5. Generate Tables (when ready)
```bash
# Generate all figures
python3 generate_figures.py all

# Or separately
python3 generate_figures.py latex      # For paper
python3 generate_figures.py markdown   # For preview
```

## Character List (76 Total)

### Section 2.1: Early Human Society (5)
- 人 娘 母 女 好

### Section 2.2: Nature Observation (10)
- 日 月 星 木 金 水 火 土 石 山

### Section 2.3: Hunting & Domestication (3)
- 犬 器 哭

### Section 2.4: Cutting & Inscribing (5)
- 乂 匕 文 刀 刃

### Section 2.5: Agricultural Development (5)
- 田 禾 男 甫 良

### Section 2.6: Power Shift (5)
- 父 爸 交 斧 刀

### Section 2.7: Craftsmanship (8)
- 工 巧 功 力 巠 乍 作 炸

### Section 2.8: Metallurgy (5)
- 金 銀 钱 銅 冶

### Section 2.9: Military Development (5)
- 弓 矢 戈 叉 矛

### Section 2.10: Counting & Calendar (12)
- 甲 乙 丙 丁 子 丑 寅 卯 一 二 三 四

### Section 2.11: Measurement (5)
- 分 寸 尺 斗 斤

### Section 2.12: Flow & Hydraulics (6)
- 㐬 流 川 江 气 冰

### Section 2.13: Advanced Concepts (7)
- 尧 烧 晓 艮 屰 鬲 禺

**Total: 76 characters**

## Expected Files

- **Total expected**: 228 image files (76 chars × 3 scripts: oracle, bronze, seal)
- **Currently specified**: 216 files in YAML
- **Missing**: ~12 files (genuinely unavailable for later-developed characters)

## Missing Forms (Genuinely Unavailable)

### Missing Oracle Forms (7):
娘, 爸, 銀, 钱, 銅, 烧, 晓

### Missing Bronze Forms (5):
娘, 爸, 钱, 烧, 晓

### Missing Seal Forms (0):
All seal forms available!

**Note:** These characters developed later in Chinese history, so early forms don't exist. Leave these blank - the script will handle them automatically with "(unavailable)" placeholder.

## Tips for Efficient Collection

### Batch Download Strategy
1. **Start with seal forms** (all 76 available - 100% success rate)
2. **Then bronze forms** (71 available - 93% success rate)
3. **Finally oracle forms** (69 available - 91% success rate)

### Quality Check
- Verify image is clear and readable
- Check it's the correct historical form (oracle/bronze/seal)
- Ensure background is clean/white if possible

### Status Tracking
Update YAML as you go:
- `pending` → `collected` (image downloaded)
- `collected` → `verified` (quality checked)

### Time Saver
You can update status in batch using text editor:
```bash
# Open YAML in editor
vim figures-config.yaml

# Search and replace
:%s/status: "pending"/status: "collected"/g
```

## Quick Commands Reference

```bash
# Check how many images you have
find characters/ -name "*.png" | wc -l

# List missing oracle forms
ls characters/oracle/ | grep -v oracle || echo "Check which are missing"

# Check progress report
python3 generate_figures.py status

# Generate preview (Markdown) to see what you have
python3 generate_figures.py markdown

# View generated markdown
cat generated/fig-2.1-evolution.md
```

## Troubleshooting

### Image Not Showing in Generated Table
**Check:**
1. File name matches YAML exactly: `char-人-oracle.png` (not `char-ren-oracle.png`)
2. File is in correct directory: `characters/oracle/`
3. YAML entry exists for the character
4. File extension is lowercase `.png`

### Pinyin Confusion
**Don't use pinyin in filenames!** Use character:
- ❌ `char-ma-oracle.png` (which ma? 馬/媽/麻/嗎?)
- ✅ `char-馬-oracle.png` (unambiguous)

### Multiple Variants
If Richard Sears shows multiple oracle bone forms:
```
char-馬-oracle-1.png  (most representative)
char-馬-oracle-2.png  (alternative form)
char-馬-oracle-3.png  (rare variant)
```

Just use the first one in YAML, keep others for reference.

## Current Status at 40% Complete

You've collected approximately:
- **91 images** out of 228 expected
- About **30 characters** fully completed (all 3 forms)

**Keep going!** 🚀

The system is fully automated - once you hit 100%, just run:
```bash
python3 generate_figures.py all
```

And all 15 LaTeX tables + 15 Markdown previews will be generated instantly!

---

**Quick Help:**
- Design docs: `README.md` (complete system overview)
- Commands: `USAGE.md` (quick command reference)
- Setup info: `SETUP-COMPLETE.md`
- Click CLI: `CLICK-UPGRADE.md`
