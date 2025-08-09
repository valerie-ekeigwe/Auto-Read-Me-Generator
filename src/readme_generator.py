from pathlib import Path
from typing import Dict
from jinja2 import Environment, FileSystemLoader, select_autoescape

def render_readme(context: Dict, template_name: str = "minimal") -> str:
    templates_dir = Path(__file__).resolve().parents[1] / "templates"
    candidate = templates_dir / f"{template_name}.md.j2"
    template_file = candidate.name if candidate.exists() else "README_template.md"

    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(enabled_extensions=("md",)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(template_file)
    return template.render(**context)
