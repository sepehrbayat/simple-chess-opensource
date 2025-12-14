"""
Author: Sepehr Bayat | Open Source Chess MVP

Piece image loader and renderer.
Falls back to high-quality drawn chess pieces if images are not available.
"""

import pygame
import os
import math
from typing import Optional, Dict
from pathlib import Path
from chess.constants import SQUARE_SIZE


class PieceImageLoader:
    """Loads and manages chess piece images."""
    
    def __init__(self):
        """Initialize the image loader."""
        self.images: Dict[str, pygame.Surface] = {}
        self.use_images = False
        self.assets_dir = Path(__file__).parent.parent / "assets"
        self._load_images()
    
    def _load_images(self):
        """Load piece images from assets directory."""
        piece_mapping = {
            'wp.png': 'pawn_white',
            'wn.png': 'knight_white',
            'wb.png': 'bishop_white',
            'wr.png': 'rook_white',
            'wq.png': 'queen_white',
            'wk.png': 'king_white',
            'bp.png': 'pawn_black',
            'bn.png': 'knight_black',
            'bb.png': 'bishop_black',
            'br.png': 'rook_black',
            'bq.png': 'queen_black',
            'bk.png': 'king_black',
        }
        
        # Try to load images
        for filename, key in piece_mapping.items():
            image_path = self.assets_dir / filename
            if image_path.exists():
                try:
                    img = pygame.image.load(str(image_path))
                    # Scale to fit square size
                    img = pygame.transform.scale(img, (int(SQUARE_SIZE * 0.85), int(SQUARE_SIZE * 0.85)))
                    self.images[key] = img
                    self.use_images = True
                except Exception as e:
                    print(f"Warning: Could not load {image_path}: {e}")
        
        # If we have at least some images, use images
        if len(self.images) > 0:
            self.use_images = True
            print(f"Loaded {len(self.images)} piece images")
        else:
            print("No piece images found, using high-quality drawn chess pieces")
    
    def get_piece_image(self, piece_type: str, color: str) -> Optional[pygame.Surface]:
        """
        Get the image for a piece.
        
        Args:
            piece_type: Type of piece ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
            color: Color of piece ('white' or 'black')
            
        Returns:
            Pygame surface with piece image, or None if not available
        """
        if not self.use_images:
            return None
        
        # Map to our internal key format
        piece_key = f"{piece_type}_{color}"
        return self.images.get(piece_key)
    
    def create_simple_image(self, piece_type: str, color: str) -> pygame.Surface:
        """
        Create a high-quality, detailed chess piece image using pygame drawing.
        This draws realistic-looking chess pieces with better detail.
        
        Args:
            piece_type: Type of piece
            color: Color of piece
            
        Returns:
            Pygame surface with drawn piece
        """
        size = int(SQUARE_SIZE * 0.9)
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        center_x, center_y = size // 2, size // 2
        
        # Enhanced color scheme with gradients
        if color == 'white':
            piece_color = (255, 255, 255)
            piece_color_light = (255, 255, 255)
            piece_color_dark = (240, 240, 240)
            outline_color = (0, 0, 0)
            shadow_color = (180, 180, 180)
            highlight_color = (255, 255, 255)
        else:
            piece_color = (20, 20, 20)
            piece_color_light = (40, 40, 40)
            piece_color_dark = (10, 10, 10)
            outline_color = (255, 255, 255)
            shadow_color = (5, 5, 5)
            highlight_color = (60, 60, 60)
        
        # Draw piece based on type
        if piece_type == 'pawn':
            self._draw_pawn_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light, 
                                    piece_color_dark, outline_color, shadow_color, highlight_color)
        elif piece_type == 'rook':
            self._draw_rook_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light,
                                    piece_color_dark, outline_color, shadow_color, highlight_color)
        elif piece_type == 'knight':
            self._draw_knight_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light,
                                      piece_color_dark, outline_color, shadow_color, highlight_color)
        elif piece_type == 'bishop':
            self._draw_bishop_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light,
                                      piece_color_dark, outline_color, shadow_color, highlight_color)
        elif piece_type == 'queen':
            self._draw_queen_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light,
                                     piece_color_dark, outline_color, shadow_color, highlight_color)
        elif piece_type == 'king':
            self._draw_king_enhanced(surface, center_x, center_y, size, piece_color, piece_color_light,
                                     piece_color_dark, outline_color, shadow_color, highlight_color)
        
        return surface
    
    def _draw_pawn_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced pawn piece with better detail."""
        base_radius = size * 0.28
        body_top = size * 0.15
        body_bottom = size * 0.55
        head_radius = size * 0.18
        neck_width = size * 0.12
        
        # Shadow
        pygame.draw.circle(surface, shadow, (cx + 2, cy + size * 0.38), base_radius + 3)
        
        # Base (larger and more prominent)
        pygame.draw.circle(surface, dark, (cx, cy + size * 0.38), base_radius)
        pygame.draw.circle(surface, color, (cx, cy + size * 0.38), base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy + size * 0.38), base_radius, 3)
        
        # Body (more rounded, better proportions)
        body_points = [
            (cx - neck_width, cy - body_top),
            (cx - base_radius * 0.7, cy + body_bottom * 0.3),
            (cx - base_radius * 0.9, cy + body_bottom * 0.6),
            (cx, cy + body_bottom),
            (cx + base_radius * 0.9, cy + body_bottom * 0.6),
            (cx + base_radius * 0.7, cy + body_bottom * 0.3),
            (cx + neck_width, cy - body_top),
        ]
        pygame.draw.polygon(surface, dark, body_points)
        pygame.draw.polygon(surface, color, [(p[0], p[1] - 2) for p in body_points])
        pygame.draw.polygon(surface, outline, body_points, 3)
        
        # Head (larger and rounder)
        pygame.draw.circle(surface, dark, (cx, cy - body_top * 0.5), head_radius)
        pygame.draw.circle(surface, color, (cx, cy - body_top * 0.5), head_radius - 2)
        pygame.draw.circle(surface, highlight, (cx - head_radius * 0.3, cy - body_top * 0.5 - head_radius * 0.3), head_radius * 0.3)
        pygame.draw.circle(surface, outline, (cx, cy - body_top * 0.5), head_radius, 3)
    
    def _draw_rook_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced rook (castle) piece."""
        base_width = size * 0.55
        base_height = size * 0.18
        body_width = size * 0.4
        body_height = size * 0.55
        top_height = size * 0.22
        battlement_width = body_width * 0.22
        battlement_height = top_height * 0.7
        
        # Shadow
        shadow_rect = pygame.Rect(cx - base_width // 2 + 2, cy + size * 0.32 + 2, base_width, base_height)
        pygame.draw.rect(surface, shadow, shadow_rect)
        
        # Base
        base_rect = pygame.Rect(cx - base_width // 2, cy + size * 0.32, base_width, base_height)
        pygame.draw.rect(surface, dark, base_rect)
        pygame.draw.rect(surface, color, pygame.Rect(cx - base_width // 2 + 2, cy + size * 0.32 + 2, 
                                                     base_width - 4, base_height - 4))
        pygame.draw.rect(surface, outline, base_rect, 3)
        
        # Body
        body_rect = pygame.Rect(cx - body_width // 2, cy - body_height * 0.15, body_width, body_height)
        pygame.draw.rect(surface, dark, body_rect)
        pygame.draw.rect(surface, color, pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                                     body_width - 4, body_height - 4))
        pygame.draw.rect(surface, outline, body_rect, 3)
        
        # Top platform
        top_rect = pygame.Rect(cx - body_width // 2, cy - size * 0.38, body_width, top_height)
        pygame.draw.rect(surface, dark, top_rect)
        pygame.draw.rect(surface, color, pygame.Rect(cx - body_width // 2 + 2, cy - size * 0.38 + 2,
                                                    body_width - 4, top_height - 4))
        pygame.draw.rect(surface, outline, top_rect, 3)
        
        # Battlements (4 distinct rectangles)
        for i in range(4):
            x_offset = (i - 1.5) * body_width * 0.3
            battlement_rect = pygame.Rect(cx - battlement_width // 2 + x_offset,
                                        cy - size * 0.38, battlement_width, battlement_height)
            pygame.draw.rect(surface, outline, battlement_rect, 2)
            # Highlight on battlements
            pygame.draw.rect(surface, highlight, pygame.Rect(cx - battlement_width // 2 + x_offset + 1,
                                                            cy - size * 0.38 + 1,
                                                            battlement_width - 2, 3))
    
    def _draw_knight_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced knight (horse) piece."""
        base_radius = size * 0.28
        body_width = size * 0.45
        
        # Shadow
        pygame.draw.circle(surface, shadow, (cx + 2, cy + size * 0.38), base_radius + 3)
        
        # Base
        pygame.draw.circle(surface, dark, (cx, cy + size * 0.38), base_radius)
        pygame.draw.circle(surface, color, (cx, cy + size * 0.38), base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy + size * 0.38), base_radius, 3)
        
        # Enhanced horse body with more detail
        points = [
            (cx - body_width * 0.35, cy + size * 0.28),  # Bottom left
            (cx - body_width * 0.45, cy + size * 0.1),  # Left body
            (cx - body_width * 0.4, cy - size * 0.05),  # Left shoulder
            (cx - body_width * 0.25, cy - size * 0.2),  # Left neck
            (cx - body_width * 0.1, cy - size * 0.32),  # Lower neck
            (cx + body_width * 0.05, cy - size * 0.38),  # Head base
            (cx + body_width * 0.2, cy - size * 0.35),  # Head top
            (cx + body_width * 0.3, cy - size * 0.28),  # Head right
            (cx + body_width * 0.35, cy - size * 0.15),  # Right neck
            (cx + body_width * 0.4, cy - size * 0.05),  # Right shoulder
            (cx + body_width * 0.35, cy + size * 0.1),  # Right body
            (cx + body_width * 0.25, cy + size * 0.2),  # Right back
            (cx, cy + size * 0.28),  # Bottom center
        ]
        
        # Draw with shadow
        shadow_points = [(p[0] + 2, p[1] + 2) for p in points]
        pygame.draw.polygon(surface, shadow, shadow_points)
        
        # Draw main body
        pygame.draw.polygon(surface, dark, points)
        # Highlight
        highlight_points = [(p[0] - 2, p[1] - 2) for p in points[:7]]
        pygame.draw.polygon(surface, highlight, highlight_points)
        pygame.draw.polygon(surface, outline, points, 3)
        
        # Eye (more prominent)
        eye_size = 4
        pygame.draw.circle(surface, outline, (cx + body_width * 0.15, cy - size * 0.32), eye_size)
        pygame.draw.circle(surface, (255, 255, 255) if color == (20, 20, 20) else (0, 0, 0),
                         (cx + body_width * 0.15, cy - size * 0.32), eye_size - 2)
        
        # Mane detail
        mane_points = [
            (cx - body_width * 0.2, cy - size * 0.25),
            (cx - body_width * 0.15, cy - size * 0.3),
            (cx - body_width * 0.1, cy - size * 0.28),
        ]
        pygame.draw.lines(surface, outline, False, mane_points, 2)
    
    def _draw_bishop_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced bishop piece."""
        base_radius = size * 0.28
        body_width = size * 0.32
        body_height = size * 0.5
        head_radius = size * 0.14
        cross_width = size * 0.18
        cross_thickness = size * 0.04
        
        # Shadow
        pygame.draw.circle(surface, shadow, (cx + 2, cy + size * 0.38), base_radius + 3)
        
        # Base
        pygame.draw.circle(surface, dark, (cx, cy + size * 0.38), base_radius)
        pygame.draw.circle(surface, color, (cx, cy + size * 0.38), base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy + size * 0.38), base_radius, 3)
        
        # Body (more tapered)
        body_rect = pygame.Rect(cx - body_width // 2, cy - body_height * 0.15, body_width, body_height)
        pygame.draw.ellipse(surface, dark, body_rect)
        pygame.draw.ellipse(surface, color, pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                                        body_width - 4, body_height - 4))
        # Highlight on body
        highlight_rect = pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                     body_width - 4, body_height // 3)
        pygame.draw.ellipse(surface, highlight, highlight_rect)
        pygame.draw.ellipse(surface, outline, body_rect, 3)
        
        # Head
        pygame.draw.circle(surface, dark, (cx, cy - size * 0.22), head_radius)
        pygame.draw.circle(surface, color, (cx, cy - size * 0.22), head_radius - 2)
        pygame.draw.circle(surface, highlight, (cx - head_radius * 0.3, cy - size * 0.22 - head_radius * 0.3),
                          head_radius * 0.3)
        pygame.draw.circle(surface, outline, (cx, cy - size * 0.22), head_radius, 3)
        
        # Cross on top (more prominent)
        cross_rect1 = pygame.Rect(cx - cross_width // 2, cy - size * 0.36, cross_width, cross_thickness)
        cross_rect2 = pygame.Rect(cx - cross_thickness // 2, cy - size * 0.42, cross_thickness, cross_width * 0.6)
        pygame.draw.rect(surface, dark, cross_rect1)
        pygame.draw.rect(surface, dark, cross_rect2)
        pygame.draw.rect(surface, outline, cross_rect1, 2)
        pygame.draw.rect(surface, outline, cross_rect2, 2)
    
    def _draw_queen_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced queen piece."""
        base_radius = size * 0.28
        body_width = size * 0.38
        body_height = size * 0.55
        crown_base_radius = size * 0.12
        crown_point_radius = size * 0.08
        
        # Shadow
        pygame.draw.circle(surface, shadow, (cx + 2, cy + size * 0.38), base_radius + 3)
        
        # Base
        pygame.draw.circle(surface, dark, (cx, cy + size * 0.38), base_radius)
        pygame.draw.circle(surface, color, (cx, cy + size * 0.38), base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy + size * 0.38), base_radius, 3)
        
        # Body
        body_rect = pygame.Rect(cx - body_width // 2, cy - body_height * 0.15, body_width, body_height)
        pygame.draw.ellipse(surface, dark, body_rect)
        pygame.draw.ellipse(surface, color, pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                                        body_width - 4, body_height - 4))
        # Highlight
        highlight_rect = pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                     body_width - 4, body_height // 3)
        pygame.draw.ellipse(surface, highlight, highlight_rect)
        pygame.draw.ellipse(surface, outline, body_rect, 3)
        
        # Crown base
        pygame.draw.circle(surface, dark, (cx, cy - size * 0.22), crown_base_radius)
        pygame.draw.circle(surface, color, (cx, cy - size * 0.22), crown_base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy - size * 0.22), crown_base_radius, 3)
        
        # Crown with 5 distinct points
        for i in range(5):
            angle = (i * 2 * math.pi / 5) - math.pi / 2
            x = cx + (crown_base_radius * 1.4) * math.cos(angle)
            y = cy - size * 0.22 + (crown_base_radius * 1.4) * math.sin(angle)
            # Draw point
            pygame.draw.circle(surface, dark, (int(x), int(y)), crown_point_radius)
            pygame.draw.circle(surface, color, (int(x), int(y)), crown_point_radius - 1)
            pygame.draw.circle(surface, outline, (int(x), int(y)), crown_point_radius, 2)
            # Highlight on points
            highlight_x = int(x - crown_point_radius * 0.3)
            highlight_y = int(y - crown_point_radius * 0.3)
            pygame.draw.circle(surface, highlight, (highlight_x, highlight_y), crown_point_radius * 0.4)
    
    def _draw_king_enhanced(self, surface, cx, cy, size, color, light, dark, outline, shadow, highlight):
        """Draw an enhanced king piece."""
        base_radius = size * 0.28
        body_width = size * 0.38
        body_height = size * 0.55
        head_radius = size * 0.14
        cross_width = size * 0.22
        cross_thickness = size * 0.05
        
        # Shadow
        pygame.draw.circle(surface, shadow, (cx + 2, cy + size * 0.38), base_radius + 3)
        
        # Base
        pygame.draw.circle(surface, dark, (cx, cy + size * 0.38), base_radius)
        pygame.draw.circle(surface, color, (cx, cy + size * 0.38), base_radius - 2)
        pygame.draw.circle(surface, outline, (cx, cy + size * 0.38), base_radius, 3)
        
        # Body
        body_rect = pygame.Rect(cx - body_width // 2, cy - body_height * 0.15, body_width, body_height)
        pygame.draw.ellipse(surface, dark, body_rect)
        pygame.draw.ellipse(surface, color, pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                                       body_width - 4, body_height - 4))
        # Highlight
        highlight_rect = pygame.Rect(cx - body_width // 2 + 2, cy - body_height * 0.15 + 2,
                                     body_width - 4, body_height // 3)
        pygame.draw.ellipse(surface, highlight, highlight_rect)
        pygame.draw.ellipse(surface, outline, body_rect, 3)
        
        # Head
        pygame.draw.circle(surface, dark, (cx, cy - size * 0.22), head_radius)
        pygame.draw.circle(surface, color, (cx, cy - size * 0.22), head_radius - 2)
        pygame.draw.circle(surface, highlight, (cx - head_radius * 0.3, cy - size * 0.22 - head_radius * 0.3),
                          head_radius * 0.3)
        pygame.draw.circle(surface, outline, (cx, cy - size * 0.22), head_radius, 3)
        
        # King's cross (more prominent and detailed)
        cross_rect1 = pygame.Rect(cx - cross_width // 2, cy - size * 0.38, cross_width, cross_thickness)
        cross_rect2 = pygame.Rect(cx - cross_thickness // 2, cy - size * 0.45, cross_thickness, cross_width * 0.7)
        
        # Draw cross with depth
        pygame.draw.rect(surface, dark, cross_rect1)
        pygame.draw.rect(surface, dark, cross_rect2)
        pygame.draw.rect(surface, color, pygame.Rect(cx - cross_width // 2 + 1, cy - size * 0.38 + 1,
                                                    cross_width - 2, cross_thickness - 2))
        pygame.draw.rect(surface, color, pygame.Rect(cx - cross_thickness // 2 + 1, cy - size * 0.45 + 1,
                                                    cross_thickness - 2, cross_width * 0.7 - 2))
        # Highlight on cross
        pygame.draw.rect(surface, highlight, pygame.Rect(cx - cross_width // 2 + 1, cy - size * 0.38 + 1,
                                                       cross_width - 2, 2))
        pygame.draw.rect(surface, highlight, pygame.Rect(cx - cross_thickness // 2 + 1, cy - size * 0.45 + 1,
                                                        cross_thickness - 2, 2))
        pygame.draw.rect(surface, outline, cross_rect1, 2)
        pygame.draw.rect(surface, outline, cross_rect2, 2)
