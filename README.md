# mpl-richtext

**Rich text rendering for Matplotlib** - Create beautiful multi-color, multi-style text in a single line.

[![PyPI version](https://badge.fury.io/py/mpl-richtext.svg)](https://pypi.org/project/mpl-richtext/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Why mpl-richtext?

Standard Matplotlib only supports single-color text. To create multi-colored text, you need to manually position each piece and calculate spacing - tedious and error-prone!

**mpl-richtext** solves this by letting you specify colors and styles for each text segment in one simple function call.

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

## Examples

### Basic Multi-Color Text

```python
from mpl_richtext import richtext
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
richtext(0.5, 0.5,
         strings=["Error: ", "File not found"],
         colors=["red", "black"],
         ax=ax, fontsize=16, fontweight='bold',
         transform=ax.transAxes)
plt.show()
```

### Mixed Font Sizes

```python
richtext(0.5, 0.5,
         strings=["BIG", " medium ", "small"],
         colors=["red", "blue", "green"],
         fontsizes=[30, 20, 10],
         ax=ax, transform=ax.transAxes)
```

### Code Syntax Highlighting Style

```python
richtext(0.1, 0.5,
         strings=["def ", "greet", "(", "name", "):"],
         colors=["blue", "green", "black", "orange", "black"],
         ax=ax, fontsize=14, fontfamily='monospace',
         transform=ax.transAxes)
```

### Dictionary-Based Coloring

```python
# Color only specific indices
richtext(0.5, 0.5,
         strings=["One ", "Two ", "Three ", "Four"],
         colors={0: "red", 2: "green"},  # Only color 1st and 3rd
         ax=ax, fontsize=18, transform=ax.transAxes)
```

### Word Wrapping

```python
words = ["This ", "is ", "a ", "long ", "sentence ", "that ", 
         "will ", "wrap ", "automatically."]
colors = ["red", "blue", "green"] * 3

richtext(1, 5, 
         strings=words,
         colors=colors,
         box_width=5.0,  # Enable wrapping
         ax=ax, fontsize=14)
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

## Advanced Usage

### Plural Properties

```python
# Use plural form for per-segment properties
richtext(0.5, 0.5,
         strings=["A", "B", "C"],
         colors=["red", "blue", "green"],
         fontsizes=[20, 25, 30],        # Different sizes
         fontweights=["normal", "bold", "light"],  # Different weights
         ax=ax, transform=ax.transAxes)
```

### Property Extension

```python
# Provide fewer colors than segments - last color repeats
richtext(0.5, 0.5,
         strings=["One", "Two", "Three", "Four", "Five"],
         colors=["red", "blue"],  # "blue" extends to remaining segments
         ax=ax, transform=ax.transAxes)
```

### Alignment Options

```python
# Center-aligned text block
richtext(0.5, 0.5,
         strings=["Centered ", "text"],
         colors=["red", "blue"],
         ha='center',  # Horizontal alignment
         va='center',  # Vertical alignment
         ax=ax, transform=ax.transAxes)
```

## Real-World Use Cases

- 🎯 **Syntax highlighting** in code examples
- 📊 **Colorful annotations** on plots
- ⚠️ **Styled error/warning messages**
- 🎨 **Creative titles and labels**
- 📈 **Data visualization callouts**
- 🎓 **Educational diagrams**

## Requirements

- Python >= 3.8
- Matplotlib >= 3.5.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for easier multi-styled text in Matplotlib
- Built on top of the excellent Matplotlib library

## Links

- **Documentation:** [Coming soon]
- **PyPI:** https://pypi.org/project/mpl-richtext/
- **GitHub:** https://github.com/yourusername/mpl-richtext
- **Issues:** https://github.com/yourusername/mpl-richtext/issues

## Support

If you find this library useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📖 Improving documentation

---

Made with ❤️ for the Matplotlib community