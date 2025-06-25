# 🔤 Boggle Solver (Backwards)

A Python project that "cheats" at Boggle by flipping the usual solving strategy: instead of scanning the board for words, it scans the dictionary for words that can be found _on_ the board.

![YouTube Video](https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube)

> 🔗 [Watch the full walkthrough on YouTube](https://www.youtube.com/watch?v=-qAZig2l_vs)

---

## ✨ What It Does

This tool loads a Boggle board (like the one used in the BSDGames terminal version) and checks every word in a dictionary to see if it can be formed on the board using Boggle rules.

It doesn't use tries, prefix trees, or forward board search. Just a good old fashioned word by word check.

---

## 🔍 Highlights

- Reverse solving approach: **dictionary → board**
- Recursive path search for each word
- Works with standard `/usr/share/dict/words`
- Compatible with terminal-based Boggle (e.g., BSDGames)

---

## 🧰 Technologies Used

- Python 3
- Standard Library: `sys`, `typing`, `os`, `argparse`
- Linux dictionary file (`/usr/share/dict/words`)

---

## 🚀 Getting Started

### 🔧 Run It

Clone the repo and run the solver on a given board:

```bash
python3 boggle.py <board> <dictionary>
```

The solver will check every dictionary word against the board and print all matches.

---

## 📚 External Resources

- [BSD Boggle Game (man page)](https://manpages.debian.org/stretch/bsdgames/boggle.6)
- [Backtracking in Python](https://realpython.com/python-thinking-recursively/)
- [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)

---

## 🙌 Acknowledgments

Inspired by those moments in Boggle where you wish you had superpowers or a Python script.
