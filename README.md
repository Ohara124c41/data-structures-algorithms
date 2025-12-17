# Data Structures & Algorithms (Udacity)

Collection of completed Udacity projects and exercises covering foundational data structures, algorithms, and search.

## Projects

### 1) Data Structures (`data-structures`)
- Problems: LRU cache, file search, Huffman coding, group membership, blockchain, linked list union/intersection.
- Files: `problem_1.py` … `problem_6.py` with tests; `explanation_*.md`; README with run steps.

### 2) Basic Algorithms (`basic-algorithms`)
- Problems: sqrt via binary search, rotated array search, rearrange digits, Dutch flag, trie/suffixes, min/max, HTTP router trie.
- Files: `problem_1.py` … `problem_7.py`, `explanation_*.md`, filled `Trie.ipynb`; README with run steps.

### 3) Route Planning (`route-planning-algorithms`)
- Goal: A* shortest path on provided road graphs.
- Files: `student_code.py`, `helpers.py`, maps, `test.py`; README with run steps. Plotly optional for visualization.

### 4) Unscramble CS Problems (`unscramble-compsci-problems`)
- Tasks 0–4 on call/text datasets; outputs printed per spec; `Analysis.md` with Big-O; README with run steps.

## How to Use

```bash
git clone <repo>
cd data-structures-algorithms
```
- Each project folder has its own README and runnable scripts (Python 3.10+).  
- No external deps beyond stdlib except optional Plotly for route plotting.

## Notes
- Tests for route planning: `python route-planning-algorithms/test.py`.
- Other scripts can be run directly (`python problem_X.py`, `python TaskN.py`).
- Analysis files document time complexity per rubric.
