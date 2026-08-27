"""Scenario registry and dynamic management module.

Maintains the catalog of registered database design scenarios and provides
retrieval and registration interfaces.
"""

from typing import Dict, List, Optional
from .scenario import Scenario


class ScenarioRegistry:
    """Registry class for managing database analysis scenarios."""

    def __init__(self) -> None:
        """Initializes the scenario registry with an empty scenario mapping."""
        self._scenarios: Dict[str, Scenario] = {}
        self._default_scenario_id: Optional[str] = None

    def registerScenario(self, scenario: Scenario, set_as_default: bool = False) -> None:
        """Registers a scenario in the catalog.

        Args:
            scenario (Scenario): The scenario object containing all analysis data.
            set_as_default (bool): Whether to set this scenario as the initial default.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if set_as_default or self._default_scenario_id is None:
            self._default_scenario_id = scenario.id

    def getScenario(self, scenario_id: str) -> Optional[Scenario]:
        """Retrieves a scenario by its unique identifier.

        Args:
            scenario_id (str): The unique scenario slug.

        Returns:
            Optional[Scenario]: The matching scenario object or None if not found.
        """
        return self._scenarios.get(scenario_id)

    def getDefaultScenario(self) -> Optional[Scenario]:
        """Retrieves the default scenario for initial rendering.

        Returns:
            Optional[Scenario]: The default scenario or None if no scenarios are registered.
        """
        if self._default_scenario_id:
            return self._scenarios.get(self._default_scenario_id)
        if self._scenarios:
            return next(iter(self._scenarios.values()))
        return None

    def getAllScenarios(self) -> List[Scenario]:
        """Retrieves all registered scenarios in registration order.

        Returns:
            List[Scenario]: A list of all registered scenarios.
        """
        return list(self._scenarios.values())

    def getScenarioOptions(self) -> Dict[str, str]:
        """Generates key-value dictionary for UI dropdown selectors.

        Returns:
            Dict[str, str]: Mapping from scenario_id to title, ending with the theory guide.
        """
        options = {s.id: f"{s.title} ({s.course_tag})" for s in self._scenarios.values()}
        options["theory"] = "Θεωρία & Μεθοδολογία ER (Οδηγός Crow's Foot)"
        return options



# Global singleton registry instance
scenario_registry = ScenarioRegistry()
