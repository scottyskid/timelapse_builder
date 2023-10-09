from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class Config:
    """ Config object """
    root_folder: Path = Path(os.path.dirname(os.path.abspath(__file__)))
    input_folder: Path = root_folder / "media"
    output_folder: Path = root_folder / "output"
    frame_jump: int = 8
    output_fps: float = 10 # default 29.98
    cropped_x: int = 20 # in pixels
    cropped_width: int = 990 # in pixels
    cropped_y: int = 20 # in pixels
    cropped_height: int = 550 # in pixels
    output_frame_size: tuple[int, int] = (cropped_width, cropped_height)