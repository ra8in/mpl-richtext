# mpl-richtext

**Rich text rendering for Matplotlib** - Create beautiful multi-color, multi-style text in a single line.

[![PyPI version](https://badge.fury.io/py/mpl-richtext.svg)](https://pypi.org/project/mpl-richtext/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Why mpl-richtext?

Standard Matplotlib only supports single-color text. To create multi-colored text, you need to manually position each piece and calculate spacing - tedious and error-prone!

**mpl-richtext** solves this by letting you specify colors and styles for each text segment in one simple function call.

![mpl-richtext Showcase](examples/mpl_richtext_showcase.png)

## Installation

```bash
pip install mpl-richtext
```

## Quick Start

```python
import matplotlib.pyplot as plt
from mpl_richtext import richtext

fig, ax = plt.subplots()

# Create multi-colored text in one line!
richtext(0.5, 0.5, 
         strings=["hello", ", ", "world"],
         colors=["red", "blue", "green"],
         ax=ax, fontsize=20, transform=ax.transAxes)

plt.show()
```

## Features

✨ **Multi-color text** - Different colors for each word or character  
🎨 **Multi-style text** - Mix font sizes, weights, families in one line  
📦 **Flexible input** - Lists, dicts, or tuples for colors and properties  
📏 **Auto word-wrapping** - Specify `box_width` for automatic text wrapping  
🎯 **Full alignment** - Left, center, right horizontal and vertical alignment  
⚡ **Easy to use** - Simple API, works with any Matplotlib axes

## Real-World Example

Here is a comprehensive example showing syntax highlighting, annotations, and complex formatting:

```python
import matplotlib.pyplot as plt
from mpl_richtext import richtext
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# 1. Syntax Highlighting Simulation
code_lines = [
    (["def ", "calculate_metrics", "(", "data", ", ", "threshold", "=0.5):"],
     ["#cc7832", "#ffc66d", "#a9b7c6", "#a9b7c6", "#cc7832", "#a9b7c6", "#6897bb"]),
    
    (["    ", "if ", "data", ".max() > ", "threshold", ":"],
     ["", "#cc7832", "#a9b7c6", "#a9b7c6", "#a9b7c6", "#cc7832"]),
    
    (["        ", "return ", "True"],
     ["", "#cc7832", "#cc7832"])
]

y_pos = 0.8
for strings, colors in code_lines:
    richtext(0.1, y_pos, strings, colors, ax=ax, 
             fontfamily='monospace', fontsize=14, 
             bbox=dict(facecolor='#2b2b2b', alpha=1, pad=10, boxstyle='round'))
    y_pos -= 0.15

plt.show()
```

## API Reference

### `richtext(x, y, strings, colors=None, ax=None, **kwargs)`

**Parameters:**

- **x, y** : `float`  
  Starting position of the text

- **strings** : `list of str`  
  List of text segments, e.g., `["hello", ", ", "world"]`

- **colors** : `str`, `list`, or `dict`, optional  
  Colors for each segment. Can be:
  - Single string: `"red"` (applies to all)
  - List: `["red", "blue", "green"]` (one per segment)
  - Dict: `{0: "red", 2: "green"}` (specific indices)
  - Tuple keys: `{(0, 2): "red"}` (multiple indices same color)

- **ax** : `matplotlib.axes.Axes`, optional  
  Axes to draw on. If `None`, uses current axes.

- **kwargs** : Additional properties  
  - **Global:** `box_width`, `linespacing`, `ha`, `va`, `transform`, `zorder`
  - **Per-segment:** `fontsize`/`fontsizes`, `fontweight`/`fontweights`, `fontfamily`/`fontfamilies`, etc.
  - Any property can be:
    - Single value (applies to all)
    - List (one per segment, auto-extends)
    - Dict (specific indices)

**Returns:**
- `list of Text` - List of created matplotlib Text objects

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **PyPI:** https://pypi.org/project/mpl-richtext/
- **GitHub:** https://github.com/ra8in/mpl-richtext
- **Issues:** https://github.com/ra8in/mpl-richtext/issues

---

Made with ❤️ for the Matplotlib community