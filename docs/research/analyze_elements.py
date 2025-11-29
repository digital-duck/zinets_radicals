#!/usr/bin/env python3
"""
Analyze elemental characters spreadsheet for Zinets Semantic Radicals Project
"""

import pandas as pd

# Read the Excel file
df = pd.read_excel('t_ele_zi-20251127-v2.xlsx')

# Select columns of interest
columns_of_interest = ['zi', 'n_frequency', 'is_zi', 'id_kangxi', 'selected',
                       'category', 'sub_category', 'meaning']

# Filter to selected columns
df_filtered = df[columns_of_interest]

# Get selected characters only
selected = df_filtered[df_filtered['selected'] == 'Y']

print("=" * 80)
print("ZINETS SEMANTIC RADICALS - SPREADSHEET ANALYSIS")
print("=" * 80)
print()

# Basic statistics
print("📊 OVERVIEW:")
print(f"   Total characters in spreadsheet: {len(df_filtered)}")
print(f"   Selected for semantic radicals: {len(selected)}")
print(f"   Selection rate: {len(selected)/len(df_filtered)*100:.1f}%")
print()

# Character type breakdown
print("🔤 CHARACTER TYPES (Selected):")
standalone = len(selected[selected['is_zi'] == 1])
component = len(selected[selected['is_zi'] == 0])
print(f"   Standalone (is_zi=1): {standalone} ({standalone/len(selected)*100:.1f}%)")
print(f"   Component only (is_zi=0): {component} ({component/len(selected)*100:.1f}%)")
print()

# Kangxi radical coverage
print("📚 KANGXI RADICAL COVERAGE:")
has_kangxi = len(selected[selected['id_kangxi'] >= 0])
no_kangxi = len(selected[selected['id_kangxi'] == -1])
print(f"   Has Kangxi ID (id_kangxi >= 0): {has_kangxi} ({has_kangxi/len(selected)*100:.1f}%)")
print(f"   Non-Kangxi elements (id_kangxi = -1): {no_kangxi} ({no_kangxi/len(selected)*100:.1f}%)")
print()

# Frequency distribution
print("📈 FREQUENCY DISTRIBUTION (Selected):")
high = len(selected[selected['n_frequency'] > 100])
medium = len(selected[(selected['n_frequency'] >= 20) & (selected['n_frequency'] <= 100)])
low = len(selected[selected['n_frequency'] < 20])
print(f"   High (>100): {high} ({high/len(selected)*100:.1f}%)")
print(f"   Medium (20-100): {medium} ({medium/len(selected)*100:.1f}%)")
print(f"   Low (<20): {low} ({low/len(selected)*100:.1f}%)")
print()

# Category breakdown
print("🏷️  CATEGORIES (Selected, top 15):")
cat_counts = selected['category'].value_counts().head(15)
for cat, count in cat_counts.items():
    if pd.notna(cat):
        pct = count/len(selected)*100
        print(f"   {cat:20s}: {count:3d} ({pct:5.1f}%)")
print()

# Sub-category breakdown for selected categories
print("🏷️  SUB-CATEGORIES (Selected, where available):")
subcats = selected[selected['sub_category'].notna()]['sub_category'].value_counts().head(15)
for subcat, count in subcats.items():
    pct = count/len(selected)*100
    print(f"   {subcat:20s}: {count:3d} ({pct:5.1f}%)")
print()

# Characters we've analyzed
print("=" * 80)
print("🔬 OUR ANALYZED CHARACTERS:")
print("=" * 80)
analyzed_chars = {
    '乂': 'cutting/crossed blades (85-90% coherence)',
    '氐': 'low/base/foundation (70-75% coherence)',
    '屰': 'contrary direction/reversal (100% coherence)',
    '艮': 'visibility/sight (90%+ coherence)',
    '鬲': 'infusion/fusion (95%+ coherence)',
    '乇': 'insufficient evidence (50% coherence - excluded)',
    '良': 'seed germination/growth'
}

for char, description in analyzed_chars.items():
    row = df_filtered[df_filtered['zi'] == char]
    if not row.empty:
        r = row.iloc[0]
        status = '✓ SELECTED' if r['selected'] == 'Y' else '✗ NOT SELECTED'
        print(f"\n{char} - {description}")
        print(f"   Status: {status}")
        print(f"   Frequency: {r['n_frequency']}, Kangxi: {r['id_kangxi']}, is_zi: {r['is_zi']}")
        print(f"   Category: {r['category']}, Sub: {r['sub_category']}")
        print(f"   Meaning: {r['meaning']}")
    else:
        print(f"\n{char} - {description}")
        print(f"   ⚠️  NOT FOUND in spreadsheet")

print()
print("=" * 80)
print("📋 SAMPLE SELECTED CHARACTERS (first 30):")
print("=" * 80)
sample = selected.head(30)[columns_of_interest]
print(sample.to_string(index=False))

print()
print("=" * 80)
print("💾 EXPORT OPTIONS:")
print("=" * 80)
print("To export selected characters to CSV:")
print("   selected.to_csv('selected_elements.csv', index=False)")
print()
print("To export all data to CSV:")
print("   df_filtered.to_csv('all_elements.csv', index=False)")

# Optionally save to CSV
# selected.to_csv('selected_semantic_radicals.csv', index=False, encoding='utf-8-sig')
# print("\n✓ Saved selected characters to 'selected_semantic_radicals.csv'")
