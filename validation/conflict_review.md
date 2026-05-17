# Conflict Review — Previously Validated vs 216 Extracted Corpus

Date: 2026-05-18

Purpose: keep the full 216 extracted corpus active while preserving transparent review evidence for four previously validated keys whose old fixture values differ from the newly extracted Wikibooks corpus.

Current app behavior: **uses extracted Wikibooks values from the 216 corpus**. No chart values are changed by this review file.

Conflict keys: `6|NE3`, `7|W2`, `8|SW2`, `9|E1`.

## 6|NE3

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 6
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_6
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_6

### Sector differences

| Sector | Field | Previous app fixture | Extracted Wikibooks |
|---|---:|---:|---:|
| SE | mountain | 4 | 1 |
| SE | base | 1 | 4 |
| S | mountain | 8 | 5 |
| S | base | 5 | 8 |
| SW | mountain | 6 | 3 |
| SW | base | 3 | 6 |
| E | mountain | 5 | 2 |
| E | base | 2 | 5 |
| C | mountain | 3 | 9 |
| C | base | 9 | 3 |
| W | mountain | 1 | 7 |
| W | base | 7 | 1 |
| NE | mountain | 9 | 6 |
| NE | base | 6 | 9 |
| N | mountain | 7 | 4 |
| N | base | 4 | 7 |
| NW | mountain | 2 | 8 |
| NW | base | 8 | 2 |

- Difference count: 18

### Previous app fixture values

```json
{
  "SE": {
    "mountain": 4,
    "water": 5,
    "base": 1
  },
  "S": {
    "mountain": 8,
    "water": 1,
    "base": 5
  },
  "SW": {
    "mountain": 6,
    "water": 3,
    "base": 3
  },
  "E": {
    "mountain": 5,
    "water": 4,
    "base": 2
  },
  "C": {
    "mountain": 3,
    "water": 6,
    "base": 9
  },
  "W": {
    "mountain": 1,
    "water": 8,
    "base": 7
  },
  "NE": {
    "mountain": 9,
    "water": 9,
    "base": 6
  },
  "N": {
    "mountain": 7,
    "water": 2,
    "base": 4
  },
  "NW": {
    "mountain": 2,
    "water": 7,
    "base": 8
  }
}
```

### Extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 1,
    "water": 5,
    "base": 4
  },
  "S": {
    "mountain": 5,
    "water": 1,
    "base": 8
  },
  "SW": {
    "mountain": 3,
    "water": 3,
    "base": 6
  },
  "E": {
    "mountain": 2,
    "water": 4,
    "base": 5
  },
  "C": {
    "mountain": 9,
    "water": 6,
    "base": 3
  },
  "W": {
    "mountain": 7,
    "water": 8,
    "base": 1
  },
  "NE": {
    "mountain": 6,
    "water": 9,
    "base": 9
  },
  "N": {
    "mountain": 4,
    "water": 2,
    "base": 7
  },
  "NW": {
    "mountain": 8,
    "water": 7,
    "base": 2
  }
}
```

## 7|W2

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 7
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_7
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_7

### Sector differences

| Sector | Field | Previous app fixture | Extracted Wikibooks |
|---|---:|---:|---:|
| SE | mountain | 6 | 1 |
| SE | base | 1 | 6 |
| S | mountain | 1 | 5 |
| S | base | 5 | 1 |
| SW | mountain | 8 | 3 |
| SW | base | 3 | 8 |
| E | mountain | 7 | 2 |
| E | base | 2 | 7 |
| C | mountain | 5 | 9 |
| C | base | 9 | 5 |
| W | mountain | 3 | 7 |
| W | base | 7 | 3 |
| NE | mountain | 2 | 6 |
| NE | base | 6 | 2 |
| N | mountain | 9 | 4 |
| N | base | 4 | 9 |
| NW | mountain | 4 | 8 |
| NW | base | 8 | 4 |

- Difference count: 18

### Previous app fixture values

```json
{
  "SE": {
    "mountain": 6,
    "water": 6,
    "base": 1
  },
  "S": {
    "mountain": 1,
    "water": 2,
    "base": 5
  },
  "SW": {
    "mountain": 8,
    "water": 4,
    "base": 3
  },
  "E": {
    "mountain": 7,
    "water": 5,
    "base": 2
  },
  "C": {
    "mountain": 5,
    "water": 7,
    "base": 9
  },
  "W": {
    "mountain": 3,
    "water": 9,
    "base": 7
  },
  "NE": {
    "mountain": 2,
    "water": 1,
    "base": 6
  },
  "N": {
    "mountain": 9,
    "water": 3,
    "base": 4
  },
  "NW": {
    "mountain": 4,
    "water": 8,
    "base": 8
  }
}
```

### Extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 1,
    "water": 6,
    "base": 6
  },
  "S": {
    "mountain": 5,
    "water": 2,
    "base": 1
  },
  "SW": {
    "mountain": 3,
    "water": 4,
    "base": 8
  },
  "E": {
    "mountain": 2,
    "water": 5,
    "base": 7
  },
  "C": {
    "mountain": 9,
    "water": 7,
    "base": 5
  },
  "W": {
    "mountain": 7,
    "water": 9,
    "base": 3
  },
  "NE": {
    "mountain": 6,
    "water": 1,
    "base": 2
  },
  "N": {
    "mountain": 4,
    "water": 3,
    "base": 9
  },
  "NW": {
    "mountain": 8,
    "water": 8,
    "base": 4
  }
}
```

## 8|SW2

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 8
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_8
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_8

### Sector differences

| Sector | Field | Previous app fixture | Extracted Wikibooks |
|---|---:|---:|---:|
| SE | mountain | 1 | 4 |
| SE | base | 4 | 1 |
| S | mountain | 6 | 9 |
| S | base | 9 | 6 |
| SW | mountain | 8 | 2 |
| SW | base | 2 | 8 |
| E | mountain | 9 | 3 |
| E | base | 3 | 9 |
| C | mountain | 2 | 5 |
| C | base | 5 | 2 |
| W | mountain | 4 | 7 |
| W | base | 7 | 4 |
| NE | mountain | 5 | 8 |
| NE | base | 8 | 5 |
| N | mountain | 7 | 1 |
| N | base | 1 | 7 |
| NW | mountain | 3 | 6 |
| NW | base | 6 | 3 |

- Difference count: 18

### Previous app fixture values

```json
{
  "SE": {
    "mountain": 1,
    "water": 7,
    "base": 4
  },
  "S": {
    "mountain": 6,
    "water": 3,
    "base": 9
  },
  "SW": {
    "mountain": 8,
    "water": 5,
    "base": 2
  },
  "E": {
    "mountain": 9,
    "water": 6,
    "base": 3
  },
  "C": {
    "mountain": 2,
    "water": 8,
    "base": 5
  },
  "W": {
    "mountain": 4,
    "water": 1,
    "base": 7
  },
  "NE": {
    "mountain": 5,
    "water": 2,
    "base": 8
  },
  "N": {
    "mountain": 7,
    "water": 4,
    "base": 1
  },
  "NW": {
    "mountain": 3,
    "water": 9,
    "base": 6
  }
}
```

### Extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 4,
    "water": 7,
    "base": 1
  },
  "S": {
    "mountain": 9,
    "water": 3,
    "base": 6
  },
  "SW": {
    "mountain": 2,
    "water": 5,
    "base": 8
  },
  "E": {
    "mountain": 3,
    "water": 6,
    "base": 9
  },
  "C": {
    "mountain": 5,
    "water": 8,
    "base": 2
  },
  "W": {
    "mountain": 7,
    "water": 1,
    "base": 4
  },
  "NE": {
    "mountain": 8,
    "water": 2,
    "base": 5
  },
  "N": {
    "mountain": 1,
    "water": 4,
    "base": 7
  },
  "NW": {
    "mountain": 6,
    "water": 9,
    "base": 3
  }
}
```

## 9|E1

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 9
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_9
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_9

### Sector differences

| Sector | Field | Previous app fixture | Extracted Wikibooks |
|---|---:|---:|---:|
| SE | mountain | 3 | 6 |
| SE | base | 6 | 3 |
| S | mountain | 7 | 2 |
| S | base | 2 | 7 |
| SW | mountain | 5 | 4 |
| SW | base | 4 | 5 |
| E | mountain | 4 | 5 |
| E | base | 5 | 4 |
| C | mountain | 2 | 7 |
| C | base | 7 | 2 |
| NE | mountain | 8 | 1 |
| NE | base | 1 | 8 |
| N | mountain | 6 | 3 |
| N | base | 3 | 6 |
| NW | mountain | 1 | 8 |
| NW | base | 8 | 1 |

- Difference count: 16

### Previous app fixture values

```json
{
  "SE": {
    "mountain": 3,
    "water": 8,
    "base": 6
  },
  "S": {
    "mountain": 7,
    "water": 4,
    "base": 2
  },
  "SW": {
    "mountain": 5,
    "water": 6,
    "base": 4
  },
  "E": {
    "mountain": 4,
    "water": 7,
    "base": 5
  },
  "C": {
    "mountain": 2,
    "water": 9,
    "base": 7
  },
  "W": {
    "mountain": 9,
    "water": 2,
    "base": 9
  },
  "NE": {
    "mountain": 8,
    "water": 3,
    "base": 1
  },
  "N": {
    "mountain": 6,
    "water": 5,
    "base": 3
  },
  "NW": {
    "mountain": 1,
    "water": 1,
    "base": 8
  }
}
```

### Extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 6,
    "water": 8,
    "base": 3
  },
  "S": {
    "mountain": 2,
    "water": 4,
    "base": 7
  },
  "SW": {
    "mountain": 4,
    "water": 6,
    "base": 5
  },
  "E": {
    "mountain": 5,
    "water": 7,
    "base": 4
  },
  "C": {
    "mountain": 7,
    "water": 9,
    "base": 2
  },
  "W": {
    "mountain": 9,
    "water": 2,
    "base": 9
  },
  "NE": {
    "mountain": 1,
    "water": 3,
    "base": 8
  },
  "N": {
    "mountain": 3,
    "water": 5,
    "base": 6
  },
  "NW": {
    "mountain": 8,
    "water": 1,
    "base": 1
  }
}
```
