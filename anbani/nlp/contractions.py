import pandas as pd
import os
import re
from pathlib import Path

module_path = Path(__file__).parent.parent.absolute()

cdf = pd.read_csv(os.path.join(module_path, "data/georgian_contractions.csv"))
cmap = cdf.set_index('CONTRACTION')[['EXPANSION']].to_dict('dict')['EXPANSION']

def expand(word):
    # Just a wrapper around contractions map
    if word in cmap:
        return cmap[word]

    return word

def expand_text(text):
    # Sort contractions by length (longest first) to avoid partial matches
    sorted_contractions = sorted(cmap.keys(), key=len, reverse=True)
    
    for contraction in sorted_contractions:
        if contraction in text:
            text = text.replace(contraction, cmap[contraction])
    
    return text
