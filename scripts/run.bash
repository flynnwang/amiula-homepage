set -e

python3 scripts/gen_sketch.py docs/assets/img/sketch > docs/_data/sketch.json
python3 scripts/gen_sketch_by_year.py docs/assets/img/sketch > docs/_data/sketch_by_year.json
