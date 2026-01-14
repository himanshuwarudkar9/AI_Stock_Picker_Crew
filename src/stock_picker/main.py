#!/usr/bin/env python
import datetime
import warnings
import sys
from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'sector': 'Technology sector in India',
    }
    
    result = StockPicker().crew().kickoff(inputs=inputs)
    print("\n\n==FINAL DECISION==\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()
    