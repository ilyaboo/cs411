from typing import Any, Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:

    def __init__(self) -> None:
        self.migration_id: int
        self.current_location: str
        self.start_date: str
        self.start_location: Habitat
        self.species: str
        self.age: Optional[int] = None
        self.status: str = "Scheduled"
        self.destination: Habitat
        self.animals: List[int] = []
        self.duration: Optional[int] = None
