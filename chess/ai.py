"""
Author: Sepehr Bayat | Open Source Chess MVP

AI Engine for computer player using minimax algorithm with alpha-beta pruning.
"""

import random
from typing import Tuple, List, Optional
from chess.board import Board
from chess.evaluator import Evaluator


class ChessAI:
    """AI engine for playing chess using minimax algorithm."""
    
    def __init__(self, depth: int = 3):
        """
        Initialize the AI.
        
        Args:
            depth: Search depth for minimax algorithm (default: 3)
        """
        self.depth = depth
        self.evaluator = Evaluator()
    
    def get_best_move(self, board: Board, color: str) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """
        Get the best move for the given color using minimax.
        
        Args:
            board: Current board state
            color: Color to play ('white' or 'black')
            
        Returns:
            Best move as ((start_row, start_col), (end_row, end_col)) or None if no moves available
        """
        moves = board.get_all_moves(color)
        if not moves:
            return None
        
        # Use minimax with alpha-beta pruning
        best_move = None
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        
        # Shuffle moves for variety
        random.shuffle(moves)
        
        for move in moves:
            # Make the move on a copy
            test_board = board.copy()
            start, end = move
            test_board.make_move(start, end)
            
            # Evaluate the move
            score = self._minimax(test_board, self.depth - 1, alpha, beta, False, color)
            
            if score > best_score:
                best_score = score
                best_move = move
            
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Alpha-beta pruning
        
        return best_move if best_move else moves[0]  # Fallback to first move
    
    def _minimax(self, board: Board, depth: int, alpha: float, beta: float, 
                 maximizing: bool, ai_color: str) -> float:
        """
        Minimax algorithm with alpha-beta pruning.
        
        Args:
            board: Current board state
            depth: Remaining search depth
            alpha: Best value for maximizing player
            beta: Best value for minimizing player
            maximizing: True if maximizing (AI's turn), False if minimizing (opponent's turn)
            ai_color: Color the AI is playing
            
        Returns:
            Evaluation score
        """
        # Terminal conditions
        if depth == 0:
            return self._evaluate_board(board, ai_color)
        
        current_color = ai_color if maximizing else ('black' if ai_color == 'white' else 'white')
        moves = board.get_all_moves(current_color)
        
        if not moves:
            # No moves available - check if checkmate or stalemate
            if board.is_in_check(current_color):
                return float('-inf') if maximizing else float('inf')  # Checkmate
            else:
                return 0  # Stalemate
        
        if maximizing:
            max_score = float('-inf')
            for move in moves:
                test_board = board.copy()
                test_board.make_move(move[0], move[1])
                score = self._minimax(test_board, depth - 1, alpha, beta, False, ai_color)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            return max_score
        else:
            min_score = float('inf')
            for move in moves:
                test_board = board.copy()
                test_board.make_move(move[0], move[1])
                score = self._minimax(test_board, depth - 1, alpha, beta, True, ai_color)
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            return min_score
    
    def _evaluate_board(self, board: Board, color: str) -> float:
        """
        Evaluate the board position for the given color.
        
        Args:
            board: Board state to evaluate
            color: Color to evaluate for
            
        Returns:
            Evaluation score (positive is better for the color)
        """
        # Material balance
        material = self.evaluator.calculate_material_balance(board, color)
        
        # Position score
        position = self.evaluator.calculate_position_score(board, color)
        
        # Check/checkmate bonus/penalty
        check_bonus = 0
        opponent_color = 'black' if color == 'white' else 'white'
        if board.is_in_check(opponent_color):
            if board.is_checkmate(opponent_color):
                check_bonus = 1000  # Checkmate is very good
            else:
                check_bonus = 50  # Check is good
        
        if board.is_in_check(color):
            if board.is_checkmate(color):
                check_bonus = -1000  # Being checkmated is very bad
            else:
                check_bonus = -25  # Being in check is bad
        
        return material + position + check_bonus
