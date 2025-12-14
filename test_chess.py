"""
Author: Sepehr Bayat | Open Source Chess MVP

Simple test script to verify the chess game components work correctly.
"""

import sys

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports...")
    try:
        from chess import constants
        print("[OK] constants imported")
        
        from chess.pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King
        print("[OK] pieces imported")
        
        from chess.board import Board
        print("[OK] board imported")
        
        from chess.evaluator import Evaluator
        print("[OK] evaluator imported")
        
        from chess.game import Game
        print("[OK] game imported")
        
        from chess.ai import ChessAI
        print("[OK] AI imported")
        
        from chess.menu import GameMenu
        print("[OK] menu imported")
        
        from chess.piece_images import PieceImageLoader
        print("[OK] piece_images imported")
        
        return True
    except Exception as e:
        print(f"[ERROR] Import error: {e}")
        return False

def test_board_initialization():
    """Test that board initializes correctly."""
    print("\nTesting board initialization...")
    try:
        from chess.board import Board
        board = Board()
        
        # Check that pieces are placed
        assert board.get_piece(7, 4) is not None, "White king should be at e1"
        assert board.get_piece(0, 4) is not None, "Black king should be at e8"
        assert board.get_piece(7, 4).piece_type == 'king', "Should be a king"
        assert board.get_piece(7, 4).color == 'white', "Should be white"
        
        print("[OK] Board initialized correctly")
        return True
    except Exception as e:
        print(f"[ERROR] Board initialization error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_piece_moves():
    """Test that pieces can generate valid moves."""
    print("\nTesting piece moves...")
    try:
        from chess.board import Board
        board = Board()
        
        # Test pawn moves
        pawn = board.get_piece(6, 0)  # White pawn
        assert pawn is not None, "Pawn should exist"
        moves = pawn.get_valid_moves(board)
        assert len(moves) > 0, "Pawn should have valid moves"
        print(f"[OK] Pawn has {len(moves)} valid moves")
        
        # Test knight moves
        knight = board.get_piece(7, 1)  # White knight
        assert knight is not None, "Knight should exist"
        moves = knight.get_valid_moves(board)
        assert len(moves) > 0, "Knight should have valid moves"
        print(f"[OK] Knight has {len(moves)} valid moves")
        
        return True
    except Exception as e:
        print(f"[ERROR] Piece moves error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_move_execution():
    """Test that moves can be executed."""
    print("\nTesting move execution...")
    try:
        from chess.board import Board
        board = Board()
        
        # Make a simple pawn move
        result = board.make_move((6, 0), (5, 0))
        assert result, "Move should succeed"
        assert board.get_piece(5, 0) is not None, "Piece should be at new position"
        assert board.get_piece(6, 0) is None, "Old position should be empty"
        assert board.current_turn == 'black', "Turn should switch to black"
        
        print("[OK] Move executed correctly")
        return True
    except Exception as e:
        print(f"[ERROR] Move execution error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_evaluator():
    """Test that evaluator works."""
    print("\nTesting evaluator...")
    try:
        from chess.board import Board
        from chess.evaluator import Evaluator
        
        board = Board()
        evaluator = Evaluator()
        
        # Evaluate a move
        move = ((6, 0), (5, 0))
        score = evaluator.evaluate_move(board, move, 'white')
        
        assert 0 <= score <= 100, f"Score should be 0-100, got {score}"
        print(f"[OK] Evaluator returned score: {score}/100")
        
        return True
    except Exception as e:
        print(f"[ERROR] Evaluator error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("Chess MVP Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_board_initialization,
        test_piece_moves,
        test_move_execution,
        test_evaluator,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"[ERROR] Test {test.__name__} crashed: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Tests passed: {passed}/{len(tests)}")
    print(f"Tests failed: {failed}/{len(tests)}")
    print("=" * 50)
    
    if failed == 0:
        print("\n[SUCCESS] All tests passed!")
        return 0
    else:
        print("\n[FAILED] Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())

