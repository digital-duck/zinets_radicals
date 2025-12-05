# Section Refactoring Plan for v0.7

## TEMPLATE FORMAT (Established & Approved)
Each section must follow this exact structure:
```
### 2.X SECTION TITLE

#### 2.X.1 Character Forms
**Table 2.X.1** Oracle bone and bronze evidence for [topic]
[Table with Oracle/Bronze/Seal/Modern columns + character descriptions]

#### 2.X.2 Semantic Networks  
**Table 2.X.2** Semantic networks for [topic] radicals
[Network analysis table showing coherence patterns]

#### 2.X.3 Validation
**Table 2.X.3** Validation summary for Section 2.X
[Oracle evidence + Network coherence + Archaeological correlation + Modern usage]

#### 2.X.4 Commentary

##### 2.X.4.1 **Material Culture Context:** 
[Consolidated background material]

##### 2.X.4.2 **Key Insights**

##### 2.X.4.3 **Section Synthesis:** 
[Main conclusions]

##### 2.X.4.4 **Cross-references:** 
[optional if any]

add other special section specific contents as notes below

```

## PROGRESS STATUS (as of December 5, 2025)

✅ **COMPLETED:**
- Section 2.1 EARLY HUMAN SOCIETY (approved by user)
- Section 2.2 NATURE OBSERVATION  
- Section 2.3 TREES & WOOD (just completed)

🔄 **IN PROGRESS:**
- Section 2.4 STONE AGE - Primitive Civilization (needs restructuring)

⏳ **REMAINING (17 sections):**
- Section 2.5 FIRE & COOKING - Food Preparation (食)
- Section 2.6 SHELTER & ARCHITECTURE - Dwelling (住) 
- Section 2.7 TEXTILE & CLOTHING - Garments (衣)
- Section 2.8 HUNTING & DOMESTICATION - Animal Relationships
- Section 2.9 POTTERY & CERAMICS - Food Storage and Cooking Vessels (食)
- Section 2.10 CUTTING & INSCRIBING - Tool Inventions
- Section 2.11 AGRICULTURAL DEVELOPMENT - Settled Civilization
- Section 2.12 POWER SHIFT - Patriarchy Emergence
- Section 2.13 CRAFTSMANSHIP - Engineering
- Section 2.14 METALLURGY DEVELOPMENT - Bronze Revolution
- Section 2.15 MILITARY DEVELOPMENT - Organized conflict
- Section 2.16 RITUAL & RELIGION - Oracle Bone Divination Context
- Section 2.17 COUNTING & CALENDAR - Symbolic systems
- Section 2.18 MEASUREMENT - Standardization Systems
- Section 2.19 FLOW & HYDRAULICS - Physics Understanding
- Section 2.20 TRANSPORTATION - Mobility Systems (行)
- Section 2.21 ADVANCED CONCEPTS - Philosophical Abstraction

## TABLE NUMBERING SYSTEM (CRITICAL)

| Section | Character Forms | Semantic Networks | Validation |
|---------|-----------------|-------------------|------------|
| 2.1 | Table 2.1 | Table 2.2 | Table 2.3 |
| 2.2 | Table 2.4 | Table 2.5 | Table 2.6 |
| 2.3 | Table 2.7 | Table 2.8 | Table 2.9 |
| 2.4 | Table 2.10 | Table 2.11 | Table 2.12 |
| 2.5 | Table 2.13 | Table 2.14 | Table 2.15 |
| 2.6 | Table 2.16 | Table 2.17 | Table 2.18 |
| 2.7 | Table 2.19 | Table 2.20 | Table 2.21 |
| 2.8 | Table 2.22 | Table 2.23 | Table 2.24 |
| 2.9 | Table 2.25 | Table 2.26 | Table 2.27 |
| 2.10 | Table 2.28 | Table 2.29 | Table 2.30 |
| 2.11 | Table 2.31 | Table 2.32 | Table 2.33 |
| 2.12 | Table 2.34 | Table 2.35 | Table 2.36 |
| 2.13 | Table 2.37 | Table 2.38 | Table 2.39 |
| 2.14 | Table 2.40 | Table 2.41 | Table 2.42 |
| 2.15 | Table 2.43 | Table 2.44 | Table 2.45 |
| 2.16 | Table 2.46 | Table 2.47 | Table 2.48 |
| 2.17 | Table 2.49 | Table 2.50 | Table 2.51 |
| 2.18 | Table 2.52 | Table 2.53 | Table 2.54 |
| 2.19 | Table 2.55 | Table 2.56 | Table 2.57 |
| 2.20 | Table 2.58 | Table 2.59 | Table 2.60 |
| 2.21 | Table 2.61 | Table 2.62 | Table 2.63 |

## REFACTORING BATCHES (for efficiency)

**Batch 1:** Sections 2.4-2.6 (Stone Age, Fire/Cooking, Shelter)
**Batch 2:** Sections 2.7-2.10 (Textile, Hunting, Pottery, Cutting) 
**Batch 3:** Sections 2.11-2.15 (Agriculture, Power, Crafts, Metallurgy, Military)
**Batch 4:** Sections 2.16-2.21 (Ritual, Calendar, Measurement, Flow, Transport, Advanced)

## CURRENT SEARCH PATTERNS FOR FINDING SECTIONS

```bash
# Find section headers
grep "^### 2\.[0-9]" file.md

# Find subsection structure  
grep "^#### ([0-9])" file.md

# Find table references that need updating
grep "Table 2\." file.md

# Find validation sections
grep "Validation.*Section 2\." file.md
```

## KEY REFACTORING ACTIONS FOR EACH SECTION

1. **Replace Background section** with Character Forms (oracle/bronze evidence first)
2. **Keep Semantic Networks section** but update table number
3. **Remove Oracle/Bronze/Seal Forms section** (redundant, move to Character Forms)
4. **Streamline Validation section** with consistent table format
5. **Add Commentary section** consolidating Background content + insights
6. **Update all table references** following numbering system
7. **Maintain content quality** while eliminating redundancy

## SECTIONS WITH SPECIAL CONSIDERATIONS

- **Section 2.9 (Pottery)** - Has extensive material culture analysis
- **Section 2.12 (Power Shift)** - Complex social analysis 
- **Section 2.16 (Ritual)** - Meta-textual oracle bone discussion
- **Section 2.21 (Advanced)** - Philosophical abstractions

## QUALITY CHECKS AFTER EACH SECTION

- [ ] Table numbers sequential and correct
- [ ] All four subsections present: (a), (b), (c), (d)
- [ ] Character Forms leads with oracle evidence
- [ ] Commentary consolidates background material
- [ ] No redundancy between old Background and new Commentary
- [ ] Consistent formatting and style

## COMPLETION TARGET

All 21 sections (2.1-2.21) restructured with new format by end of current session.

## RESUME INSTRUCTIONS FOR NEXT SESSION

1. Check REFACTORING-PLAN.md for current progress
2. Run: `grep "#### (a) Character Forms" v0.7.md | wc -l` to count completed sections
3. Continue from first incomplete section using template format
4. Update table numbers according to numbering system
5. Follow batch approach for efficiency