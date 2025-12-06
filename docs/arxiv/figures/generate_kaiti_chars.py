#!/usr/bin/env python3
"""
Generate Kaiti-style modern character images using Makemeahanzi data

This script reads figures-config.yaml and generates PNG images for all
characters using Makemeahanzi SVG stroke data (with Noto font fallback).

Usage:
    python3 generate_kaiti_chars.py [--makemeahanzi PATH] [--size SIZE]

Author: Paper #2 - Chinese Characters as Living Fossils
Date: 2025-01-30
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

import click
import yaml

# Check for required dependencies
try:
    import cairosvg
    from PIL import Image
    from io import BytesIO
    HAS_CAIRO = True
except ImportError:
    HAS_CAIRO = False
    print("Warning: cairosvg not installed. Install with: pip install cairosvg")

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("Error: Pillow not installed. Install with: pip install pillow")
    sys.exit(1)


class KaitiGenerator:
    """Generate Kaiti character images from Makemeahanzi data"""

    def __init__(self, makemeahanzi_path: Optional[str] = None,
                 size: int = 300, font_path: Optional[str] = None):
        """
        Initialize generator

        Args:
            makemeahanzi_path: Path to graphics.txt file (or auto-detect)
            size: Output image size in pixels (default 300x300)
            font_path: Path to Noto Serif CJK font for fallback
        """
        self.size = size
        self.font_path = font_path
        self.char_data = {}

        # Auto-detect or use provided Makemeahanzi path
        if makemeahanzi_path:
            self.makemeahanzi_path = Path(makemeahanzi_path)
        else:
            self.makemeahanzi_path = self._find_makemeahanzi()

        if self.makemeahanzi_path and self.makemeahanzi_path.exists():
            self._load_makemeahanzi_data()
        else:
            print(f"Warning: Makemeahanzi data not found at {self.makemeahanzi_path}")
            print("Will use font fallback for all characters")

    def _find_makemeahanzi(self) -> Optional[Path]:
        """Auto-detect Makemeahanzi graphics.txt location"""
        possible_paths = [
            Path.home() / "projects/Proj-ZiNets/makemeahanzi/graphics.txt",
            Path.home() / "projects/digital-duck/makemeahanzi/graphics.txt",
            Path.home() / "makemeahanzi" / "graphics.txt",
            Path("/usr/local/share/makemeahanzi/graphics.txt"),
            Path("makemeahanzi/graphics.txt"),
            Path("../makemeahanzi/graphics.txt"),
            Path("../../makemeahanzi/graphics.txt"),
        ]

        for path in possible_paths:
            if path.exists():
                print(f"Found Makemeahanzi data: {path}")
                return path

        return None

    def _load_makemeahanzi_data(self):
        """Load Makemeahanzi character data from graphics.txt"""
        print(f"Loading Makemeahanzi data from: {self.makemeahanzi_path}")

        count = 0
        with open(self.makemeahanzi_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        data = json.loads(line)
                        char = data.get('character')
                        if char:
                            self.char_data[char] = data
                            count += 1
                    except json.JSONDecodeError:
                        continue

        print(f"Loaded {count} character definitions from Makemeahanzi")

    def _render_svg_to_png(self, svg_content: str) -> Image.Image:
        """Render SVG content to PIL Image"""
        if not HAS_CAIRO:
            raise ImportError("cairosvg required for SVG rendering. Install with: pip install cairosvg")

        # Render SVG to PNG bytes
        png_bytes = cairosvg.svg2png(
            bytestring=svg_content.encode('utf-8'),
            output_width=self.size,
            output_height=self.size
        )

        # Convert to PIL Image
        img = Image.open(BytesIO(png_bytes))

        # Ensure RGB mode with white background
        if img.mode != 'RGB':
            background = Image.new('RGB', img.size, 'white')
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            else:
                background.paste(img)
            img = background

        return img

    def _create_svg_from_strokes(self, strokes: List[str]) -> str:
        """Create SVG content from Makemeahanzi stroke paths"""
        stroke_paths = []
        for i, stroke in enumerate(strokes):
            # Each stroke is an SVG path
            stroke_paths.append(f'<path d="{stroke}" fill="black" />')

        # Create SVG with proper viewBox and transformation
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
  <g transform="scale(1, -1) translate(0, -900)">
    {''.join(stroke_paths)}
  </g>
</svg>'''

        return svg_content

    def _generate_with_font(self, hanzi: str, output_path: Path) -> bool:
        """Fallback: Generate image using Noto Serif CJK font"""

        # Try to find Noto Serif CJK font
        if not self.font_path:
            possible_fonts = [
                str(Path.home() / "projects/Proj-ZiNets/noto-cjk-font/NotoSerifTC-VariableFont_wght.ttf"),
                "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
                "/System/Library/Fonts/Supplemental/Songti.ttc",  # macOS
                "NotoSerifCJKsc-Regular.otf",  # Local download
                "NotoSerifCJKtc-Regular.otf",
            ]

            for font_candidate in possible_fonts:
                if Path(font_candidate).exists():
                    self.font_path = font_candidate
                    break

        if not self.font_path or not Path(self.font_path).exists():
            print(f"  ⚠️  No font available for fallback: {hanzi}")
            return False

        try:
            # Load font (size adjusted for proper centering)
            font_size = int(self.size * 0.7)
            font = ImageFont.truetype(self.font_path, font_size)

            # Create white background image
            img = Image.new('RGB', (self.size, self.size), 'white')
            draw = ImageDraw.Draw(img)

            # Get text bounding box for centering
            bbox = draw.textbbox((0, 0), hanzi, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Calculate centered position
            x = (self.size - text_width) / 2 - bbox[0]
            y = (self.size - text_height) / 2 - bbox[1]

            # Draw character
            draw.text((x, y), hanzi, font=font, fill='black')

            # Save
            img.save(output_path)
            print(f"  ✓ Generated (font): {output_path.name}")
            return True

        except Exception as e:
            print(f"  ✗ Font fallback failed for {hanzi}: {e}")
            return False

    def generate_character(self, hanzi: str, output_path: Path) -> bool:
        """
        Generate kaiti image for a single character

        Args:
            hanzi: Chinese character to generate
            output_path: Where to save PNG file

        Returns:
            True if successful, False otherwise
        """
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Try Makemeahanzi first
        if hanzi in self.char_data:
            try:
                data = self.char_data[hanzi]
                strokes = data.get('strokes', [])

                if not strokes:
                    print(f"  ⚠️  No strokes for {hanzi}, using font fallback")
                    return self._generate_with_font(hanzi, output_path)

                # Create SVG from strokes
                svg_content = self._create_svg_from_strokes(strokes)

                # Render to PNG
                img = self._render_svg_to_png(svg_content)

                # Save
                img.save(output_path)
                print(f"  ✓ Generated: {output_path.name}")
                return True

            except Exception as e:
                print(f"  ⚠️  Makemeahanzi failed for {hanzi}: {e}")
                print(f"     Trying font fallback...")
                return self._generate_with_font(hanzi, output_path)
        else:
            # Character not in Makemeahanzi, use font fallback
            print(f"  ⚠️  {hanzi} not in Makemeahanzi data, using font fallback")
            return self._generate_with_font(hanzi, output_path)

    def generate_from_config(self, config_path: Path, output_dir: Path) -> Dict:
        """
        Generate kaiti images for all characters in figures-config.yaml

        Args:
            config_path: Path to figures-config.yaml
            output_dir: Base directory for output (will create kaiti/ subdir)

        Returns:
            Dictionary with generation statistics
        """
        # Load config
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        # Collect all unique characters
        characters = set()
        for section_key in config.keys():
            if section_key.startswith('section_'):
                section = config[section_key]
                for char_data in section.get('characters', []):
                    hanzi = char_data.get('hanzi')
                    if hanzi:
                        characters.add(hanzi)

        characters = sorted(characters)  # Sort for consistent ordering

        print(f"\nProcessing {len(characters)} unique characters from {config_path.name}:")
        print("=" * 60)

        # Generate images
        output_kaiti = output_dir / 'kaiti'
        output_kaiti.mkdir(parents=True, exist_ok=True)

        stats = {
            'total': len(characters),
            'success': 0,
            'failed': 0,
            'missing_from_data': 0,
            'used_fallback': 0,
        }

        for hanzi in characters:
            output_path = output_kaiti / f"char-{hanzi}-kaiti.png"

            if hanzi not in self.char_data:
                stats['missing_from_data'] += 1

            success = self.generate_character(hanzi, output_path)

            if success:
                stats['success'] += 1
                # Check if we used fallback
                if hanzi not in self.char_data:
                    stats['used_fallback'] += 1
            else:
                stats['failed'] += 1

        return stats


@click.command()
@click.option(
    '--config',
    default='figures-config.yaml',
    type=click.Path(exists=True, path_type=Path),
    help='Path to figures-config.yaml (default: figures-config.yaml)'
)
@click.option(
    '--makemeahanzi',
    type=click.Path(path_type=Path),
    help='Path to Makemeahanzi graphics.txt file (auto-detect if not specified)'
)
@click.option(
    '--font',
    type=click.Path(path_type=Path),
    help='Path to Noto Serif CJK font for fallback (auto-detect if not specified)'
)
@click.option(
    '--size',
    default=300,
    type=int,
    help='Output image size in pixels (default: 300)'
)
@click.option(
    '--output',
    default='characters',
    type=click.Path(path_type=Path),
    help='Output base directory (default: characters/)'
)
def main(config, makemeahanzi, font, size, output):
    """Generate Kaiti character images from figures-config.yaml"""

    # Create generator
    print("Initializing Kaiti character generator...")
    generator = KaitiGenerator(
        makemeahanzi_path=str(makemeahanzi) if makemeahanzi else None,
        size=size,
        font_path=str(font) if font else None
    )

    # Generate all characters
    stats = generator.generate_from_config(config, output)

    # Print summary
    print("\n" + "=" * 60)
    print("GENERATION SUMMARY")
    print("=" * 60)
    print(f"Total characters:        {stats['total']}")
    print(f"Successfully generated:  {stats['success']}")
    print(f"Failed:                  {stats['failed']}")
    print(f"Missing from data:       {stats['missing_from_data']}")
    print(f"Used font fallback:      {stats['used_fallback']}")
    print("=" * 60)

    if stats['success'] == stats['total']:
        print("\n✓ All kaiti character images generated successfully!")
    elif stats['failed'] > 0:
        print(f"\n⚠️  {stats['failed']} characters failed to generate")
        print("Check error messages above for details")
        sys.exit(1)
    else:
        print(f"\n✓ Generated {stats['success']}/{stats['total']} characters")

    print(f"\nOutput saved to: {output / 'kaiti'}/")
    print("\nNext step: python3 generate_figures.py all")


if __name__ == '__main__':
    main()
