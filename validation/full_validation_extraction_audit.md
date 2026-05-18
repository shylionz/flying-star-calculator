# Full Validation Corpus Extraction Audit

Date: 2026-05-18

Source: Wikibooks Flying Star Feng Shui Period 1-9 pages.
Normalization: raw Wikibooks cell `<sup>A</sup>B<sup>C</sup>` => mountain=A, water=C, base=B; app stores `{mountain, water, base}`.

## Period audits

### Period 1

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period1.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P1-E1",
  "period": 1,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_1",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 2,
      "water": 9,
      "base": 9
    },
    "S": {
      "mountain": 7,
      "water": 4,
      "base": 5
    },
    "SW": {
      "mountain": 9,
      "water": 2,
      "base": 7
    },
    "E": {
      "mountain": 1,
      "water": 1,
      "base": 8
    },
    "C": {
      "mountain": 3,
      "water": 8,
      "base": 1
    },
    "W": {
      "mountain": 5,
      "water": 6,
      "base": 3
    },
    "NE": {
      "mountain": 6,
      "water": 5,
      "base": 4
    },
    "N": {
      "mountain": 8,
      "water": 3,
      "base": 6
    },
    "NW": {
      "mountain": 4,
      "water": 7,
      "base": 2
    }
  },
  "raw_cells": {
    "SE": "299",
    "S": "754",
    "SW": "972",
    "E": "181",
    "C": "318",
    "W": "536",
    "NE": "645",
    "N": "863",
    "NW": "427"
  }
}
```

### Period 2

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period2.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P2-E1",
  "period": 2,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_2",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 5,
      "water": 8,
      "base": 1
    },
    "S": {
      "mountain": 9,
      "water": 4,
      "base": 6
    },
    "SW": {
      "mountain": 7,
      "water": 6,
      "base": 8
    },
    "E": {
      "mountain": 6,
      "water": 7,
      "base": 9
    },
    "C": {
      "mountain": 4,
      "water": 9,
      "base": 2
    },
    "W": {
      "mountain": 2,
      "water": 2,
      "base": 4
    },
    "NE": {
      "mountain": 1,
      "water": 3,
      "base": 5
    },
    "N": {
      "mountain": 8,
      "water": 5,
      "base": 7
    },
    "NW": {
      "mountain": 3,
      "water": 1,
      "base": 3
    }
  },
  "raw_cells": {
    "SE": "518",
    "S": "964",
    "SW": "786",
    "E": "697",
    "C": "429",
    "W": "242",
    "NE": "153",
    "N": "875",
    "NW": "331"
  }
}
```

### Period 3

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period3.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P3-E1",
  "period": 3,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_3",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 4,
      "water": 9,
      "base": 2
    },
    "S": {
      "mountain": 9,
      "water": 5,
      "base": 7
    },
    "SW": {
      "mountain": 2,
      "water": 7,
      "base": 9
    },
    "E": {
      "mountain": 3,
      "water": 8,
      "base": 1
    },
    "C": {
      "mountain": 5,
      "water": 1,
      "base": 3
    },
    "W": {
      "mountain": 7,
      "water": 3,
      "base": 5
    },
    "NE": {
      "mountain": 8,
      "water": 4,
      "base": 6
    },
    "N": {
      "mountain": 1,
      "water": 6,
      "base": 8
    },
    "NW": {
      "mountain": 6,
      "water": 2,
      "base": 4
    }
  },
  "raw_cells": {
    "SE": "429",
    "S": "975",
    "SW": "297",
    "E": "318",
    "C": "531",
    "W": "753",
    "NE": "864",
    "N": "186",
    "NW": "642"
  }
}
```

### Period 4

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period4.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P4-E1",
  "period": 4,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_4",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 7,
      "water": 3,
      "base": 3
    },
    "S": {
      "mountain": 2,
      "water": 7,
      "base": 8
    },
    "SW": {
      "mountain": 9,
      "water": 5,
      "base": 1
    },
    "E": {
      "mountain": 8,
      "water": 4,
      "base": 2
    },
    "C": {
      "mountain": 6,
      "water": 2,
      "base": 4
    },
    "W": {
      "mountain": 4,
      "water": 9,
      "base": 6
    },
    "NE": {
      "mountain": 3,
      "water": 8,
      "base": 7
    },
    "N": {
      "mountain": 1,
      "water": 6,
      "base": 9
    },
    "NW": {
      "mountain": 5,
      "water": 1,
      "base": 5
    }
  },
  "raw_cells": {
    "SE": "733",
    "S": "287",
    "SW": "915",
    "E": "824",
    "C": "642",
    "W": "469",
    "NE": "378",
    "N": "196",
    "NW": "551"
  }
}
```

### Period 5

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period5.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P5-E1",
  "period": 5,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_5",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 6,
      "water": 2,
      "base": 4
    },
    "S": {
      "mountain": 2,
      "water": 7,
      "base": 9
    },
    "SW": {
      "mountain": 4,
      "water": 9,
      "base": 2
    },
    "E": {
      "mountain": 5,
      "water": 1,
      "base": 3
    },
    "C": {
      "mountain": 7,
      "water": 3,
      "base": 5
    },
    "W": {
      "mountain": 9,
      "water": 5,
      "base": 7
    },
    "NE": {
      "mountain": 1,
      "water": 6,
      "base": 8
    },
    "N": {
      "mountain": 3,
      "water": 8,
      "base": 1
    },
    "NW": {
      "mountain": 8,
      "water": 4,
      "base": 6
    }
  },
  "raw_cells": {
    "SE": "642",
    "S": "297",
    "SW": "429",
    "E": "531",
    "C": "753",
    "W": "975",
    "NE": "186",
    "N": "318",
    "NW": "864"
  }
}
```

### Period 6

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period6.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P6-E1",
  "period": 6,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_6",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 9,
      "water": 5,
      "base": 5
    },
    "S": {
      "mountain": 4,
      "water": 9,
      "base": 1
    },
    "SW": {
      "mountain": 2,
      "water": 7,
      "base": 3
    },
    "E": {
      "mountain": 1,
      "water": 6,
      "base": 4
    },
    "C": {
      "mountain": 8,
      "water": 4,
      "base": 6
    },
    "W": {
      "mountain": 6,
      "water": 2,
      "base": 8
    },
    "NE": {
      "mountain": 5,
      "water": 1,
      "base": 9
    },
    "N": {
      "mountain": 3,
      "water": 8,
      "base": 2
    },
    "NW": {
      "mountain": 7,
      "water": 3,
      "base": 7
    }
  },
  "raw_cells": {
    "SE": "955",
    "S": "419",
    "SW": "237",
    "E": "146",
    "C": "864",
    "W": "682",
    "NE": "591",
    "N": "328",
    "NW": "773"
  }
}
```

### Period 7

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period7.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P7-E1",
  "period": 7,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_7",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 8,
      "water": 4,
      "base": 6
    },
    "S": {
      "mountain": 4,
      "water": 9,
      "base": 2
    },
    "SW": {
      "mountain": 6,
      "water": 2,
      "base": 4
    },
    "E": {
      "mountain": 7,
      "water": 3,
      "base": 5
    },
    "C": {
      "mountain": 9,
      "water": 5,
      "base": 7
    },
    "W": {
      "mountain": 2,
      "water": 7,
      "base": 9
    },
    "NE": {
      "mountain": 3,
      "water": 8,
      "base": 1
    },
    "N": {
      "mountain": 5,
      "water": 1,
      "base": 3
    },
    "NW": {
      "mountain": 1,
      "water": 6,
      "base": 8
    }
  },
  "raw_cells": {
    "SE": "864",
    "S": "429",
    "SW": "642",
    "E": "753",
    "C": "975",
    "W": "297",
    "NE": "318",
    "N": "531",
    "NW": "186"
  }
}
```

### Period 8

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period8.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P8-E1",
  "period": 8,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_8",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
    "SE": {
      "mountain": 9,
      "water": 7,
      "base": 7
    },
    "S": {
      "mountain": 5,
      "water": 2,
      "base": 3
    },
    "SW": {
      "mountain": 7,
      "water": 9,
      "base": 5
    },
    "E": {
      "mountain": 8,
      "water": 8,
      "base": 6
    },
    "C": {
      "mountain": 1,
      "water": 6,
      "base": 8
    },
    "W": {
      "mountain": 3,
      "water": 4,
      "base": 1
    },
    "NE": {
      "mountain": 4,
      "water": 3,
      "base": 2
    },
    "N": {
      "mountain": 6,
      "water": 1,
      "base": 4
    },
    "NW": {
      "mountain": 2,
      "water": 5,
      "base": 9
    }
  },
  "raw_cells": {
    "SE": "977",
    "S": "532",
    "SW": "759",
    "E": "868",
    "C": "186",
    "W": "314",
    "NE": "423",
    "N": "641",
    "NW": "295"
  }
}
```

### Period 9

- extracted count: 24
- duplicate count: 0
- malformed count: 0
- conflicts: []
- missing facings: []
- file path: `research/corpus_period9.json`
- file size: 37739 bytes
- one sample object:

```json
{
  "id": "P9-E1",
  "period": 9,
  "facing": "E1",
  "mountain": "W1",
  "source": "Wikibooks Flying Star Feng Shui period page",
  "source_url": "https://en.wikibooks.org/wiki/Feng_Shui/Flying_Star_Feng_Shui/Period_9",
  "validation_status": "extracted",
  "validation_notes": "Extracted from Wikibooks period chart. Raw <sup>A</sup>B<sup>C</sup> cells normalized to app format as mountain=A, water=C, base=B.",
  "position_order": [
    "SE",
    "S",
    "SW",
    "E",
    "C",
    "W",
    "NE",
    "N",
    "NW"
  ],
  "grid": {
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
  },
  "raw_cells": {
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
}
```

## Full merge audit

- total extracted count: 216
- expected count: 216
- unique key count: 216
- duplicate count: 0
- malformed count: 0
- missing keys: []
- existing dataset conflicts: 216
- existing conflict keys: ['1|E1', '1|E2', '1|E3', '1|SE1', '1|SE2', '1|SE3', '1|S1', '1|S2', '1|S3', '1|SW1', '1|SW2', '1|SW3', '1|W1', '1|W2', '1|W3', '1|NW1', '1|NW2', '1|NW3', '1|N1', '1|N2', '1|N3', '1|NE1', '1|NE2', '1|NE3', '2|E1', '2|E2', '2|E3', '2|SE1', '2|SE2', '2|SE3', '2|S1', '2|S2', '2|S3', '2|SW1', '2|SW2', '2|SW3', '2|W1', '2|W2', '2|W3', '2|NW1', '2|NW2', '2|NW3', '2|N1', '2|N2', '2|N3', '2|NE1', '2|NE2', '2|NE3', '3|E1', '3|E2', '3|E3', '3|SE1', '3|SE2', '3|SE3', '3|S1', '3|S2', '3|S3', '3|SW1', '3|SW2', '3|SW3', '3|W1', '3|W2', '3|W3', '3|NW1', '3|NW2', '3|NW3', '3|N1', '3|N2', '3|N3', '3|NE1', '3|NE2', '3|NE3', '4|E1', '4|E2', '4|E3', '4|SE1', '4|SE2', '4|SE3', '4|S1', '4|S2', '4|S3', '4|SW1', '4|SW2', '4|SW3', '4|W1', '4|W2', '4|W3', '4|NW1', '4|NW2', '4|NW3', '4|N1', '4|N2', '4|N3', '4|NE1', '4|NE2', '4|NE3', '5|E1', '5|E2', '5|E3', '5|SE1', '5|SE2', '5|SE3', '5|S1', '5|S2', '5|S3', '5|SW1', '5|SW2', '5|SW3', '5|W1', '5|W2', '5|W3', '5|NW1', '5|NW2', '5|NW3', '5|N1', '5|N2', '5|N3', '5|NE1', '5|NE2', '5|NE3', '6|E1', '6|E2', '6|E3', '6|SE1', '6|SE2', '6|SE3', '6|S1', '6|S2', '6|S3', '6|SW1', '6|SW2', '6|SW3', '6|W1', '6|W2', '6|W3', '6|NW1', '6|NW2', '6|NW3', '6|N1', '6|N2', '6|N3', '6|NE1', '6|NE2', '6|NE3', '7|E1', '7|E2', '7|E3', '7|SE1', '7|SE2', '7|SE3', '7|S1', '7|S2', '7|S3', '7|SW1', '7|SW2', '7|SW3', '7|W1', '7|W2', '7|W3', '7|NW1', '7|NW2', '7|NW3', '7|N1', '7|N2', '7|N3', '7|NE1', '7|NE2', '7|NE3', '8|E1', '8|E2', '8|E3', '8|SE1', '8|SE2', '8|SE3', '8|S1', '8|S2', '8|S3', '8|SW1', '8|SW2', '8|SW3', '8|W1', '8|W2', '8|W3', '8|NW1', '8|NW2', '8|NW3', '8|N1', '8|N2', '8|N3', '8|NE1', '8|NE2', '8|NE3', '9|E1', '9|E2', '9|E3', '9|SE1', '9|SE2', '9|SE3', '9|S1', '9|S2', '9|S3', '9|SW1', '9|SW2', '9|SW3', '9|W1', '9|W2', '9|W3', '9|NW1', '9|NW2', '9|NW3', '9|N1', '9|N2', '9|N3', '9|NE1', '9|NE2', '9|NE3']
- merged corpus path: `validation/full_validation_corpus.json`
- merged corpus size: 319840 bytes
