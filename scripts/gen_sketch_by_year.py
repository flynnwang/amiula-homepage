"""
Usage:

$ cd amiula-homepage/site
$ python3 ../scripts/gen_sketch_by_year.py assets/img/sketch

"""

from collections import defaultdict
from pathlib import Path
import json
import sys


def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <path>")
    sys.exit(1)

  path = sys.argv[1]

  # Define the root directory
  root_dir = Path(path)

  sketch = defaultdict(list)
  # Iterate through all files recursively
  for file in root_dir.rglob('*'):
    if file.is_file():
      if file.suffix not in ('.jpg', '.jpeg'):
        continue

      path = str(file)

      parts = path.split('/')
      year = parts[-2]
      name = '-'.join(parts[-2:])

      sketch[year].append({
          "name": name,
          "url": "/" + path,
      })

  j = {
      "sketch": sketch,
      "sketch_years": list(sketch.keys()),
  }
  print(json.dumps(j, indent=4))


if __name__ == "__main__":
  main()
