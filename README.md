# 🂡 Command-Line Blackjack

A fun, interactive Blackjack (21) game you can play right in your terminal!

## 🎮 How to Play
- Try to get your cards as close to 21 as possible without going over.
- You and the dealer get 2 cards.
- Choose to **Hit (H)** to draw a card or **Stand (S)** to end your turn.
- Dealer reveals their hidden card and plays automatically.
- Closest to 21 without busting wins!

## 🕹️ Controls
- `P` — Play a new game
- `H` — Show instructions
- `Q` — Quit
- During game:
  - `H` — Hit (draw a card)
  - `S` — Stand (end your turn)

## 🛠️ Features
- ASCII Art for card visuals 🃏
- Colorful terminal output using `chromafy`
- Smart Ace handling (1 or 11)
- Dealer AI that plays by the rules

## 📦 Dependencies
- `keyboard`
- `chromafy` (custom module for styling output)
- `cards` (custom module for card visuals and logic)

Make sure these are in the same folder, or install dependencies via pip if available.

## 🚀 Running the Game
```bash
python main.py
