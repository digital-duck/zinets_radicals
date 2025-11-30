#!/usr/bin/env python3
"""
Organize character images into subfolders by style

Moves character images from characters/ into style-specific subdirectories:
- char-*-oracle.png → characters/oracle/
- char-*-bronze.png → characters/bronze/
- char-*-seal.png → characters/seal/
- char-*-kaiti.png → characters/kaiti/

Usage:
    python3 organize_characters.py [--dry-run]

Author: Paper #2 - Chinese Characters as Living Fossils
Date: 2025-01-30
"""

import shutil
from pathlib import Path

import click


@click.command()
@click.option(
    '--source',
    default='characters',
    type=click.Path(exists=True, path_type=Path),
    help='Source directory containing character images (default: characters/)'
)
@click.option(
    '--dry-run',
    is_flag=True,
    help='Show what would be moved without actually moving files'
)
def main(source, dry_run):
    """Organize character images into style-specific subdirectories"""

    # Define style categories and their subdirectories
    styles = ['oracle', 'bronze', 'seal', 'kaiti']

    print(f"Organizing character images in: {source}")
    print("=" * 60)

    if dry_run:
        print("🔍 DRY RUN MODE - No files will be moved\n")

    # Create subdirectories if they don't exist
    for style in styles:
        style_dir = source / style
        if not dry_run:
            style_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Ensuring directory exists: {style_dir}")

    print("\n" + "=" * 60)
    print("Moving files:")
    print("=" * 60 + "\n")

    # Statistics
    stats = {style: 0 for style in styles}
    total_moved = 0

    # Find and move files
    for style in styles:
        pattern = f"char-*-{style}.png"
        files = list(source.glob(pattern))

        if not files:
            print(f"⚠️  No files found matching: {pattern}")
            continue

        print(f"\n{style.upper()} ({len(files)} files):")
        print("-" * 40)

        for file_path in sorted(files):
            dest_dir = source / style
            dest_path = dest_dir / file_path.name

            # Skip if already in correct location
            if file_path.parent == dest_dir:
                print(f"  ✓ Already in place: {file_path.name}")
                continue

            if dry_run:
                print(f"  Would move: {file_path.name} → {style}/")
            else:
                try:
                    shutil.move(str(file_path), str(dest_path))
                    print(f"  ✓ Moved: {file_path.name} → {style}/")
                    stats[style] += 1
                    total_moved += 1
                except Exception as e:
                    print(f"  ✗ Error moving {file_path.name}: {e}")

    # Print summary
    print("\n" + "=" * 60)
    print("ORGANIZATION SUMMARY")
    print("=" * 60)

    for style in styles:
        count = stats[style]
        emoji = "✓" if count > 0 else "-"
        print(f"{emoji} {style.capitalize():8} : {count:3} files moved")

    print("-" * 60)
    print(f"Total files moved: {total_moved}")
    print("=" * 60)

    if dry_run:
        print("\n💡 Run without --dry-run to actually move files")
    else:
        print("\n✓ All character images organized successfully!")


if __name__ == '__main__':
    main()
