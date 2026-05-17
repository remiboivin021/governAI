# Spécification overlay

## Emplacement

`sources/overlays/<nom>.md`

## Rôle

Un overlay est un **modificateur comportemental modulaire** qui ajoute des règles, contraintes ou structure de sortie par-dessus une persona.

Plusieurs overlays peuvent être empilés (appliqués dans l'ordre du catalogue).

## Structure

| Section | Requise | Utilisée par le compilateur | Description |
|---|---|---|---|
| `# Overlay: <nom>` | oui | — | Titre |
| `## Rules` | oui | ✅ Extraites comme règles | Comportements que le modèle DOIT suivre |
| `## Constraints` | oui | ✅ Extraites comme contraintes | Comportements que le modèle NE DOIT PAS faire |
| `## Output Behavior` | oui | ✅ Extrait comme format de sortie | Structure de réponse attendue |

## Fonctionnement de la compilation

Le compilateur lit chaque overlay avec `compile_overlay()` :

- Trouve les sections `## Rules`, `## Constraints`, `## Output behavior`
- Extrait les lignes commençant par `- ` (listes markdown)
- Ignore les séparateurs `---`
- Fusionne les résultats dans les sections du prompt `=== RULES ===`, `=== CONSTRAINTS ===`, `=== OUTPUT FORMAT ===`

Les overlays ne sont **pas déconflictés** : ils s'empilent séquentiellement.

## Overlays existants

| Fichier | Rôle |
|---|---|
| `diagnostics.md` | Diagnostic systématique, analyse de causes racines |
| `structured-analysis.md` | Décomposition structurée de problèmes |
| `hypothesis-driven.md` | Raisonnement hypothético-déductif |
| `strict-mode.md` | Rigueur élevée, séparation faits/hypothèses |
