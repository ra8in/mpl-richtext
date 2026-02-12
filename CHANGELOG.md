# Changelog

All notable changes to mpl-richtext will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-02-12

### Added

- **Index-Based Styling API**: New cleaner syntax for specifying all text properties per segment
  - Pass styles as dict: `{0: {'color': 'red', 'size': 20, 'weight': 'bold'}}`
  - Supports both named parameter (`styles=`) and positional (4th parameter)
  - Auto-detection of dict-of-dicts vs dict-of-strings
  
- **Property Aliases**: User-friendly short names for common properties
  - `weight` → `fontweight`
  - `size` → `fontsize`
  - `family` → `fontfamily`
  - `style` → `fontstyle`
  
- **Flexible API Mixing**: Combine global defaults, property dicts, and styles dict
  - Clear priority order: styles dict > individual kwargs > global defaults
  - Full backward compatibility with existing code
  
- **Enhanced Documentation**: 
  - Comprehensive README with Nepali/Devanagari support section
  - Examples showing old vs new API
  - Property alias documentation

### Changed

- Enhanced `richtext()` function signature with `styles` parameter
- Updated `_normalize_properties()` to support styles dict and property aliases
- Improved docstrings with detailed parameter documentation

### Technical

- Added auto-detection logic for positional styles dict
- Implemented property name normalization for aliases
- Added comprehensive test suite (`tests/test_styles_api.py`)
- All tests passing (7/7 verification tests)

## [0.1.7] - Previous Release

- Initial stable release
- Multi-color and multi-style text support
- HarfBuzz integration for complex scripts (Nepali/Devanagari)
- Word wrapping, alignment, decorations
- Rotation and transparency support

---

[0.2.0]: https://github.com/ra8in/mpl-richtext/compare/v0.1.7...v0.2.0
[0.1.7]: https://github.com/ra8in/mpl-richtext/releases/tag/v0.1.7
