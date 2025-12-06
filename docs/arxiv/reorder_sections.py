#!/usr/bin/env python3
"""
Section Reordering Script for Chinese Characters Living Fossils Paper

Purpose: Reorder sections from v0.7 to v0.8 based on improved chronological organization
Author: AI Assistant (Claude) based on user requirements
Date: December 6, 2025

Usage:
    python reorder-sections.py

Input:  paper-2nd-living-fossil-v0.7.md
Output: paper-2nd-living-fossil-v0.8.md

Strategy:
1. Use temporary placeholder "2xyz" to avoid replacement conflicts
2. Replace sections with whole-word matching (equivalent to VS Code case-sensitive + whole-word)
3. Final replacement: "2xyz" → "2"

"""

import re
import os

def replace_sections(text, section_map):
    """
    Replace sections using regex with whole-word matching
    Equivalent to VS Code's case-sensitive + whole-word search
    
    Args:
        text (str): Input text content
        section_map (dict): Mapping from old section to temporary placeholder
    
    Returns:
        str: Updated text with reordered sections
    """
    
    print("Step 1: Replacing sections with temporary placeholders...")
    
    # Step 1: Replace with temporary placeholders using whole-word matching
    for old_section, temp_section in section_map.items():
        # Use word boundaries \b to match whole words only (VS Code equivalent)
        # Escape dots for literal matching
        pattern = r'\b' + re.escape(old_section) + r'\b'
        
        # Count matches before replacement for verification
        matches = len(re.findall(pattern, text))
        if matches > 0:
            print(f"  {old_section} → {temp_section} ({matches} matches)")
            text = re.sub(pattern, temp_section, text)
    
    print("\nStep 2: Replacing temporary placeholder '2xyz' with '2'...")
    
    # Step 2: Replace temporary placeholder back to "2"
    xyz_matches = text.count("2xyz")
    print(f"  Found {xyz_matches} instances of '2xyz' to replace")
    text = text.replace("2xyz", "2")
    
    return text

def main():
    """
    Main execution function

    Section Mapping (Old → New):
    - 2.3 → 2.4  (Trees & Wood)
    - 2.4 → 2.5  (Stone Age)  
    - 2.5 → 2.3  (Fire & Cooking)
    - 2.6 → 2.10 (Shelter & Architecture)
    - 2.7 → 2.8  (Textile & Clothing)
    - 2.8 → 2.7  (Hunting & Domestication)
    - 2.10 → 2.6 (Cutting & Inscribing)
    - 2.11 → 2.12 (Agricultural Development)
    - 2.12 → 2.17 (Power & Patriarchy)
    - 2.13 → 2.14 (Craftsmanship & Engineering)
    - 2.14 → 2.15 (Metallurgy Development)
    - 2.15 → 2.16 (Military Development)
    - 2.16 → 2.18 (Ritual & Religion)
    - 2.17 → 2.20 (Calendar & Time)
    - 2.18 → 2.19 (Measurement)
    - 2.19 → 2.13 (Water & Hydraulics)
    - 2.20 → 2.11 (Transportation)

    Note: 2.1, 2.2, 2.9, 2.21 remain unchanged
    
    """
    
    # Section mapping: current section → temporary placeholder
    section_map = {
        "2.3": "2xyz.4",    # Trees & Wood: 2.3 → 2.4
        "2.4": "2xyz.5",    # Stone Age: 2.4 → 2.5  
        "2.5": "2xyz.3",    # Fire & Cooking: 2.5 → 2.3
        "2.6": "2xyz.10",   # Shelter & Architecture: 2.6 → 2.10
        "2.7": "2xyz.8",    # Textile & Clothing: 2.7 → 2.8
        "2.8": "2xyz.7",    # Hunting & Domestication: 2.8 → 2.7
        "2.10": "2xyz.6",   # Cutting & Inscribing: 2.10 → 2.6
        "2.11": "2xyz.12",  # Agricultural Development: 2.11 → 2.12
        "2.12": "2xyz.17",  # Power & Patriarchy: 2.12 → 2.17
        "2.13": "2xyz.14",  # Craftsmanship & Engineering: 2.13 → 2.14
        "2.14": "2xyz.15",  # Metallurgy Development: 2.14 → 2.15
        "2.15": "2xyz.16",  # Military Development: 2.15 → 2.16
        "2.16": "2xyz.18",  # Ritual & Religion: 2.16 → 2.18
        "2.17": "2xyz.20",  # Calendar & Time: 2.17 → 2.20
        "2.18": "2xyz.19",  # Measurement: 2.18 → 2.19
        "2.19": "2xyz.13",  # Water & Hydraulics: 2.19 → 2.13
        "2.20": "2xyz.11",  # Transportation: 2.20 → 2.11
    }
    
    # File paths
    input_file = "paper-2nd-living-fossil-v0.7.md"
    output_file = "paper-2nd-living-fossil-v0.8.md"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir('.')}")
        return
    
    print(f"Reading input file: {input_file}")
    
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"File size: {len(content):,} characters")
        print(f"Total sections to reorder: {len(section_map)}")
        print()
        
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Apply section reordering
    try:
        updated_content = replace_sections(content, section_map)
        
        # Update version number in content
        updated_content = updated_content.replace("**Version:** v0.7", "**Version:** v0.8")
        updated_content = updated_content.replace("**Date:** December 5, 2025", "**Date:** December 6, 2025")
        
        print(f"\nStep 3: Writing output file: {output_file}")
        
        # Write output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Successfully created {output_file}")
        print(f"Output file size: {len(updated_content):,} characters")
        
        # Verification: Check that no temporary placeholders remain
        if "2xyz" in updated_content:
            print("⚠️  WARNING: Temporary placeholders '2xyz' still found in output!")
        else:
            print("✅ Verification: No temporary placeholders remaining")
            
    except Exception as e:
        print(f"Error processing file: {e}")
        return

if __name__ == "__main__":
    main()