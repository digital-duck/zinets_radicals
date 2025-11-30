#!/usr/bin/env python3
"""
Generate LaTeX and Markdown figure tables from figures-config.yaml

This script reads the master configuration file and generates:
1. LaTeX tables for character evolution grids (for academic paper)
2. Markdown tables for preview/documentation

Usage:
    python generate_figures.py latex
    python generate_figures.py markdown
    python generate_figures.py all
    python generate_figures.py status

Author: Paper #2 - Chinese Characters as Living Fossils
"""

import yaml
import click
from pathlib import Path


class FigureGenerator:
    """Generate figure tables from YAML configuration"""

    def __init__(self, config_path="figures-config.yaml"):
        """Load configuration from YAML file"""
        self.config_path = Path(config_path)
        self.base_dir = self.config_path.parent

        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        self.settings = self.config.get('generation_settings', {})
        self.latex_settings = self.settings.get('latex_settings', {})
        self.markdown_settings = self.settings.get('markdown_settings', {})

    def generate_all_latex(self, output_dir="generated", dry_run=False, filter_chars=None):
        """Generate LaTeX tables for all sections"""
        output_path = self.base_dir / output_dir

        if not dry_run:
            output_path.mkdir(exist_ok=True)

        generated_files = []

        # Process each section
        for section_key in self.config.keys():
            if section_key.startswith('section_'):
                section = self.config[section_key]
                figures = section.get('figures', [])

                for fig in figures:
                    fig_id = fig['id']
                    chars = fig['characters']
                    caption = fig['caption']

                    # Get character objects
                    char_objects = [
                        c for c in section['characters']
                        if c['hanzi'] in chars
                    ]

                    # Apply character filter if provided
                    if filter_chars:
                        char_objects = [c for c in char_objects if c['hanzi'] in filter_chars]
                        if not char_objects:
                            continue  # Skip this figure if no matching characters

                    # Generate LaTeX
                    latex_content = self.generate_latex_table(
                        char_objects,
                        caption,
                        fig_id
                    )

                    filename = f"{fig_id}-evolution.tex"
                    filepath = output_path / filename

                    if dry_run:
                        print(f"Would generate: {filename}")
                        print(f"  Characters: {', '.join([c['hanzi'] for c in char_objects])}")
                        print(f"  Caption: {caption[:60]}...")
                    else:
                        # Write to file
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(latex_content)
                        print(f"✓ Generated: {filename}")

                    generated_files.append(filename)

        return generated_files

    def generate_all_markdown(self, output_dir="generated", dry_run=False, filter_chars=None):
        """Generate Markdown tables for all sections"""
        output_path = self.base_dir / output_dir

        if not dry_run:
            output_path.mkdir(exist_ok=True)

        generated_files = []

        # Process each section
        for section_key in self.config.keys():
            if section_key.startswith('section_'):
                section = self.config[section_key]
                figures = section.get('figures', [])

                for fig in figures:
                    fig_id = fig['id']
                    chars = fig['characters']
                    caption = fig['caption']

                    # Get character objects
                    char_objects = [
                        c for c in section['characters']
                        if c['hanzi'] in chars
                    ]

                    # Apply character filter if provided
                    if filter_chars:
                        char_objects = [c for c in char_objects if c['hanzi'] in filter_chars]
                        if not char_objects:
                            continue  # Skip this figure if no matching characters

                    # Generate Markdown
                    md_content = self.generate_markdown_table(
                        char_objects,
                        caption,
                        fig_id
                    )

                    filename = f"{fig_id}-evolution.md"
                    filepath = output_path / filename

                    if dry_run:
                        print(f"Would generate: {filename}")
                        print(f"  Characters: {', '.join([c['hanzi'] for c in char_objects])}")
                        print(f"  Caption: {caption[:60]}...")
                    else:
                        # Write to file
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(md_content)
                        print(f"✓ Generated: {filename}")

                    generated_files.append(filename)

        return generated_files

    def generate_latex_table(self, characters, caption, label):
        """Generate LaTeX table for character evolution"""

        col_width = self.latex_settings.get('column_width', '1.2cm')
        font_modern = self.latex_settings.get('font_modern', '\\Huge')

        # Start table
        latex = []
        latex.append("\\begin{figure}[htbp]")
        latex.append("\\centering")
        latex.append("\\begin{tabular}{|c|c|c|c|}")
        latex.append("\\hline")
        latex.append("\\textbf{Oracle} & \\textbf{Bronze} & \\textbf{Seal} & \\textbf{Kaiti} \\\\")
        latex.append("\\hline")

        # Add rows for each character
        for char in characters:
            row = self._latex_row(char, col_width, font_modern)
            latex.append(row)
            latex.append("\\hline")

        # End table
        latex.append("\\end{tabular}")
        latex.append(f"\\caption{{{caption}}}")
        latex.append(f"\\label{{{label}}}")
        latex.append("\\end{figure}")

        return '\n'.join(latex)

    def _latex_row(self, char, col_width, font_modern):
        """Generate single LaTeX table row for character"""

        hanzi = char['hanzi']
        pinyin = char['pinyin']
        meaning = char['meaning']
        files = char['files']

        # Get file paths
        oracle = files.get('oracle', '')
        bronze = files.get('bronze', '')
        seal = files.get('seal', '')
        kaiti = files.get('kaiti', '')

        # Character info
        char_info = f"{hanzi} ({pinyin}) - {meaning}"

        # Build cells
        cells = []

        # Oracle
        if oracle:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/oracle/{oracle}}}")
        else:
            cells.append("\\textit{{(unavail.)}}")

        # Bronze
        if bronze:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/bronze/{bronze}}}")
        else:
            cells.append("\\textit{{(unavail.)}}")

        # Seal
        if seal:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/seal/{seal}}}")
        else:
            cells.append("\\textit{{(unavail.)}}")

        # Kaiti
        if kaiti:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/kaiti/{kaiti}}}")
        else:
            cells.append("\\textit{{(unavail.)}}")

        return ' & '.join(cells) + ' \\\\'

    def generate_markdown_table(self, characters, caption, label):
        """Generate Markdown table for character evolution"""

        img_width = self.markdown_settings.get('image_width', '100')
        use_unicode = self.markdown_settings.get('use_unicode_modern', True)

        # Start table
        md = []
        md.append(f"## {label}")
        md.append("")
        md.append(caption)
        md.append("")
        md.append("| Oracle | Bronze | Seal | Kaiti |")
        md.append("|--------|--------|------|-------|")

        # Add rows
        for char in characters:
            row = self._markdown_row(char, img_width, use_unicode)
            md.append(row)

        return '\n'.join(md)

    def _markdown_row(self, char, img_width, use_unicode):
        """Generate single Markdown table row for character"""

        hanzi = char['hanzi']
        pinyin = char['pinyin']
        meaning = char['meaning']
        files = char['files']

        # Get file paths
        oracle = files.get('oracle', '')
        bronze = files.get('bronze', '')
        seal = files.get('seal', '')
        kaiti = files.get('kaiti', '')

        # Character info
        char_info = f"{hanzi} ({pinyin}) - {meaning}"

        # Build cells
        cells = []

        # Oracle
        if oracle:
            cells.append(f'<img src="figures/characters/oracle/{oracle}" width="{img_width}" alt="{hanzi} oracle">')
        else:
            cells.append("(unavail.)")

        # Bronze
        if bronze:
            cells.append(f'<img src="figures/characters/bronze/{bronze}" width="{img_width}" alt="{hanzi} bronze">')
        else:
            cells.append("(unavail.)")

        # Seal
        if seal:
            cells.append(f'<img src="figures/characters/seal/{seal}" width="{img_width}" alt="{hanzi} seal">')
        else:
            cells.append("(unavail.)")

        # Kaiti
        if kaiti:
            cells.append(f'<img src="figures/characters/kaiti/{kaiti}" width="{img_width}" alt="{hanzi} kaiti">')
        else:
            cells.append("(unavail.)")

        return '| ' + ' | '.join(cells) + ' |'

    def generate_status_report(self):
        """Generate progress status report"""

        total_chars = 0
        total_images = 0
        pending = 0
        collected = 0
        verified = 0

        missing_oracle = []
        missing_bronze = []
        missing_seal = []

        # Count status
        for section_key in self.config.keys():
            if section_key.startswith('section_'):
                section = self.config[section_key]
                characters = section.get('characters', [])

                for char in characters:
                    total_chars += 1
                    status = char.get('status', 'pending')

                    if status == 'pending':
                        pending += 1
                    elif status == 'collected':
                        collected += 1
                    elif status == 'verified':
                        verified += 1

                    # Count images
                    files = char['files']
                    if files.get('oracle'):
                        total_images += 1
                    else:
                        missing_oracle.append(char['hanzi'])

                    if files.get('bronze'):
                        total_images += 1
                    else:
                        missing_bronze.append(char['hanzi'])

                    if files.get('seal'):
                        total_images += 1
                    else:
                        missing_seal.append(char['hanzi'])

        # Print report
        print("\n" + "="*60)
        print("FIGURE PREPARATION STATUS REPORT")
        print("="*60)
        print(f"\nTotal Characters: {total_chars}")
        print(f"\nProgress Status:")
        print(f"  Pending:   {pending:3d} ({pending/total_chars*100:.1f}%)")
        print(f"  Collected: {collected:3d} ({collected/total_chars*100:.1f}%)")
        print(f"  Verified:  {verified:3d} ({verified/total_chars*100:.1f}%)")
        print(f"\nImage Files Expected: {total_chars * 3} (oracle + bronze + seal)")
        print(f"Image Files Available: {total_images}")
        print(f"Completion: {total_images/(total_chars*3)*100:.1f}%")

        print(f"\nMissing Oracle Forms: {len(missing_oracle)}")
        if len(missing_oracle) > 0 and len(missing_oracle) <= 10:
            print(f"  {', '.join(missing_oracle)}")

        print(f"\nMissing Bronze Forms: {len(missing_bronze)}")
        if len(missing_bronze) > 0 and len(missing_bronze) <= 10:
            print(f"  {', '.join(missing_bronze)}")

        print(f"\nMissing Seal Forms: {len(missing_seal)}")
        if len(missing_seal) > 0 and len(missing_seal) <= 10:
            print(f"  {', '.join(missing_seal)}")

        print("\n" + "="*60)


@click.command()
@click.option('--config', default='figures-config.yaml',
              help='Path to configuration file')
@click.option('--format', 'output_format',
              type=click.Choice(['latex', 'markdown', 'all'], case_sensitive=False),
              default='markdown',
              help='Output format: latex, markdown, or all (default: markdown)')
@click.option('--chars', default=None,
              help='Space-delimited list of characters to process (e.g., "人 女 母")')
@click.option('--dry-run', is_flag=True,
              help='Preview what would be generated without writing files')
@click.option('--status', 'show_status', is_flag=True,
              help='Show generation status report only')
def cli(config, output_format, chars, dry_run, show_status):
    """Generate figure tables from figures-config.yaml

    Examples:
        python generate_figures.py --format all
        python generate_figures.py --format latex --chars "人 父 分"
        python generate_figures.py --format markdown --dry-run
        python generate_figures.py --chars "甲 乙 丙 丁" --dry-run
        python generate_figures.py --status
    """
    generator = FigureGenerator(config)
    filter_chars = chars.split() if chars else None

    # Status report only
    if show_status:
        generator.generate_status_report()
        return

    # Show header
    click.echo("\n" + "="*60)
    if dry_run:
        click.echo(f"DRY RUN: {output_format.upper()} TABLES")
    else:
        click.echo(f"GENERATING {output_format.upper()} TABLES")
    if filter_chars:
        click.echo(f"Filtering characters: {' '.join(filter_chars)}")
    click.echo("="*60)

    # Generate based on format
    if output_format in ['latex', 'all']:
        click.echo("\nGenerating LaTeX tables...")
        latex_files = generator.generate_all_latex(dry_run=dry_run, filter_chars=filter_chars)
        if dry_run:
            click.secho(f"💡 Would generate {len(latex_files)} LaTeX files", fg='yellow')
        else:
            click.secho(f"✓ Generated {len(latex_files)} LaTeX files", fg='green')

    if output_format in ['markdown', 'all']:
        click.echo("\nGenerating Markdown tables...")
        md_files = generator.generate_all_markdown(dry_run=dry_run, filter_chars=filter_chars)
        if dry_run:
            click.secho(f"💡 Would generate {len(md_files)} Markdown files", fg='yellow')
        else:
            click.secho(f"✓ Generated {len(md_files)} Markdown files", fg='green')

    # Show completion
    click.echo("\n" + "="*60)
    if dry_run:
        click.echo("DRY RUN COMPLETE")
        click.secho("Run without --dry-run to actually create files", fg='yellow')
    else:
        click.echo("GENERATION COMPLETE")
    click.echo("="*60)

    generator.generate_status_report()


if __name__ == '__main__':
    cli()
