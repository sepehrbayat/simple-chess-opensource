# Simple Chess - Open Source

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Author:** Sepehr Bayat

A complete, open-source chess game built with Python and Pygame. Features move quality evaluation, AI opponent with minimax algorithm, and a clean, modular architecture. Perfect for learning chess programming, AI algorithms, and game development.

## 🎮 Features

- **Complete Chess Rules**: All standard chess rules including special moves (castling, en passant, pawn promotion)
- **Move Quality Scoring**: Each move is evaluated and assigned a score from 0-100 based on material balance, position quality, and move impact
- **Visual Feedback**: Highlighted valid moves and selected pieces
- **Game Status**: Real-time display of check, checkmate, and stalemate conditions
- **AI Opponent**: Play against computer with minimax algorithm and alpha-beta pruning
- **Multiple Game Modes**: 
  - User vs User (two players)
  - User vs AI (play as white or black)
  - AI vs AI (watch computer play)
- **High-Quality Piece Graphics**: Beautifully drawn chess pieces with shadows and highlights
- **Custom Piece Images**: Support for custom piece images (falls back to drawn pieces if not available)
- **Clean Architecture**: Object-oriented design with separate classes for pieces, board, game logic, AI, and evaluation

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.5.0 or higher
- PyInstaller 6.0.0 or higher (optional, for building executable)

## 🚀 Installation

### Quick Setup (Windows)

1. **Clone the repository**
   ```bash
   git clone https://github.com/sepehrbayat/simple-chess-opensource.git
   cd simple-chess-opensource
   ```
   
   Or download the ZIP file from the repository page and extract it.

2. **Run the setup script:**
   - **PowerShell**: `.\setup.ps1`
   - **Command Prompt**: `setup.bat`

   This will:
   - Check for Python installation
   - Create a virtual environment
   - Install all dependencies

### Manual Setup

1. **Install Python 3.7+** from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows (PowerShell)**: `.\venv\Scripts\Activate.ps1`
   - **Windows (CMD)**: `venv\Scripts\activate.bat`
   - **Linux/Mac**: `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Running the Game

### Run from Source

**Using the run script:**
- **PowerShell**: `.\run.ps1`
- **Command Prompt**: `run.bat`

**Or manually:**
```bash
python main.py
```

### Build Executable (Windows)

To create a standalone `.exe` file using PyInstaller:

```bash
pyinstaller --onefile --windowed --name ChessMVP main.py
```

The executable will be created in the `dist` folder.

**With icon:**
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name ChessMVP main.py
```

## 🎲 How to Play

1. **Select Game Mode**: When the game starts, choose your preferred game mode:
   - **User vs User**: Play against another person
   - **User vs AI (White)**: You play as white, computer plays as black
   - **User vs AI (Black)**: You play as black, computer plays as white
   - **AI vs AI**: Watch two computer players compete

2. **Select a Piece**: Click on one of your pieces (white moves first)

3. **Make a Move**: Click on a highlighted square to move the selected piece

4. **Move Score**: After each move, the quality score (0-100) is displayed in the side panel

5. **Game Status**: The panel shows the current turn, game status (check/checkmate/stalemate), and move scores

6. **Quit**: Press ESC to exit the game

## 📊 Move Scoring System

The move evaluation system assigns scores based on:

- **Material Balance** (0-90 points): Value of captured pieces
- **Position Quality** (0-20 points): Center control and piece activity
- **Move Impact** (0-15 points): Checks, threats, and strategic value

**Score Interpretation:**
- **81-100**: Excellent move (major capture, check, strong threat)
- **61-80**: Good move (gains material, improves position)
- **31-60**: Neutral move
- **0-30**: Poor move (loses material, weakens position)

## 🤖 AI Engine

The AI uses a minimax algorithm with alpha-beta pruning to find the best moves. The default search depth is 3, which provides a good balance between skill and speed.

## 📁 Project Structure

```
simple-chess-opensource/
├── chess/
│   ├── __init__.py
│   ├── game.py          # Game class (main loop, rendering, menu)
│   ├── board.py         # Board class (grid, state management)
│   ├── pieces.py        # Piece base class + 6 subclasses
│   ├── evaluator.py     # Evaluator class (heuristic scoring)
│   ├── ai.py            # AI engine (minimax algorithm)
│   ├── menu.py          # Game mode selection menu
│   ├── piece_images.py  # Piece image loader and renderer
│   └── constants.py    # Colors, dimensions, Unicode symbols
├── assets/
│   └── README.md        # Instructions for adding custom piece images
├── main.py              # Entry point
├── requirements.txt     # Python dependencies
├── setup.ps1           # PowerShell setup script
├── setup.bat            # Batch setup script
├── run.ps1              # PowerShell run script
├── run.bat              # Batch run script
├── LICENSE              # MIT License
└── README.md           # This file
```

## 🏗️ Architecture

The project uses a modular OOP architecture:

- **Piece Hierarchy**: Base `Piece` class with 6 subclasses (Pawn, Rook, Knight, Bishop, Queen, King)
- **Board**: Manages game state, move validation, and check/checkmate detection
- **Evaluator**: Calculates move quality scores using heuristic evaluation
- **AI Engine**: Implements minimax algorithm with alpha-beta pruning for computer player
- **Game**: Handles Pygame main loop, event handling, UI rendering, and game mode management
- **Menu**: Provides game mode selection interface
- **Piece Images**: Loads custom images or generates high-quality drawn pieces

## 🎨 Custom Piece Images

You can add your own chess piece images to the `assets/` folder. See `assets/README.md` for details.

Required files:
- `wp.png`, `wn.png`, `wb.png`, `wr.png`, `wq.png`, `wk.png` (white pieces)
- `bp.png`, `bn.png`, `bb.png`, `br.png`, `bq.png`, `bk.png` (black pieces)

If images are not provided, the game will use beautifully drawn pieces with shadows and highlights.

## 🧪 Testing

Run the test suite:
```bash
python test_chess.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sepehr Bayat**

## 📦 Version

Current version: **1.0.0**

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## 🙏 Acknowledgments

- Pygame community for the excellent game development library
- Chess.com for inspiration and chess rules reference
- Open source community for continuous support and feedback

## 📞 Contact & Links

**Sepehr Bayat**

- **Repository**: [simple-chess-opensource](https://github.com/sepehrbayat/simple-chess-opensource)
- **Issues**: [Report a Bug](https://github.com/sepehrbayat/simple-chess-opensource/issues)
- **Discussions**: [Join the Discussion](https://github.com/sepehrbayat/simple-chess-opensource/discussions)

---

**Made with ❤️ and Python** | **Enjoy playing Simple Chess!** 🎮♟️
