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
    output_fps: float = 29.98
    output_frame_size: tuple[int, int] = (1280, 720)