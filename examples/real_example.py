import matplotlib.pyplot as plt
from mpl_richtext import richtext
import numpy as np

def create_comprehensive_example():
    # Set up the figure with subplots
    fig = plt.figure(figsize=(12, 10))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1.2])
    
    # 1. Syntax Highlighting Example
    ax1 = fig.add_subplot(gs[0, :])
    ax1.set_title("1. Syntax Highlighting Simulation", pad=20, fontsize=14, fontweight='bold')
    ax1.axis('off')
    
    code_lines = [
        (["def ", "calculate_metrics", "(", "data", ", ", "threshold", "=0.5):"],
         ["#cc7832", "#ffc66d", "#a9b7c6", "#a9b7c6", "#cc7832", "#a9b7c6", "#6897bb"]),
        
        (["    ", "if ", "data", ".max() > ", "threshold", ":"],
         ["", "#cc7832", "#a9b7c6", "#a9b7c6", "#a9b7c6", "#cc7832"]),
        
        (["        ", "return ", "True"],
         ["", "#cc7832", "#cc7832"]),
         
        (["    ", "return ", "False"],
         ["", "#cc7832", "#cc7832"])
    ]
    
    y_pos = 0.8
    for strings, colors in code_lines:
        richtext(0.1, y_pos, strings, colors, ax=ax1, 
                 fontfamily='monospace', fontsize=14, 
                 bbox=dict(facecolor='#2b2b2b', alpha=1, pad=10, boxstyle='round'))
        y_pos -= 0.2

    # 2. Rich Text Annotations on Plot
    ax2 = fig.add_subplot(gs[1, 0])
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax2.plot(x, y, color='#444444')
    ax2.set_title("2. Rich Annotations", pad=10, fontsize=12)
    
    # Peak annotation
    peak_idx = np.argmax(y)
    richtext(x[peak_idx], y[peak_idx] + 0.2,
             strings=["Max Value: ", f"{y[peak_idx]:.2f}"],
             colors=["black", "red"],
             fontweights=["normal", "bold"],
             ha='center', va='bottom', ax=ax2)
    
    # Trough annotation
    trough_idx = np.argmin(y)
    richtext(x[trough_idx], y[trough_idx] - 0.2,
             strings=["Min Value: ", f"{y[trough_idx]:.2f}"],
             colors=["black", "blue"],
             fontweights=["normal", "bold"],
             ha='center', va='top', ax=ax2)

    # 3. Complex Formatting
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.axis('off')
    ax3.set_title("3. Complex Formatting", pad=10, fontsize=12)
    
    richtext(0.5, 0.5,
             strings=["Big ", "Bold ", "& ", "Colorful"],
             colors=["#FF5733", "#33FF57", "#3357FF", "#F333FF"],
             fontsizes=[24, 20, 18, 22],
             fontweights=["bold", "heavy", "light", "bold"],
             fontfamilies=["sans-serif", "serif", "cursive", "monospace"],
             ha='center', va='center', ax=ax3)

    # 4. Word Wrapping Example
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')
    ax4.set_title("4. Automatic Word Wrapping", pad=10, fontsize=12)
    
    long_text = ["mpl-richtext ", "makes ", "it ", "easy ", "to ", "create ", 
                 "beautiful ", "multi-colored ", "text ", "layouts ", "with ", 
                 "automatic ", "wrapping ", "capabilities. ", "Perfect ", "for ", 
                 "creating ", "complex ", "annotations ", "and ", "labels!"]
    
    colors = ["#333333"] * len(long_text)
    # Highlight specific words
    for i, word in enumerate(long_text):
        if word.strip() in ["beautiful", "multi-colored", "wrapping"]:
            colors[i] = "#E91E63"
            
    richtext(0.5, 0.8,
             strings=long_text,
             colors=colors,
             box_width=8.0,
             ha='center', va='top',
             fontsize=16,
             ax=ax4)

    plt.tight_layout()
    plt.savefig('examples/mpl_richtext_showcase.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_comprehensive_example()
