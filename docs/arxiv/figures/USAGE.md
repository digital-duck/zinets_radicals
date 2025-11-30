# Quick Usage Guide - generate_figures.py

## Script is Ready! ✅

The Python script `generate_figures.py` has been created and tested using **Click CLI**. It successfully:
- ✅ Reads `figures-config.yaml`
- ✅ Generates LaTeX tables for all 15 figures
- ✅ Generates Markdown tables for preview
- ✅ Handles missing images with "(unavailable)" placeholder
- ✅ Provides status reports on progress
- ✅ Clean Click-based command interface

## Installation

**Requires Click:**
```bash
pip install click
# or
pip install pyyaml click
```

## Command Reference

### Show Help
```bash
python3 generate_figures.py --help
```

### Show Status Report
```bash
python3 generate_figures.py status
```

**Output shows:**
- Total characters to process
- Progress (pending/collected/verified)
- Image completion percentage
- Missing oracle/bronze/seal forms

### Generate All Figures (LaTeX + Markdown)
```bash
python3 generate_figures.py all
```

### Generate LaTeX Only
```bash
python3 generate_figures.py latex
```

### Generate Markdown Only
```bash
python3 generate_figures.py markdown
```

### Use Custom Config File
```bash
python3 generate_figures.py --config /path/to/config.yaml status
python3 generate_figures.py --config /path/to/config.yaml all
```

## Current Status (Initial Run)

```
Total Characters: 76
Progress Status:
  Pending:    76 (100.0%)
  Collected:   0 (0.0%)
  Verified:    0 (0.0%)

Image Files Expected: 228 (oracle + bronze + seal)
Image Files Available: 216 (specified in YAML)
Completion: 94.7%

Missing Oracle Forms: 7 (娘, 爸, 銀, 钱, 銅, 烧, 晓)
Missing Bronze Forms: 5 (娘, 爸, 钱, 烧, 晓)
Missing Seal Forms: 0
```

**Note:** These are genuinely unavailable (later-developed characters without early forms).

## Generated Output

### Files Created
The script generated **30 files** in `generated/`:

**LaTeX files (15):**
- `fig-2.1-evolution.tex`
- `fig-2.2a-evolution.tex`
- `fig-2.2b-evolution.tex`
- ... (through fig-2.13)

**Markdown files (15):**
- `fig-2.1-evolution.md`
- `fig-2.2a-evolution.md`
- `fig-2.2b-evolution.md`
- ... (through fig-2.13)

### Sample LaTeX Output

```latex
\begin{figure}[htbp]
\centering
\begin{tabular}{|c|c|c|c|l|}
\hline
\textbf{Oracle} & \textbf{Bronze} & \textbf{Seal} & \textbf{Modern} & \textbf{Character} \\
\hline
\includegraphics[width=1.2cm]{figures/characters/oracle/char-ren-oracle.png} &
\includegraphics[width=1.2cm]{figures/characters/bronze/char-ren-bronze.png} &
\includegraphics[width=1.2cm]{figures/characters/seal/char-ren-seal.png} &
{\Huge 人} &
人 (ren) - Person, human \\
\hline
...
\end{tabular}
\caption{Evolution of Early Human Society radicals...}
\label{fig-2.1}
\end{figure}
```

### Sample Markdown Output

```markdown
## fig-2.1

Evolution of Early Human Society radicals...

| Oracle | Bronze | Seal | Modern | Character |
|--------|--------|------|--------|-----------|
| ![oracle](characters/oracle/char-ren-oracle.png) | ![bronze](characters/bronze/char-ren-bronze.png) | ![seal](characters/seal/char-ren-seal.png) | 人 | 人 (ren) - Person, human |
| (unavailable) | (unavailable) | ![seal](characters/seal/char-niang-seal.png) | 娘 | 娘 (niang) - Mother, young woman |
```

## Workflow

### 1. Collect Images
Download character images from Richard Sears' database (https://hanziyuan.net/) and save to:
- `characters/oracle/char-{pinyin}-oracle.png`
- `characters/bronze/char-{pinyin}-bronze.png`
- `characters/seal/char-{pinyin}-seal.png`

### 2. Update Status
Edit `figures-config.yaml` and change status:
```yaml
- hanzi: "人"
  status: "collected"  # was "pending"
```

### 3. Regenerate Figures
```bash
python3 generate_figures.py all
```

### 4. Check Progress
```bash
python3 generate_figures.py status
```

### 5. Use in Paper
Include in LaTeX:
```latex
\input{figures/generated/fig-2.1-evolution.tex}
```

## Tips

**Batch downloading images:**
- Start with high-priority characters (巠, 鬲, 艮, 器, 江, 冶)
- Use browser automation or scripting to speed up downloads
- Verify image quality before marking "verified"

**Testing output:**
- Markdown files can be previewed in GitHub or any Markdown viewer
- LaTeX files need images in place to compile properly
- Use `--status` frequently to track progress

**Regenerating after changes:**
- Script is idempotent - safe to run multiple times
- Only regenerates if configuration changed
- Previous output files will be overwritten

## What's Next?

1. **Collect character images** (highest priority)
   - Download from hanziyuan.net
   - Save with proper naming convention
   - Update status in YAML

2. **Create conceptual diagrams** (custom work)
   - Spoke wheel (巠)
   - Dialectical process (鬲)
   - Phase cycle (ice⇄water⇄vapor)

3. **Integrate into paper**
   - Include generated LaTeX files
   - Compile paper to verify rendering
   - Adjust image sizes if needed

## Script Features

✅ **Automatic table generation** from YAML config
✅ **Missing image handling** with "(unavailable)" placeholder
✅ **Progress tracking** with status reports
✅ **Dual format output** (LaTeX + Markdown)
✅ **Reusable character library** (same images across sections)
✅ **Consistent formatting** (uniform grid layout)

The infrastructure is complete and ready to use!
