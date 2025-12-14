# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-12-14

### Added
- Complete chess game implementation with all standard rules
- Move quality scoring system (0-100 scale)
- AI opponent using minimax algorithm with alpha-beta pruning
- Multiple game modes:
  - User vs User
  - User vs AI (White)
  - User vs AI (Black)
  - AI vs AI
- Game mode selection menu
- High-quality drawn chess pieces with shadows and highlights
- Support for custom piece images
- Visual feedback for selected pieces and valid moves
- Real-time game status display (check, checkmate, stalemate)
- Setup scripts for Windows (PowerShell and Batch)
- Run scripts for easy game execution
- Comprehensive test suite
- MIT License
- Contributing guidelines
- Installation documentation

### Features
- Complete chess rules including:
  - Castling (kingside and queenside)
  - En passant capture
  - Pawn promotion
  - Check and checkmate detection
  - Stalemate detection
- Move evaluation based on:
  - Material balance
  - Position quality
  - Move impact (checks, threats)
- Beautiful UI with:
  - Checkerboard pattern
  - Highlighted valid moves
  - Side panel with game information
  - Move score display

### Technical
- Object-oriented architecture
- Modular design with separate classes for:
  - Pieces (6 types)
  - Board management
  - Game logic
  - AI engine
  - Move evaluation
  - Image rendering
- Python 3.7+ compatibility
- Pygame 2.5.0+ for graphics
