# Pipeline de build

## Pipeline

```
catalog/index.yaml
  → résoudre persona depuis sources/personas/<nom>.md
  → résoudre overlays depuis sources/overlays/<nom>.md
  → construire l'IR (persona + règles + contraintes + sortie)
  → aplatir en chaîne de prompt
  → écrire dist/opencode.json
```

Implémenté dans `scripts/compile.py`.

## Étapes

### 1. Chargement du catalogue

Lecture de `catalog/index.yaml`, itération sur les configs activées.

### 2. Résolution des sources

- Persona : chargée depuis `sources/personas/<persona>.md`
- Overlays : chargés depuis `sources/overlays/<overlay>.md` (liste ordonnée)
- Échec du build si un fichier source est manquant

### 3. Compilation de l'IR

`build_ir()` agrège le texte de la persona + les règles/contraintes/sortie des overlays en un dictionnaire intermédiaire.

### 4. Aplatissement

`flatten_to_opencode_prompt()` produit une chaîne unique avec sections :

```
SYSTEM PERSONA:
...
=== RULES ===
...
=== CONSTRAINTS ===
...
=== TASK BEHAVIOR ===
...
=== OUTPUT FORMAT ===
...
```

### 5. Écriture du JSON

Sortie dans `dist/opencode.json` avec id, mode, model, prompt, tools, permissions.

## Artefacts de sortie

```
dist/
  opencode.json       # Configuration agent OpenCode
```

## Runtime supporté

Un seul runtime pour l'instant : **OpenCode** (`targets: [{runtime: opencode}]`).
