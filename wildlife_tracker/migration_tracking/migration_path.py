from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self) -> None:
        self.path_id: int

    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_path_by_id(self, path_id: int) -> MigrationPath:
        pass

    def get_migration_paths(self) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_destination(self, destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(self, species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(self, start_location: Habitat) -> list[MigrationPath]:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass

    def remove_migration_path(self, path_id: int) -> None:
        pass


    