from typing import List, Dict, Any


# =========================================================
# 1. IR BUILDER
# =========================================================

def build_ir(persona: str, overlays: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Build intermediate representation (IR) from persona + overlays.
    """

    rules = []
    constraints = []
    output_format = []

    for overlay in overlays:
        if not isinstance(overlay, dict):
            continue

        rules.extend(overlay.get("rules", []))
        constraints.extend(overlay.get("constraints", []))
        output_format.extend(overlay.get("output", []))

    return {
        "persona": persona,
        "rules": rules,
        "constraints": constraints,
        "output_format": output_format,
    }


# =========================================================
# 2. IR NORMALIZATION
# =========================================================

def normalize_ir(ir: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean IR: remove duplicates, normalize empty fields.
    """

    def dedupe(lst):
        seen = set()
        out = []
        for x in lst:
            if x and x not in seen:
                seen.add(x)
                out.append(x)
        return out

    return {
        "persona": ir.get("persona", ""),
        "rules": dedupe(ir.get("rules", [])),
        "constraints": dedupe(ir.get("constraints", [])),
        "output_format": dedupe(ir.get("output_format", [])),
    }


# =========================================================
# 3. FLATTEN TO OPENCODE PROMPT
# =========================================================

def flatten_to_opencode_prompt(ir: Dict[str, Any], task_rules: List[str] | None = None) -> str:
    """
    Convert IR → OpenCode system prompt string.
    """

    sections = []

    # Persona
    sections.append("SYSTEM PERSONA:")
    sections.append(ir["persona"].strip())

    # Rules
    if ir["rules"]:
        sections.append("=== RULES ===")
        sections.append("\n".join(ir["rules"]))

    # Constraints
    if ir["constraints"]:
        sections.append("=== CONSTRAINTS ===")
        sections.append("\n".join(ir["constraints"]))

    # Task behavior
    if task_rules:
        sections.append("=== TASK BEHAVIOR ===")
        sections.append("\n".join(task_rules))

    # Output format
    if ir["output_format"]:
        sections.append("=== OUTPUT FORMAT ===")
        sections.append("\n".join(ir["output_format"]))

    return "\n\n".join(sections).strip()

# =========================================================
# 4. OVERLAY COMPILER
# =========================================================

def compile_overlay(raw_text: str) -> Dict[str, List[str]]:
    """
    Parse overlay markdown → structured dict.
    """

    def extract(section: str) -> List[str]:
        marker = f"## {section}"
        if marker not in raw_text:
            return []

        block = raw_text.split(marker)[1]
        block = block.split("\n##")[0]

        lines = []
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("- "):
                lines.append(line[2:].strip())

        return lines

    return {
        "rules": extract("Rules"),
        "constraints": extract("Constraints"),
        "output": extract("Output Behavior"),
    }