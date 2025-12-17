# Route Planning (A* Search)

Implements A* shortest-path search on provided map graphs.

## Files
- `student_code.py`: A* implementation.
- `helpers.py`: map loader/plot helper (plotly optional).
- `map-10.pickle`, `map-40.pickle`: sample graphs.
- `test.py`: simple correctness tests.

## Running
From this folder:
```bash
python test.py
```
Expected: all tests pass. For manual checks:
```bash
python -c "from helpers import load_map; from student_code import shortest_path; m=load_map('map-40.pickle'); print(shortest_path(m,5,34))"
```

## Notes
- Plotting is optional; if plotly is missing, `show_map` will raise an ImportError.
- A* uses Euclidean distance as an admissible heuristic and set/dict for fast lookups.
