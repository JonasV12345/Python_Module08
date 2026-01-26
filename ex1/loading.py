import sys
import importlib


def main():
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies")
    diction = {"pandas": "Data manipulation ready",
               "matplotlib": "Visualization ready",
               "requests": "Network ready", "numpy": "raw signals"}
    for name, last_name in diction.items():
        try:
            module = importlib.import_module(name)
            print(f"[OK] {module.__name__}"
                  f"{getattr(module, '__version__', 'Unkown')} -  {last_name}")
        except (ImportError, AttributeError):
            print(f"Missing dependency: {name}\n"
                  "Please install it using 'pip install requests'")
            sys.exit(1)
    print()
    create_matrix()


def create_matrix():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data..")
    data = np.random.standard_normal(1000)
    print("Processsing 1000 data points...")
    # 1. Create the DataFrame
    df = pd.DataFrame(data, columns=['Signal'])
    df['Moving_Average'] = df['Signal'].rolling(window=10).mean()
    plt.plot(data)
    plt.plot(df['Moving_Average'], color='red', label='Filtered')
    print("Generating visualization")
    print()
    plt.title("Matrix Analysis")
    plt.savefig("matrix_analysis.png")
    print("Analysis complite!")
    print("Results saved to: matix_analysis.png")


if __name__ == "__main__":
    main()
