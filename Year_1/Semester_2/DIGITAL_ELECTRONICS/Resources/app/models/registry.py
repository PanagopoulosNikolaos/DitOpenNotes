"""Scenario registry managing available exam papers, practice sets, and theory view."""

from typing import Dict, List, Optional
from models.scenario import Scenario


class ScenarioRegistry:
    """Registry maintaining collection of loaded exam scenarios and navigation options."""

    def __init__(self) -> None:
        """Initializes empty scenario registry."""
        self._scenarios: Dict[str, Scenario] = {}
        self._order: List[str] = []

    def registerScenario(self, scenario: Scenario) -> None:
        """Registers an exam scenario in the registry.

        Args:
            scenario (Scenario): The scenario object to register.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if scenario.id not in self._order:
            self._order.append(scenario.id)

    def getScenario(self, scenario_id: str) -> Optional[Scenario]:
        """Retrieves a registered scenario by unique identifier.

        Args:
            scenario_id (str): Unique identifier of the scenario.

        Returns:
            Optional[Scenario]: Matching Scenario instance or None.
        """
        return self._scenarios.get(scenario_id)

    def getAllScenarios(self) -> List[Scenario]:
        """Returns list of all registered scenarios in registration order.

        Returns:
            List[Scenario]: Ordered list of Scenario objects.
        """
        return [self._scenarios[sid] for sid in self._order]

    def getDefaultScenario(self) -> Optional[Scenario]:
        """Returns the first registered scenario as default.

        Returns:
            Optional[Scenario]: First scenario or None.
        """
        if self._order:
            return self._scenarios[self._order[0]]
        return None

    def getScenarioOptions(self) -> Dict[str, str]:
        """Returns key-value mapping for NiceGUI ui.select dropdown selector.

        Returns:
            Dict[str, str]: Dictionary mapping scenario IDs to display titles.
        """
        options: Dict[str, str] = {}
        for sid in self._order:
            sc = self._scenarios[sid]
            options[sid] = f"{sc.course_tag}: {sc.title}"

        # Dedicated Master Theory Guide entry
        options["theory"] = "Οδηγός Πλήρους Θεωρίας & Αρχιτεκτονικής (100% Κάλυψη)"
        return options


# Global singleton instance
scenario_registry = ScenarioRegistry()

