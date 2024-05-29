from dataclasses import dataclass
from typing import List

@dataclass
class Artist:
  id: str
  name: str
  genres: List[str]
  popularity: int
  followers: int
  spotify_url: str

@dataclass
class Song:
  id: str
  name: str
  popularity: int
  preview_url: str
