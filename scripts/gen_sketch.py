"""
Usage:

$ cd amiula-homepage/site
$ python3 ../scripts/gen_sketch.py assets/img/sketch

"""

from pathlib import Path
import json
import os
import sys

IMGIX_BASE = "https://amiula.imgix.net/"


def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <path>")
    sys.exit(1)

  path = sys.argv[1]

  # Define the root directory
  root_dir = Path(path)

  sketch = []
  # Iterate through all files recursively
  for file in root_dir.rglob('*'):
    if file.is_file():
      if file.suffix not in ('.jpg', '.jpeg'):
        continue

      path = str(file)

      parts = path.split('/')
      name = '-'.join(parts[-2:])
      imgix_url = os.path.join(IMGIX_BASE, "/".join(parts[3:]))

      sketch.append({
          "name": name,
          # "url": "/" + path,
          "url": imgix_url,
      })

  j = {"sketch": sketch}
  print(json.dumps(j, indent=4))


if __name__ == "__main__":
  main()
