"""Programs Rail API client."""

from typing import Any, Optional


class ProgramsRail:
    """Financial programs and schemes management rail."""

    def __init__(self, http_client: Any) -> None:
        self.http = http_client
        self.base_path = "/api/v1/programs"

    def list_programs(self, page: int = 1, limit: int = 20, status: Optional[str] = None) -> dict:
        """List financial programs."""
        params = {"page": page, "limit": limit, "status": status}
        return self.http.get(self.base_path, params=params)

    def get_program(self, program_id: str) -> dict:
        """Get program by ID."""
        return self.http.get(f"{self.base_path}/{program_id}")

    def create_program(self, data: dict) -> dict:
        """Create a new financial program."""
        return self.http.post(self.base_path, json=data)

    def update_program(self, program_id: str, data: dict) -> dict:
        """Update a financial program."""
        return self.http.patch(f"{self.base_path}/{program_id}", json=data)

    def activate_program(self, program_id: str) -> dict:
        """Activate a program."""
        return self.http.post(f"{self.base_path}/{program_id}/activate")

    def deactivate_program(self, program_id: str) -> dict:
        """Deactivate a program."""
        return self.http.post(f"{self.base_path}/{program_id}/deactivate")

    def list_participants(self, program_id: str, page: int = 1, limit: int = 20) -> dict:
        """List participants enrolled in a program."""
        params = {"page": page, "limit": limit}
        return self.http.get(f"{self.base_path}/{program_id}/participants", params=params)

    def enroll_participant(self, program_id: str, data: dict) -> dict:
        """Enroll a participant in a program."""
        return self.http.post(f"{self.base_path}/{program_id}/participants", json=data)

    def get_program_stats(self, program_id: str) -> dict:
        """Get statistics for a program."""
        return self.http.get(f"{self.base_path}/{program_id}/stats")
