"""
Basic usage examples for mpl-richtext
"""

import matplotlib.pyplot as plt
from mpl_richtext import richtext

# Create figure
fig = plt.figure(figsize=(12, 8))
fig.suptitle('mpl-richtext Examples', fontsize=20, fontweight='bold')

# Example 1: Basic multi-color text
ax1 = plt.subplot(3, 2, 1)
richtext(0.5, 0.5,
         strings=["hello", ", ", "world"],
         colors=["red", "blue", "green"],
         ax=ax1, fontsize=18, ha='center', transform=ax1.transAxes)
ax1.set_title('Basic Multi-Color', loc='left', fontweight='bold')
ax1.axis('off')

# Example 2: Error message style
ax2 = plt.subplot(3, 2, 2)
richtext(0.1, 0.5,
         strings=["ERROR: ", "File not found"],
         colors=["red", "black"],
         ax=ax2, fontsize=14, fontweight='bold', transform=ax2.transAxes)
ax2.set_title('Styled Messages', loc='left', fontweight='bold')
ax2.axis('off')

# Example 3: Mixed font sizes
ax3 = plt.subplot(3, 2, 3)
richtext(0.5, 0.5,
         strings=["BIG", " medium ", "small"],
         colors=["red", "blue", "green"],
         fontsizes=[30, 18, 12],
         ax=ax3, ha='center', transform=ax3.transAxes)
ax3.set_title('Mixed Font Sizes', loc='left', fontweight='bold')
ax3.axis('off')

# Example 4: Code syntax highlighting
ax4 = plt.subplot(3, 2, 4)
richtext(0.1, 0.5,
         strings=["def ", "hello", "(", "name", "):"],
         colors=["blue", "green", "black", "orange", "black"],
         ax=ax4, fontsize=14, fontfamily='monospace', transform=ax4.transAxes)
ax4.set_title('Syntax Highlighting', loc='left', fontweight='bold')
ax4.axis('off')

# Example 5: Rainbow colors
ax5 = plt.subplot(3, 2, 5)
rainbow = ["red", "orange", "gold", "green", "blue", "indigo", "violet"]
richtext(0.5, 0.5,
         strings=list("Rainbow"),
         colors=rainbow,
         ax=ax5, fontsize=20, fontweight='bold', ha='center', transform=ax5.transAxes)
ax5.set_title('Rainbow Text', loc='left', fontweight='bold')
ax5.axis('off')

# Example 6: Dictionary-based coloring
ax6 = plt.subplot(3, 2, 6)
richtext(0.5, 0.5,
         strings=["One ", "Two ", "Three ", "Four"],
         colors={0: "red", 2: "green"},
         ax=ax6, fontsize=16, ha='center', transform=ax6.transAxes)
ax6.set_title('Dictionary Colors', loc='left', fontweight='bold')
ax6.axis('off')

plt.tight_layout()
plt.savefig('mpl_richtext_examples.png', dpi=150, bbox_inches='tight')
print("Examples saved as 'mpl_richtext_examples.png'")