"""
Author: Sepehr Bayat | Open Source Chess MVP

Main entry point for the Chess MVP game.
"""

from chess.game import Game


def main():
    """Main function to start the chess game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

