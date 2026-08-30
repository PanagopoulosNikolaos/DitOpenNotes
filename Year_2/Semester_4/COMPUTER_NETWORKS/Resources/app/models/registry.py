"""Scenario and theory registry management module.

Maintains the catalog of registered Computer Networks scenarios, exam papers,
and theory modules, providing retrieval interfaces for the UI selector.
"""

from typing import Dict, List, Optional
from .scenario import NetworkScenario


class ScenarioRegistry:
    """Registry singleton managing network learning scenarios and theory modules."""

    def __init__(self) -> None:
        """Initializes the scenario registry with an empty catalog."""
        self._scenarios: Dict[str, NetworkScenario] = {}
        self._default_scenario_id: Optional[str] = None

    def registerScenario(self, scenario: NetworkScenario, set_as_default: bool = False) -> None:
        """Registers a scenario in the catalog.

        Args:
            scenario (NetworkScenario): The scenario object containing all analysis data.
            set_as_default (bool): Whether to set this scenario as the initial default.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if set_as_default or self._default_scenario_id is None:
            self._default_scenario_id = scenario.id

    def getScenario(self, scenario_id: str) -> Optional[NetworkScenario]:
        """Retrieves a scenario by its unique identifier.

        Args:
            scenario_id (str): The unique scenario slug.

        Returns:
            Optional[NetworkScenario]: The matching scenario object or None if not found.
        """
        return self._scenarios.get(scenario_id)

    def getDefaultScenario(self) -> Optional[NetworkScenario]:
        """Retrieves the default scenario for initial rendering.

        Returns:
            Optional[NetworkScenario]: The default scenario or None if no scenarios exist.
        """
        if self._default_scenario_id:
            return self._scenarios.get(self._default_scenario_id)
        if self._scenarios:
            return next(iter(self._scenarios.values()))
        return None

    def getAllScenarios(self) -> List[NetworkScenario]:
        """Retrieves all registered scenarios in registration order.

        Returns:
            List[NetworkScenario]: A list of all registered scenarios.
        """
        return list(self._scenarios.values())

    def getScenarioOptions(self) -> Dict[str, str]:
        """Generates key-value dictionary for UI dropdown selectors.

        Returns:
            Dict[str, str]: Mapping from scenario_id to display title.
        """
        options: Dict[str, str] = {}
        # Theory topics
        options["theory_full_prep"] = "[Θεωρία] Πλήρης Οδηγός Προετοιμασίας Εξετάσεων"
        options["topic_1_network_edge"] = "[Θεωρία] Θέμα 1: Δίκτυο στο Έπακρο (Network Edge)"
        options["topic_2_the_internet"] = "[Θεωρία] Θέμα 2: Το Διαδίκτυο & Πρωτόκολλα (Internet & Protocols)"
        options["topic_3_network_structure"] = "[Θεωρία] Θέμα 3: Δομή του Δικτύου (Network Structure)"
        options["topic_4_access_technologies"] = "[Θεωρία] Θέμα 4: Τεχνολογίες Πρόσβασης (Access Technologies)"
        options["topic_5_communication_media"] = "[Θεωρία] Θέμα 5: Μέσα Επικοινωνίας (Communication Media)"
        options["topic_6_data_switching_and_routing"] = "[Θεωρία] Θέμα 6: Μεταγωγή Δεδομένων & Δρομολόγηση"
        options["topic_7_basic_networking_issues"] = "[Θεωρία] Θέμα 7: Βασικά Θέματα Δικτύωσης (Addressing, CRC, Dijkstra)"

        # Registered exam scenarios
        for s in self._scenarios.values():
            options[s.id] = f"[{s.course_tag}] {s.title}"

        return options


# Global singleton registry instance
scenario_registry = ScenarioRegistry()
