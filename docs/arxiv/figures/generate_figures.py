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

    def generate_all_latex(self, output_dir="generated"):
        """Generate LaTeX tables for all sections"""
        output_path = self.base_dir / output_dir
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

                    # Generate LaTeX
                    latex_content = self.generate_latex_table(
                        char_objects,
                        caption,
                        fig_id
                    )

                    # Write to file
                    filename = f"{fig_id}-evolution.tex"
                    filepath = output_path / filename

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(latex_content)

                    generated_files.append(filename)
                    print(f"✓ Generated: {filename}")

        return generated_files

    def generate_all_markdown(self, output_dir="generated"):
        """Generate Markdown tables for all sections"""
        output_path = self.base_dir / output_dir
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

                    # Generate Markdown
                    md_content = self.generate_markdown_table(
                        char_objects,
                        caption,
                        fig_id
                    )

                    # Write to file
                    filename = f"{fig_id}-evolution.md"
                    filepath = output_path / filename

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(md_content)

                    generated_files.append(filename)
                    print(f"✓ Generated: {filename}")

        return generated_files

    def generate_latex_table(self, characters, caption, label):
        """Generate LaTeX table for character evolution"""

        col_width = self.latex_settings.get('column_width', '1.2cm')
        font_modern = self.latex_settings.get('font_modern', '\\Huge')

        # Start table
        latex = []
        latex.append("\\begin{figure}[htbp]")
        latex.append("\\centering")
        latex.append("\\begin{tabular}{|c|c|c|c|l|}")
        latex.append("\\hline")
        latex.append("\\textbf{Oracle} & \\textbf{Bronze} & \\textbf{Seal} & \\textbf{Modern} & \\textbf{Character} \\\\")
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
        modern = files.get('modern', '')

        # Character info
        char_info = f"{hanzi} ({pinyin}) - {meaning}"

        # Build cells
        cells = []

        # Oracle
        if oracle:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/oracle/{oracle}}}")
        else:
            cells.append("\\textit{(unavailable)}")

        # Bronze
        if bronze:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/bronze/{bronze}}}")
        else:
            cells.append("\\textit{(unavailable)}")

        # Seal
        if seal:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/seal/{seal}}}")
        else:
            cells.append("\\textit{(unavailable)}")

        # Modern (use Unicode character or image)
        if modern:
            cells.append(f"\\includegraphics[width={col_width}]{{figures/characters/modern/{modern}}}")
        else:
            cells.append(f"{{{font_modern} {hanzi}}}")

        # Character info
        cells.append(char_info)

        return ' & '.join(cells) + ' \\\\'

    def generate_markdown_table(self, characters, caption, label):
        """Generate Markdown table for character evolution"""

        img_width = self.markdown_settings.get('image_width', '100px')
        use_unicode = self.markdown_settings.get('use_unicode_modern', True)

        # Start table
        md = []
        md.append(f"## {label}")
        md.append("")
        md.append(caption)
        md.append("")
        md.append("| Oracle | Bronze | Seal | Modern | Character |")
        md.append("|--------|--------|------|--------|-----------|")

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
        modern = files.get('modern', '')

        # Character info
        char_info = f"{hanzi} ({pinyin}) - {meaning}"

        # Build cells
        cells = []

        # Oracle
        if oracle:
            cells.append(f"![oracle](characters/oracle/{oracle})")
        else:
            cells.append("(unavailable)")

        # Bronze
        if bronze:
            cells.append(f"![bronze](characters/bronze/{bronze})")
        else:
            cells.append("(unavailable)")

        # Seal
        if seal:
            cells.append(f"![seal](characters/seal/{seal})")
        else:
            cells.append("(unavailable)")

        # Modern
        if use_unicode:
            cells.append(hanzi)
        elif modern:
            cells.append(f"![modern](characters/modern/{modern})")
        else:
            cells.append(hanzi)

        # Character info
        cells.append(char_info)

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


@click.group(invoke_without_command=True)
@click.option('--config', default='figures-config.yaml',
              help='Path to configuration file')
@click.pass_context
def cli(ctx, config):
    """Generate figure tables from figures-config.yaml

    Examples:
        python generate_figures.py latex
        python generate_figures.py markdown
        python generate_figures.py all
        python generate_figures.py status
    """
    # Store config in context for subcommands
    ctx.ensure_object(dict)
    ctx.obj['config'] = config

    # If no subcommand, show help
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.command()
@click.pass_context
def latex(ctx):
    """Generate LaTeX tables only"""
    config = ctx.obj['config']
    generator = FigureGenerator(config)

    click.echo("\n" + "="*60)
    click.echo("GENERATING LATEX TABLES")
    click.echo("="*60)

    click.echo("\nGenerating LaTeX tables...")
    latex_files = generator.generate_all_latex()
    click.secho(f"\n✓ Generated {len(latex_files)} LaTeX files", fg='green')

    click.echo("\n" + "="*60)
    generator.generate_status_report()


@cli.command()
@click.pass_context
def markdown(ctx):
    """Generate Markdown tables only"""
    config = ctx.obj['config']
    generator = FigureGenerator(config)

    click.echo("\n" + "="*60)
    click.echo("GENERATING MARKDOWN TABLES")
    click.echo("="*60)

    click.echo("\nGenerating Markdown tables...")
    md_files = generator.generate_all_markdown()
    click.secho(f"\n✓ Generated {len(md_files)} Markdown files", fg='green')

    click.echo("\n" + "="*60)
    generator.generate_status_report()


@cli.command()
@click.pass_context
def all(ctx):
    """Generate both LaTeX and Markdown tables"""
    config = ctx.obj['config']
    generator = FigureGenerator(config)

    click.echo("\n" + "="*60)
    click.echo("GENERATING ALL TABLES")
    click.echo("="*60)

    click.echo("\nGenerating LaTeX tables...")
    latex_files = generator.generate_all_latex()
    click.secho(f"✓ Generated {len(latex_files)} LaTeX files", fg='green')

    click.echo("\nGenerating Markdown tables...")
    md_files = generator.generate_all_markdown()
    click.secho(f"✓ Generated {len(md_files)} Markdown files", fg='green')

    click.echo("\n" + "="*60)
    click.echo("GENERATION COMPLETE")
    click.echo("="*60)

    generator.generate_status_report()


@cli.command()
@click.pass_context
def status(ctx):
    """Show progress status report"""
    config = ctx.obj['config']
    generator = FigureGenerator(config)
    generator.generate_status_report()


if __name__ == '__main__':
    cli(obj={})
