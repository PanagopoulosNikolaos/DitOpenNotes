"""Scenario registry pattern for managing and querying course exam scenarios.

Provides central lookup, scenario registration, and options list generation
for the main UI selector, including the Master Theory Guide.
"""

from typing import Dict, List, Optional
from models.scenario import Scenario


class ScenarioRegistry:
    """Registry maintaining all loaded exam scenarios and theory modules."""

    def __init__(self) -> None:
        """Initializes empty scenario dictionary and ordered scenario IDs."""
        self._scenarios: Dict[str, Scenario] = {}
        self._ordered_ids: List[str] = []

    def registerScenario(self, scenario: Scenario) -> None:
        """Registers a new scenario in the catalog.

        Args:
            scenario (Scenario): The scenario object to register.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if scenario.id not in self._ordered_ids:
            self._ordered_ids.append(scenario.id)

    def getScenario(self, scenario_id: str) -> Optional[Scenario]:
        """Retrieves a scenario by its unique identifier.

        Args:
            scenario_id (str): The scenario identifier.

        Returns:
            Optional[Scenario]: Found scenario instance or None.
        """
        return self._scenarios.get(scenario_id)

    def getAllScenarios(self) -> List[Scenario]:
        """Returns all registered scenarios in registration order.

        Returns:
            List[Scenario]: Ordered list of scenario objects.
        """
        return [self._scenarios[sid] for sid in self._ordered_ids if sid in self._scenarios]

    def getDefaultScenario(self) -> Optional[Scenario]:
        """Retrieves the default first scenario in the catalog.

        Returns:
            Optional[Scenario]: Default scenario instance or None.
        """
        if self._ordered_ids:
            return self._scenarios.get(self._ordered_ids[0])
        return None

    def getScenarioOptions(self) -> Dict[str, str]:
        """Generates key-value dictionary for the NiceGUI scenario selector dropdown.

        Returns:
            Dict[str, str]: Mapping from scenario ID to human-readable title.
        """
        options: Dict[str, str] = {}
        for sid in self._ordered_ids:
            sc = self._scenarios.get(sid)
            if sc:
                options[sc.id] = f"{sc.course_tag} — {sc.title}"
        # Master theory guide option
        options["theory"] = "Οδηγός Θεωρίας — Θεμελιώδεις Αρχές & Εξισώσεις Maxwell"
        return options


# Global singleton registry instance
scenario_registry = ScenarioRegistry()

