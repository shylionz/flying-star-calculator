# Conflict Review — Previous App Fixture vs Corrected 216 Extracted Corpus

Date: 2026-05-18

Purpose: keep the full 216 extracted corpus active while preserving transparent review evidence for four previously validated keys whose old fixture values differ from the extracted corpus.

Normalization correction applied: Wikibooks raw cell `<sup>A</sup>B<sup>C</sup>` is normalized as `mountain=A`, `water=C`, `base=B`.

Current app behavior: **uses corrected extracted Wikibooks values from the 216 corpus**. No conflict key is reverted to the old fixture values.

Previous fixture baseline ref: `ec81c45`.

Conflict keys: `6|NE3`, `7|W2`, `8|SW2`, `9|E1`.

## 6|NE3

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 6
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_6
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_6

### Raw Wikibooks cells

```json
{
  "SE": "451",
  "S": "815",
  "SW": "633",
  "E": "542",
  "C": "369",
  "W": "187",
  "NE": "996",
  "N": "724",
  "NW": "278"
}
```

### Sector differences

| Sector | Field | Previous app fixture | Corrected extracted Wikibooks |
|---|---:|---:|---:|
| SE | water | 5 | 1 |
| SE | base | 1 | 5 |
| S | water | 1 | 5 |
| S | base | 5 | 1 |
| E | water | 4 | 2 |
| E | base | 2 | 4 |
| C | water | 6 | 9 |
| C | base | 9 | 6 |
| W | water | 8 | 7 |
| W | base | 7 | 8 |
| NE | water | 9 | 6 |
| NE | base | 6 | 9 |
| N | water | 2 | 4 |
| N | base | 4 | 2 |
| NW | water | 7 | 8 |
| NW | base | 8 | 7 |

- Difference count: 16

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

### Corrected extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 4,
    "water": 1,
    "base": 5
  },
  "S": {
    "mountain": 8,
    "water": 5,
    "base": 1
  },
  "SW": {
    "mountain": 6,
    "water": 3,
    "base": 3
  },
  "E": {
    "mountain": 5,
    "water": 2,
    "base": 4
  },
  "C": {
    "mountain": 3,
    "water": 9,
    "base": 6
  },
  "W": {
    "mountain": 1,
    "water": 7,
    "base": 8
  },
  "NE": {
    "mountain": 9,
    "water": 6,
    "base": 9
  },
  "N": {
    "mountain": 7,
    "water": 4,
    "base": 2
  },
  "NW": {
    "mountain": 2,
    "water": 8,
    "base": 7
  }
}
```

## 7|W2

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 7
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_7
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_7

### Raw Wikibooks cells

```json
{
  "SE": "661",
  "S": "125",
  "SW": "843",
  "E": "752",
  "C": "579",
  "W": "397",
  "NE": "216",
  "N": "934",
  "NW": "488"
}
```

### Sector differences

| Sector | Field | Previous app fixture | Corrected extracted Wikibooks |
|---|---:|---:|---:|
| SE | water | 6 | 1 |
| SE | base | 1 | 6 |
| S | water | 2 | 5 |
| S | base | 5 | 2 |
| SW | water | 4 | 3 |
| SW | base | 3 | 4 |
| E | water | 5 | 2 |
| E | base | 2 | 5 |
| C | water | 7 | 9 |
| C | base | 9 | 7 |
| W | water | 9 | 7 |
| W | base | 7 | 9 |
| NE | water | 1 | 6 |
| NE | base | 6 | 1 |
| N | water | 3 | 4 |
| N | base | 4 | 3 |

- Difference count: 16

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

### Corrected extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 6,
    "water": 1,
    "base": 6
  },
  "S": {
    "mountain": 1,
    "water": 5,
    "base": 2
  },
  "SW": {
    "mountain": 8,
    "water": 3,
    "base": 4
  },
  "E": {
    "mountain": 7,
    "water": 2,
    "base": 5
  },
  "C": {
    "mountain": 5,
    "water": 9,
    "base": 7
  },
  "W": {
    "mountain": 3,
    "water": 7,
    "base": 9
  },
  "NE": {
    "mountain": 2,
    "water": 6,
    "base": 1
  },
  "N": {
    "mountain": 9,
    "water": 4,
    "base": 3
  },
  "NW": {
    "mountain": 4,
    "water": 8,
    "base": 8
  }
}
```

## 8|SW2

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 8
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_8
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_8

### Raw Wikibooks cells

```json
{
  "SE": "174",
  "S": "639",
  "SW": "852",
  "E": "963",
  "C": "285",
  "W": "417",
  "NE": "528",
  "N": "741",
  "NW": "396"
}
```

### Sector differences

| Sector | Field | Previous app fixture | Corrected extracted Wikibooks |
|---|---:|---:|---:|
| SE | water | 7 | 4 |
| SE | base | 4 | 7 |
| S | water | 3 | 9 |
| S | base | 9 | 3 |
| SW | water | 5 | 2 |
| SW | base | 2 | 5 |
| E | water | 6 | 3 |
| E | base | 3 | 6 |
| C | water | 8 | 5 |
| C | base | 5 | 8 |
| W | water | 1 | 7 |
| W | base | 7 | 1 |
| NE | water | 2 | 8 |
| NE | base | 8 | 2 |
| N | water | 4 | 1 |
| N | base | 1 | 4 |
| NW | water | 9 | 6 |
| NW | base | 6 | 9 |

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

### Corrected extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 1,
    "water": 4,
    "base": 7
  },
  "S": {
    "mountain": 6,
    "water": 9,
    "base": 3
  },
  "SW": {
    "mountain": 8,
    "water": 2,
    "base": 5
  },
  "E": {
    "mountain": 9,
    "water": 3,
    "base": 6
  },
  "C": {
    "mountain": 2,
    "water": 5,
    "base": 8
  },
  "W": {
    "mountain": 4,
    "water": 7,
    "base": 1
  },
  "NE": {
    "mountain": 5,
    "water": 8,
    "base": 2
  },
  "N": {
    "mountain": 7,
    "water": 1,
    "base": 4
  },
  "NW": {
    "mountain": 3,
    "water": 6,
    "base": 9
  }
}
```

## 9|E1

### Sources

- Previous app fixture source: Wikibooks - Feng Shui Flying Star Feng Shui/Period 9
- Previous app fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_9
- Extracted fixture source: Wikibooks Flying Star Feng Shui period page
- Extracted fixture source URL: https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_9

### Raw Wikibooks cells

```json
{
  "SE": "386",
  "S": "742",
  "SW": "564",
  "E": "475",
  "C": "297",
  "W": "929",
  "NE": "831",
  "N": "653",
  "NW": "118"
}
```

### Sector differences

| Sector | Field | Previous app fixture | Corrected extracted Wikibooks |
|---|---:|---:|---:|
| SE | water | 8 | 6 |
| SE | base | 6 | 8 |
| S | water | 4 | 2 |
| S | base | 2 | 4 |
| SW | water | 6 | 4 |
| SW | base | 4 | 6 |
| E | water | 7 | 5 |
| E | base | 5 | 7 |
| C | water | 9 | 7 |
| C | base | 7 | 9 |
| W | water | 2 | 9 |
| W | base | 9 | 2 |
| NE | water | 3 | 1 |
| NE | base | 1 | 3 |
| N | water | 5 | 3 |
| N | base | 3 | 5 |
| NW | water | 1 | 8 |
| NW | base | 8 | 1 |

- Difference count: 18

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

### Corrected extracted Wikibooks values currently used by app

```json
{
  "SE": {
    "mountain": 3,
    "water": 6,
    "base": 8
  },
  "S": {
    "mountain": 7,
    "water": 2,
    "base": 4
  },
  "SW": {
    "mountain": 5,
    "water": 4,
    "base": 6
  },
  "E": {
    "mountain": 4,
    "water": 5,
    "base": 7
  },
  "C": {
    "mountain": 2,
    "water": 7,
    "base": 9
  },
  "W": {
    "mountain": 9,
    "water": 9,
    "base": 2
  },
  "NE": {
    "mountain": 8,
    "water": 1,
    "base": 3
  },
  "N": {
    "mountain": 6,
    "water": 3,
    "base": 5
  },
  "NW": {
    "mountain": 1,
    "water": 8,
    "base": 1
  }
}
```
