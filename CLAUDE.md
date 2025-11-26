# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Zinets (字网)** is an academic research project that challenges the 300-year-old Kangxi radical system by identifying true semantic primitives in Chinese characters through oracle bone inscription analysis and material culture reconstruction. This is NOT a software development project - it's a scholarly research initiative focused on Chinese etymology and linguistics.

## Project Type & Structure

This repository contains **academic research documentation** rather than executable code:

- **Main documentation**: `README.md` (comprehensive project overview)
- **Draft paper**: `docs/arxiv/semantic-radicals-v0.1.md` (complete theoretical framework with 7 case studies)
- **Research status**: Currently in Phase 2 (expanding from 7 to 20-50 analyzed elements)

## Development Commands

Since this is a research documentation project, there are **no build, test, or run commands**. Common tasks involve:

### Documentation Work
```bash
# Edit main research files
vim README.md
vim docs/arxiv/semantic-radicals-v0.1.md

# View project structure
tree
ls -la
```

### Git Operations
```bash
# Standard git workflow for research updates
git status
git add .
git commit -m "Update case study analysis"
git push origin main
```

### Potential Future Development

The `.gitignore` suggests potential future Python development for:
- Computational semantic analysis tools
- Character database management
- Oracle bone inscription analysis
- Semantic network visualization

However, **no such tools currently exist** in this repository.

## Research Methodology & Architecture

### Core Research Framework

1. **Oracle bone inscription analysis** (primary evidence from ~1200 BCE)
2. **Material culture reconstruction** (understanding Neolithic survival practices)
3. **Semantic network mapping** (testing meanings across ALL characters containing each element)
4. **Archaeological corroboration** (cross-referencing with physical evidence)

### Current Findings (7 Completed Case Studies)

| Element | Traditional Interpretation | Reinterpreted As | Key Insight |
|---------|---------------------------|------------------|-------------|
| 犬 (quǎn) | dog | trapped prey in hunting context | Explains 器 (trap system), 哭 (wailing of trapped animals) |
| 乍 (zhà) | sudden | mechanical working/tool operation | Explains 作 (work), 榨 (press), 炸 (explosive work) |
| 禺 (yú) | corner | joining/connection | Explains 偶 (couple), 遇 (meet), 愚 (mental entanglement) |
| 巠 (jīng) | [missing from Kangxi] | radial fiber structure | Explains 輕 (spoke wheel), 經 (warp threads) |
| 亢 (kàng) | throat/high | raised structure to resist | Explains 抗 (resist), 坑 (supported pit), 航 (boat staying afloat) |
| 甫 (fǔ) | beginning/male | agricultural nursery system | Explains 圃 (garden plot), 哺 (nurture), 補 (supplement) |
| 呙 (guō) | crooked | spiral/nested opening structure | Explains 蝸 (snail shell), 渦 (whirlpool), 鍋 (deep pot) |

### Research Goals

- **Phase 1** ✅: Establish methodology with 7 case studies
- **Phase 2** 🔄: Expand to 20-50 elements for publication
- **Phase 3** 🔮: Complete ~400 elemental character system

## Working with This Repository

### For Research Tasks

When working on this project, focus on:

1. **Case study expansion**: Identify new candidate elements using the established criteria
2. **Evidence gathering**: Oracle bone inscription research and archaeological validation
3. **Semantic network analysis**: Testing proposed meanings across character families
4. **Documentation**: Maintaining consistency with established format and rigor

### Key Research Files to Reference

- `README.md:40-47` - Summary table of 7 completed case studies
- `docs/arxiv/semantic-radicals-v0.1.md:42-315` - Detailed case study evidence and analysis
- `docs/arxiv/semantic-radicals-v0.1.md:428-451` - Criteria for identifying true semantic primitives

### Research Criteria for New Elements

All candidate elements must meet:

1. **Irreducibility**: Cannot be meaningfully decomposed further
2. **Productivity**: Appears in multiple character families
3. **Material culture grounding**: Traces to concrete Neolithic practice
4. **Semantic network coherence**: Works systematically across ALL instances
5. **Cultural salience**: Important enough to encode permanently

### Publication Target

Preparing academic paper: *"Semantic Radicals Reconsidered: Recovering Lost Primitives Through Material Culture Analysis"* for journals like:
- Journal of Chinese Linguistics
- Language (theoretical framing)
- Antiquity (archaeological angle)

## Important Notes for Claude Code

- This is **academic research**, not software development
- **No code execution** or build processes are involved
- **Content accuracy** and scholarly rigor are paramount
- **Evidence-based analysis** is required for all claims
- **Material culture context** must ground all interpretations
- **Semantic network validation** is essential for all proposed meanings

When contributing to this research, maintain the established academic standards and ensure all new analysis follows the proven methodology demonstrated in the existing case studies.