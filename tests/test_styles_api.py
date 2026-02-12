"""
Tests for the styles parameter API and property aliases.
"""
import pytest
import matplotlib.pyplot as plt
from mpl_richtext import richtext


class TestStylesParameter:
    """Test the new styles parameter."""
    
    def test_styles_basic(self):
        """Test basic styles dict usage."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["Hello", " ", "World"],
            styles={
                0: {'color': 'red', 'fontsize': 20},
                2: {'color': 'blue', 'fontsize': 30}
            },
            ax=ax
        )
        assert len(result) == 3
        assert result[0].get_color() == 'red'
        assert result[0].get_fontsize() == 20
        assert result[2].get_color() == 'blue'
        assert result[2].get_fontsize() == 30
        plt.close(fig)
    
    def test_styles_with_aliases(self):
        """Test property name aliases (weight, size, etc.)."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["Bold", "Normal"],
            styles={
                0: {'weight': 'bold', 'size': 24},
                1: {'weight': 'normal', 'size': 12}
            },
            ax=ax
        )
        assert result[0].get_weight() == 'bold'
        assert result[0].get_fontsize() == 24
        assert result[1].get_weight() == 'normal'
        assert result[1].get_fontsize() == 12
        plt.close(fig)
    
    def test_styles_with_global_defaults(self):
        """Test styles dict with global kwargs as defaults."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B", "C"],
            styles={0: {'color': 'red'}},
            fontsize=20,  # Global default
            ax=ax
        )
        assert result[0].get_color() == 'red'
        assert result[0].get_fontsize() == 20  # From styles OR global
        # Segments 1 and 2 should get global defaults
        assert result[1].get_fontsize() == 20
        assert result[2].get_fontsize() == 20
        plt.close(fig)
    
    def test_styles_mixed_with_colors(self):
        """Test styles parameter combined with colors parameter."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B", "C"],
            colors=['green', 'green', 'green'],  # Base colors
            styles={1: {'color': 'red', 'fontsize': 30}},  # Override segment 1
            fontsize=20,
            ax=ax
        )
        assert result[0].get_color() == 'green'
        assert result[0].get_fontsize() == 20
        assert result[1].get_color() == 'red'  # styles takes precedence
        assert result[1].get_fontsize() == 30
        assert result[2].get_color() == 'green'
        plt.close(fig)
    
    def test_styles_complete_example(self):
        """Test a complete realistic example with styles."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["TechCorp Inc.", " (General Public)"],
            styles={
                0: {'fontsize': 11, 'weight': 'bold', 'color': '#2C4A6E'},
                1: {'fontsize': 8, 'weight': 'normal', 'color': '#556B2F'}
            },
            ax=ax,
            ha='center', 
            va='center'
        )
        assert len(result) == 2
        assert result[0].get_color() == '#2C4A6E'
        assert result[0].get_fontsize() == 11
        assert result[0].get_weight() == 'bold'
        assert result[1].get_color() == '#556B2F'
        assert result[1].get_fontsize() == 8
        assert result[1].get_weight() == 'normal'
        plt.close(fig)
    
    def test_backward_compatibility_without_styles(self):
        """Ensure existing API still works without styles parameter."""
        fig, ax = plt.subplots()
        # Old API - should work exactly as before
        result = richtext(
            0.5, 0.5,
            ["A", "B"],
            colors={0: 'red', 1: 'blue'},
            fontsizes={0: 20, 1: 30},
            ax=ax
        )
        assert result[0].get_color() == 'red'
        assert result[0].get_fontsize() == 20
        assert result[1].get_color() == 'blue'
        assert result[1].get_fontsize() == 30
        plt.close(fig)
    
    def test_styles_priority_over_kwargs(self):
        """Test that styles dict has higher priority than individual kwargs."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B"],
            colors={0: 'green', 1: 'green'},  # Lower priority
            fontsizes={0: 15, 1: 15},
            styles={0: {'color': 'red', 'size': 25}},  # Higher priority
            ax=ax
        )
        # Segment 0: styles should override
        assert result[0].get_color() == 'red'
        assert result[0].get_fontsize() == 25
        # Segment 1: no styles, use kwargs
        assert result[1].get_color() == 'green'
        assert result[1].get_fontsize() == 15
        plt.close(fig)
    
    def test_tuple_keys_in_styles(self):
        """Test tuple keys to apply same styles to multiple indices."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B", "C", "D", "E"],
            styles={(0, 2, 4): {'color': 'red', 'size': 20, 'weight': 'bold'}},
            ax=ax
        )
        # Indices 0, 2, 4 should be red/20/bold
        assert result[0].get_color() == 'red'
        assert result[0].get_fontsize() == 20
        assert result[0].get_weight() == 'bold'
        
        assert result[2].get_color() == 'red'
        assert result[2].get_fontsize() == 20
        
        assert result[4].get_color() == 'red'
        assert result[4].get_fontsize() == 20
        
        # Indices 1, 3 should not be affected
        assert result[1].get_color() != 'red'
        assert result[3].get_color() != 'red'
        plt.close(fig)


class TestPropertyAliases:
    """Test property name alias normalization."""
    
    def test_all_aliases(self):
        """Test all supported aliases."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["Test"],
            styles={0: {
                'weight': 'bold',
                'size': 20,
                'family': 'monospace',
                'style': 'italic'
            }},
            ax=ax
        )
        assert result[0].get_weight() == 'bold'
        assert result[0].get_fontsize() == 20
        assert result[0].get_family()[0] == 'monospace'
        assert result[0].get_style() == 'italic'
        plt.close(fig)
    
    def test_aliases_mixed_with_standard(self):
        """Test mixing aliases and standard names."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B"],
            styles={
                0: {'size': 20, 'color': 'red'},  # alias + standard
                1: {'fontsize': 30, 'weight': 'bold'}  # standard + alias
            },
            ax=ax
        )
        assert result[0].get_fontsize() == 20
        assert result[0].get_color() == 'red'
        assert result[1].get_fontsize() == 30
        assert result[1].get_weight() == 'bold'
        plt.close(fig)


class TestFlexibleAPI:
    """Test the flexible combination of old and new APIs."""
    
    def test_all_three_approaches_combined(self):
        """Test combining global defaults, property kwargs, and styles dict."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B", "C", "D"],
            fontsize=10,  # Global default
            colors={1: 'blue'},  # Individual property targeting
            styles={2: {'color': 'green', 'size': 25}},  # Complete specification
            ax=ax
        )
        # A: global defaults
        assert result[0].get_fontsize() == 10
        # B: global + individual override
        assert result[1].get_fontsize() == 10
        assert result[1].get_color() == 'blue'
        # C: styles dict
        assert result[2].get_fontsize() == 25
        assert result[2].get_color() == 'green'
        # D: global defaults
        assert result[3].get_fontsize() == 10
        plt.close(fig)
    
    def test_empty_styles_dict(self):
        """Test that empty styles dict doesn't break anything."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B"],
            styles={},  # Empty
            color='red',
            ax=ax
        )
        assert result[0].get_color() == 'red'
        assert result[1].get_color() == 'red'
        plt.close(fig)
    
    def test_styles_none(self):
        """Test that styles=None works (backward compat)."""
        fig, ax = plt.subplots()
        result = richtext(
            0.5, 0.5,
            ["A", "B"],
            styles=None,
            color='red',
            ax=ax
        )
        assert result[0].get_color() == 'red'
        assert result[1].get_color() == 'red'
        plt.close(fig)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
