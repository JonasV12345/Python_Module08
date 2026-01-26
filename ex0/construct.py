import sys


def main():
    if sys.base_prefix == sys.prefix:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.version.split()[0]}")
        print("Virtual Enviroment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate      # On Windows")
        print("\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print([p for p in sys.path if "site-packages" in p][0])


if __name__ == "__main__":
    main()
