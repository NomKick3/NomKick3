from enum import Enum
import pygame


class Occupation(Enum):
    """Enum class for representing different states of squares in a grid"""
    NONE = 1
    GOAL = 2
    START = 3
    BLOCKED = 4
    PATH = 5
