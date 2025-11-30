# Figure Preparation System - Setup Complete ✓

## Summary

A systematic figure preparation infrastructure has been created for Paper #2: "Chinese Characters as Living Fossils". The system is designed for:

1. **Consistency** - Uniform grid layout across all character evolution figures
2. **Reusability** - Character-centric file naming allows cross-section reuse
3. **Automation** - YAML-driven generation of LaTeX/Markdown tables
4. **Progress Tracking** - Single configuration file tracks collection status
5. **Maintainability** - Comprehensive documentation and clear structure

## What Was Created

### Directory Structure ✓
```
figures/
├── README.md                    # Complete documentation
├── figures-config.yaml          # Master configuration (726 lines, 13 sections)
├── SETUP-COMPLETE.md           # This summary
│
├── characters/                  # Image library (empty, ready for population)
│   ├── oracle/
│   ├── bronze/
│   ├── seal/
│   └── modern/
│
└── generated/                   # Auto-generated output (empty, ready for scripts)
```

### Configuration File ✓

**`figures-config.yaml`** contains complete specifications for:

**Character Evolution Grids (13 sections):**
- Section 2.1: Early Human Society (5 characters)
- Section 2.2: Nature Observation (8 characters, split into 2.2a/2.2b)
- Section 2.3: Hunting & Domestication (5 characters)
- Section 2.4: Cutting & Inscribing (5 characters)
- Section 2.5: Agricultural Development (5 characters)
- Section 2.6: Power Shift (5 characters)
- Section 2.7: Craftsmanship (6 characters)
- Section 2.8: Metallurgy (5 characters)
- Section 2.9: Military (5 characters)
- Section 2.10: Counting & Calendar (10 characters, split into 2.10a/2.10b)
- Section 2.11: Measurement (5 characters)
- Section 2.12: Flow & Hydraulics (6 characters)
- Section 2.13: Advanced Concepts (6 characters)

**Total:** ~70 characters across ~15 evolution grid figures

**Conceptual Diagrams (7 additional figures):**
- fig-2.7-spoke-wheel (巠 engineering) - HIGH priority
- fig-2.13-ge-dialectic (鬲 dialectic) - HIGH priority
- fig-2.12-phase-cycle (water phases) - HIGH priority
- fig-2.10-sexagenary (60-cycle grid) - MEDIUM priority
- fig-2.3-pit-traps (器 hunting) - MEDIUM priority
- fig-2.13-gen-network (艮 coherence) - LOW priority
- fig-overview-timeline (chronology) - LOW priority

## Key Design Decisions (As Per Your Requirements)

### 1. Character-Centric Naming ✓
```
char-ren-oracle.png
char-ren-bronze.png
char-ren-seal.png
char-ren-modern.png
```

**Benefits:**
- Reusable across sections if character appears multiple times
- Easier library management
- Loses section context (acceptable trade-off)

### 2. YAML Configuration ✓
- Allows comments for documentation
- Drives both LaTeX and Markdown generation
- Single source of truth

### 3. Integrated Progress Tracking ✓
- No separate checklist needed
- Status field in YAML: `pending` | `collected` | `verified`
- Query progress with simple grep commands

### 4. Uniform Grid Layout ✓
```
| Oracle | Bronze | Seal | Modern | Character |
|--------|--------|------|--------|-----------|
| img    | img    | img  | 人     | 人 (rén)  |
```

- 4 script columns + 1 info column
- Missing images show "(unavailable)"
- Horizontal scanning shows evolution

### 5. "(unavailable)" Placeholder ✓
- Clear indication when script form doesn't exist
- No confusion with empty cells
- Maintains table structure

## File Naming Examples

**Oracle bone scripts:**
- `char-ren-oracle.png` - 人
- `char-nv-oracle.png` - 女
- `char-quan-oracle.png` - 犬
- `char-jing-oracle.png` - 巠 (CRITICAL character)

**Bronze inscriptions:**
- `char-ren-bronze.png` - 人
- `char-fu-bronze.png` - 父
- `char-jin-bronze.png` - 金

**Seal scripts:**
- `char-ren-seal.png` - 人
- `char-ge-seal.png` - 戈
- `char-li-vessel-seal.png` - 鬲 (CRITICAL character)

**Homonym handling:**
- `char-mu-oracle.png` - 母 (mother)
- `char-mu-wood-oracle.png` - 木 (wood)
- `char-yi-crossed-oracle.png` - 乂 (crossed cuts)
- `char-yi-stem-oracle.png` - 乙 (heavenly stem)
- `char-yi-one-oracle.png` - 一 (number one)

## Progress Tracking Workflow

### Check Overall Status
```bash
cd /home/papagame/projects/Proj-ZiNets/zinets_radicals/docs/arxiv/figures/

# Count pending
grep 'status: "pending"' figures-config.yaml | wc -l

# Count collected
grep 'status: "collected"' figures-config.yaml | wc -l

# Count verified
grep 'status: "verified"' figures-config.yaml | wc -l
```

### Update Status
Edit `figures-config.yaml`:
```yaml
- hanzi: "人"
  pinyin: "ren"
  status: "pending"      # ← Change to "collected" after download
  files:
    oracle: "char-ren-oracle.png"
    bronze: "char-ren-bronze.png"
    seal: "char-ren-seal.png"
```

After verification:
```yaml
  status: "verified"     # ← Final status
```

## Next Steps

### Immediate (High Priority)

1. **Collect critical character images** (start with these):
   - 巠 (jing) - Spoke wheel radical (95%+ coherence, Section 2.7)
   - 鬲 (li) - Dialectical vessel (Section 2.13)
   - 艮 (gen) - Visibility radical (90%+ coherence, Section 2.13)
   - 器 (qi) - Pit trap system (Section 2.3)
   - 江 (jiang) - River = water's work (Section 2.7/2.12)
   - 冶 (ye) - Smelting thermodynamics (Section 2.8)

2. **Create conceptual diagrams** (high priority):
   - fig-2.7-spoke-wheel.pdf - Radial engineering diagram
   - fig-2.13-ge-dialectic.pdf - Fusion/separation process
   - fig-2.12-phase-cycle.pdf - Water phase transitions

### Medium Priority

3. **Collect remaining character images** systematically by section:
   - Complete Section 2.1 (人女母娘好)
   - Complete Section 2.2 (金木水火土日月星)
   - Continue through 2.3-2.13

4. **Create Python generation script**:
   - `generate_figures.py` - Reads YAML, generates LaTeX/Markdown tables
   - Automates table creation from metadata

### Lower Priority

5. **Create supplementary diagrams**:
   - Sexagenary cycle grid
   - Pit trap system
   - Network diagrams
   - Timeline

## Estimated Workload

### Character Image Collection
- **~70 characters × 4 scripts** = ~280 images maximum
- **Actual:** ~180-220 images (many missing oracle/bronze for later characters)
- **Source:** Richard Sears' database (https://hanziyuan.net/)
- **Time estimate:** 2-4 hours if batch downloading systematically

### Conceptual Diagrams
- **High priority:** 3 diagrams (~2-3 hours each = 6-9 hours)
- **Medium priority:** 2 diagrams (~1-2 hours each = 2-4 hours)
- **Low priority:** 2 diagrams (~1 hour each = 2 hours)
- **Total:** 10-15 hours for custom diagrams

### Script Development
- **generate_figures.py:** 2-3 hours for full LaTeX/Markdown generation
- **Testing/refinement:** 1-2 hours
- **Total:** 3-5 hours

### Overall Estimate
- **Image collection:** 2-4 hours
- **Conceptual diagrams:** 10-15 hours
- **Script development:** 3-5 hours
- **Integration/review:** 2-3 hours
- **TOTAL:** ~17-27 hours for complete figure preparation

## Quality Standards

### Character Images
- ✓ Source from Richard Sears' database (authoritative)
- ✓ 300 DPI minimum resolution
- ✓ Transparent or white background (consistent)
- ✓ Tight cropping around character
- ✓ Verify against multiple sources if uncertain

### Conceptual Diagrams
- ✓ Professional vector graphics (PDF/SVG preferred)
- ✓ Clear labels and annotations
- ✓ Consistent styling across diagrams
- ✓ High-resolution for print (300+ DPI)
- ✓ Color-blind friendly (if using colors)

### Captions
- ✓ Concise but complete descriptions
- ✓ Section references clear
- ✓ Attribution to Richard Sears included
- ✓ Key insights highlighted

## Attribution Template

Include in all figure captions:

> "Oracle bone and bronze inscription forms from Richard Sears' Chinese Etymology database (https://hanziyuan.net/). Seal script and modern forms from standard references."

## Critical Characters Requiring Special Attention

These characters have the highest analytical importance in the paper:

1. **巠 (jīng)** - Spoke wheel radial structure
   - 95%+ network coherence
   - Revolutionary engineering insight
   - Requires detailed spoke wheel diagram

2. **鬲 (lì)** - Dialectical fusion/separation
   - Philosophical significance (dialectics before Hegel)
   - Requires conceptual diagram showing simultaneous opposites

3. **艮 (gěn)** - Visibility/sight boundary
   - 90%+ network coherence
   - Corrects 1,900-year Shuowen error
   - May benefit from network diagram

4. **器 (qì)** - Coordinated pit trap system
   - Neolithic hunting technology
   - Multi-犬 composition critical
   - Requires overhead/cross-section diagrams

5. **江 (jiāng)** - Water's work (erosion)
   - Proto-Newtonian mechanics (氵+ 工)
   - Could use erosion process illustration

6. **冶 (yě)** - Smelting thermodynamics
   - 冫+ 台 composition shows cooling control
   - Metallurgical process diagram recommended

## Files Created

1. ✓ `/figures/README.md` - Complete documentation (322 lines)
2. ✓ `/figures/figures-config.yaml` - Master configuration (726 lines)
3. ✓ `/figures/SETUP-COMPLETE.md` - This summary
4. ✓ `/figures/characters/{oracle,bronze,seal,modern}/` - Image directories
5. ✓ `/figures/generated/` - Output directory

## Ready to Proceed

The infrastructure is complete and ready for:
- Image collection workflow
- Script development
- Figure generation
- Paper integration

All design decisions reflect your requirements:
- Character-centric naming ✓
- YAML with comments ✓
- Integrated progress tracking ✓
- Uniform grid layout ✓
- "(unavailable)" placeholders ✓

**You can now begin collecting character images and tracking progress in `figures-config.yaml`.**

Good luck with figure preparation! This systematic approach will ensure consistency and save significant time through automation. 🎨📊
