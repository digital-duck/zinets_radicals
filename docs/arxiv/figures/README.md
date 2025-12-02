# Figures Directory - Paper #2: Chinese Characters as Living Fossils

This directory contains all figure assets and generation infrastructure for Paper #2.

## Directory Structure

```
figures/
├── README.md                    # This file
├── figures-config.yaml          # Master configuration (drives generation)
├── generate_figures.py          # Python script to generate LaTeX/Markdown tables
│
├── characters/                  # Character-centric image library (reusable)
│   ├── oracle/                  # Oracle bone script images
│   │   └── char-{pinyin}-oracle.png
│   ├── bronze/                  # Bronze inscription images
│   │   └── char-{pinyin}-bronze.png
│   ├── seal/                    # Seal script images
│   │   └── char-{pinyin}-seal.png
│   └── modern/                  # Modern character images (optional)
│       └── char-{pinyin}-modern.png
│
└── generated/                   # Auto-generated output (LaTeX/Markdown)
    ├── fig-2.1-evolution.tex
    ├── fig-2.2a-evolution.tex
    └── ...
```

## File Naming Convention

**Character images:** `char-{pinyin}-{script}.png`

Examples:
- `char-ren-oracle.png` - 人 in oracle bone script
- `char-nv-bronze.png` - 女 in bronze script
- `char-jing-seal.png` - 巠 in seal script

**Pinyin romanization:**
- Use standard pinyin without tone marks
- For homonyms, add clarifying suffix (e.g., `mu` vs `mu-wood` for 母 vs 木)
- Consistent across all scripts for same character

## Configuration File: `figures-config.yaml`

The master configuration file contains:

1. **Section definitions** - All 13 case study sections (2.1-2.13)
2. **Character metadata** - Hanzi, pinyin, unicode, meaning, file paths
3. **Progress tracking** - Status field (pending/collected/verified)
4. **Figure specifications** - Captions, character groupings, split rules
5. **Conceptual diagrams** - Non-character figures (spoke wheel, dialectic, etc.)
6. **Generation settings** - Output formats, styling, placeholder text

### Status Values

- `pending` - Image not yet collected
- `collected` - Image file obtained from source
- `verified` - Image reviewed for quality and correctness

### Priority Values (for conceptual diagrams)

- `high` - Critical figures (巠 spoke wheel, 鬲 dialectic, phase cycle)
- `medium` - Important supporting figures (sexagenary cycle, pit traps)
- `low` - Enhancement figures (network diagrams, timeline)

## Workflow

### 1. Image Collection

**Primary source:** Richard Sears' Chinese Etymology database (https://hanziyuan.net/)

**For each character:**
1. Look up character on hanziyuan.net
2. Download oracle/bronze/seal script images
3. Save using naming convention: `char-{pinyin}-{script}.png`
4. Place in appropriate subdirectory (`oracle/`, `bronze/`, `seal/`)
5. Update `status: "collected"` in `figures-config.yaml`

**Image specifications:**
- Format: PNG (transparent background preferred) or JPG (white background)
- Resolution: 300 DPI minimum
- Size: 200x200px minimum per character
- Cropping: Tight crop around character, minimal whitespace

**Missing images:**
- If script form doesn't exist (e.g., 娘 has no oracle bone form), leave file path empty in YAML
- Generation script will insert "(unavailable)" placeholder

### 2. Image Verification

1. Visual review for clarity and correctness
2. Check against multiple sources if uncertain
3. Ensure consistent sizing across same script type
4. Update `status: "verified"` in `figures-config.yaml`

### 3. Figure Generation

Run generation script (to be created):

```bash
python generate_figures.py --format latex
python generate_figures.py --format markdown
```

Outputs:
- `generated/fig-2.1-evolution.tex` - LaTeX table for Section 2.1
- `generated/fig-2.1-evolution.md` - Markdown table for preview

### 4. Integration

Include generated LaTeX in paper:

```latex
\input{figures/generated/fig-2.1-evolution.tex}
```

## Figure Types

### 1. Character Evolution Grids (Primary)

**Format:** 4-column table (Oracle | Bronze | Seal | Modern)

**Example:**

| Oracle | Bronze | Seal | Modern | Character |
|--------|--------|------|--------|-----------|
| ![oracle](characters/oracle/char-ren-oracle.png) | ![bronze](characters/bronze/char-ren-bronze.png) | ![seal](characters/seal/char-ren-seal.png) | 人 | 人 (rén) - Person |
| ![oracle](characters/oracle/char-nv-oracle.png) | (unavailable) | ![seal](characters/seal/char-nv-seal.png) | 女 | 女 (nǚ) - Woman |

**Sections with evolution grids:**
- 2.1 - Early Human Society (5 chars: 人女母娘好)
- 2.2 - Nature Observation (split into 2.2a/2.2b: 8 chars total)
- 2.3 - Hunting & Domestication (5 chars: 犬器哭豕家)
- 2.4 - Cutting & Inscribing (5 chars: 乂匕文刀力)
- 2.5 - Agricultural Development (5 chars: 男田良甫禾)
- 2.6 - Power Shift (5 chars: 父交斧爸刀)
- 2.7 - Craftsmanship (6 chars: 工功巧巠乍作)
- 2.8 - Metallurgy (5 chars: 金銀钱銅冶)
- 2.9 - Military (5 chars: 弓矢戈叉矛)
- 2.10 - Counting & Calendar (split into 2.10a/2.10b: 10 chars total)
- 2.11 - Measurement (5 chars: 分寸尺斗斤)
- 2.12 - Flow & Hydraulics (6 chars: 㐬流川江气冰)
- 2.13 - Advanced Concepts (6 chars: 尧烧晓艮屰鬲)

**Total character evolution figures:** ~15 figures covering ~70 characters

### 2. Conceptual Diagrams (Secondary)

Non-character figures requiring custom creation:

**High priority:**
- `fig-2.7-spoke-wheel` - 巠 radial structure engineering diagram
- `fig-2.13-ge-dialectic` - 鬲 fusion/separation dialectical process
- `fig-2.12-phase-cycle` - Water phase cycle (ice ⇄ liquid ⇄ vapor)

**Medium priority:**
- `fig-2.10-sexagenary` - 60-combination grid (10 stems × 12 branches)
- `fig-2.3-pit-traps` - Coordinated pit trap system (器 analysis)

**Low priority:**
- `fig-2.13-gen-network` - 艮 semantic network coherence diagram
- `fig-overview-timeline` - Chronological timeline (Paleolithic → Philosophy)

## Progress Tracking

Use `figures-config.yaml` as the single source of truth for tracking:

```yaml
characters:
  - hanzi: "人"
    status: "verified"  # ← Update this field as you progress
    files:
      oracle: "char-ren-oracle.png"  # ← File collected
      bronze: "char-ren-bronze.png"  # ← File collected
      seal: "char-ren-seal.png"      # ← File collected
      modern: "char-ren-modern.png"  # ← Optional
```

**Query progress:**
```bash
# Count pending images
grep "status: \"pending\"" figures-config.yaml | wc -l

# Count collected images
grep "status: \"collected\"" figures-config.yaml | wc -l

# Count verified images
grep "status: \"verified\"" figures-config.yaml | wc -l
```

## Attribution

All character images sourced from:
- **Richard Sears' Chinese Etymology Database** (https://hanziyuan.net/)
- Oracle bone and bronze inscription images from archaeological records
- Public domain historical materials

**Proper citation in figure captions:**
> "Oracle bone and bronze inscription forms from Richard Sears' Chinese Etymology database (https://hanziyuan.net/). Seal script and modern forms from standard references."

## Notes

- **Reusability:** Character-centric naming allows same image files to be used across multiple sections if character appears in different contexts
- **Missing data:** Some characters genuinely lack oracle/bronze forms (later compositions) - use "(unavailable)" placeholder, don't fabricate
- **Quality control:** Verify images against multiple sources before marking "verified"
- **Backup:** Keep original high-resolution sources; generated outputs can be regenerated

## TODO

- [ ] Create `generate_figures.py` script for automated table generation
- [ ] Collect all character images from hanziyuan.net
- [ ] Create conceptual diagrams (spoke wheel, dialectic, phase cycle)
- [ ] Verify all collected images for accuracy
- [ ] Generate LaTeX tables for all sections
- [ ] Integrate generated tables into main paper
- [ ] Final review of figure quality and consistency

## Extra

石 岩 矿 斫 破 泵 牛 马 初 妇

## Contact

For questions about figure preparation or configuration updates, contact the paper author.
