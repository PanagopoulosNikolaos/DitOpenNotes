"""Registry for Discrete Mathematics scenarios, mock exams, and theory handbook."""

from typing import Dict, List, Optional
from models.scenario import Scenario


class ScenarioRegistry:
    """Manages registered exam scenarios and theory view options."""

    def __init__(self) -> None:
        """Initializes empty scenario dictionary."""
        self._scenarios: Dict[str, Scenario] = {}
        self._order: List[str] = []

    def registerScenario(self, scenario: Scenario) -> None:
        """Registers a scenario object into the registry.

        Args:
            scenario (Scenario): The scenario instance to register.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if scenario.id not in self._order:
            self._order.append(scenario.id)

    def getScenario(self, scenario_id: str) -> Optional[Scenario]:
        """Retrieves a scenario by unique identifier.

        Args:
            scenario_id (str): Unique identifier of the scenario.

        Returns:
            Optional[Scenario]: Matching scenario or None.
        """
        return self._scenarios.get(scenario_id)

    def getAllScenarios(self) -> List[Scenario]:
        """Returns list of all registered scenarios in registration order.

        Returns:
            List[Scenario]: Registered scenarios.
        """
        return [self._scenarios[sid] for sid in self._order if sid in self._scenarios]

    def getScenarioOptions(self) -> Dict[str, str]:
        """Returns dictionary of scenario IDs to display titles for NiceGUI ui.select.

        Returns:
            Dict[str, str]: Map of scenario IDs to user-friendly titles.
        """
        options: Dict[str, str] = {}
        for sid in self._order:
            sc = self._scenarios[sid]
            options[sid] = f"{sc.course_tag} — {sc.title}"

        # Dedicated Master Theory Guide entry
        options["theory"] = "Πλήρης Οδηγός Θεωρίας (100% Exam Scope)"
        return options

    def getDefaultScenario(self) -> Optional[Scenario]:
        """Returns the default scenario for initial page load.

        Returns:
            Optional[Scenario]: First scenario in registry.
        """
        if self._order:
            return self._scenarios.get(self._order[0])
        return None


# Global registry singleton instance
scenario_registry = ScenarioRegistry()
