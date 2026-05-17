# Validation Research Notes

## Scope

Created a 50-case expanded validation corpus without changing the calculator engine.

## Sources

- Wikibooks period pages: `https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_1` through `Period_9`.
- WOFS Flying Star Calculator: `https://www.wofs.com/flying-star-calculator/`.

## Important Normalization

Wikibooks raw cells use left-superscript / center / right-superscript notation; based on validated handoff cases, stored triples are `[right-superscript center left-superscript]` = `[mountain water base]`.

WOFS forum-friendly output labels values as `b`, `m`, `w`. Cross-checking against already validated fixtures shows the needed mapping is:

- WOFS `w` -> mountain star
- WOFS `b` -> water star
- WOFS `m` -> base star

This is documented in each validation note. No formula inference was used.

## Result

- Cases collected: 50
- Cross-source confirmed: 50
- Conflicting: 0
- Weak/single-source in this expanded corpus: 0

## Caution

The existing Phase 1 fixture includes `VC001` as `Period 9 / Facing SE` from WOFS. WOFS' calculator form uses 24-mountain facings (`SE1`, `SE2`, `SE3`) rather than plain `SE`; keep `VC001` as a legacy fixture until separately explained or replaced.
