"""Registry module managing Study (Notes & Guides) and Exams (Papers & Solutions).

Maintains catalogs for the two primary modules:
1. Study Module: Course theory topics, full exam prep cheat sheets, and calculators.
2. Exams Module: Past exam papers and synthetic realistic exams with step-by-step solutions.
"""

from typing import Dict, List, Optional
from .scenario import NetworkScenario


class ScenarioRegistry:
    """Registry singleton managing Study sub-modules and Exam scenario sub-modules."""

    def __init__(self) -> None:
        """Initializes the registry catalogs."""
        self._scenarios: Dict[str, NetworkScenario] = {}
        self._default_exam_id: Optional[str] = "exam_past_2023_2024"
        self._default_study_id: str = "theory_full_prep"

    def registerScenario(self, scenario: NetworkScenario, set_as_default: bool = False) -> None:
        """Registers an exam scenario in the catalog.

        Args:
            scenario (NetworkScenario): The scenario object containing questions and topology.
            set_as_default (bool): Whether to set this scenario as the initial default exam.

        Returns:
            None
        """
        self._scenarios[scenario.id] = scenario
        if set_as_default or self._default_exam_id is None:
            self._default_exam_id = scenario.id

    def getScenario(self, scenario_id: str) -> Optional[NetworkScenario]:
        """Retrieves an exam scenario by its unique identifier.

        Args:
            scenario_id (str): The unique scenario slug.

        Returns:
            Optional[NetworkScenario]: The matching scenario object or None.
        """
        return self._scenarios.get(scenario_id)

    def getDefaultExamScenario(self) -> Optional[NetworkScenario]:
        """Retrieves the default exam scenario for initial rendering.

        Returns:
            Optional[NetworkScenario]: The default scenario.
        """
        if self._default_exam_id:
            return self._scenarios.get(self._default_exam_id)
        if self._scenarios:
            return next(iter(self._scenarios.values()))
        return None

    def getAllScenarios(self) -> List[NetworkScenario]:
        """Retrieves all registered exam scenarios.

        Returns:
            List[NetworkScenario]: List of all registered exam scenarios.
        """
        return list(self._scenarios.values())

    def getStudyOptions(self) -> Dict[str, str]:
        """Generates key-value dictionary for Study sub-modules dropdown.

        Returns:
            Dict[str, str]: Mapping from study sub-module ID to display title.
        """
        return {
            "theory_full_prep": "Πλήρης Οδηγός Προετοιμασίας Εξετάσεων (Cheat Sheet)",
            "topic_1_network_edge": "Θέμα 1: Δίκτυο στο Έπακρο (Network Edge & P2P)",
            "topic_2_the_internet": "Θέμα 2: Το Διαδίκτυο & Πρωτόκολλα (OSI vs TCP/IP)",
            "topic_3_network_structure": "Θέμα 3: Δομή του Δικτύου (ISPs, IXPs, Peering)",
            "topic_4_access_technologies": "Θέμα 4: Τεχνολογίες Πρόσβασης (DSL, FTTH, 5G)",
            "topic_5_communication_media": "Θέμα 5: Μέσα Επικοινωνίας (UTP, Οπτικές Ίνες, LEO)",
            "topic_6_data_switching_and_routing": "Θέμα 6: Μεταγωγή Δεδομένων & 4 Καθυστερήσεις",
            "topic_7_basic_networking_issues": "Θέμα 7: Διευθυνσιοδότηση, ARP, Dijkstra, CRC",
            "study_calculators": "Διαδραστικοί Υπολογιστές (Delays, CRC, Subnetting)",
        }

    def getExamOptions(self) -> Dict[str, str]:
        """Generates key-value dictionary for Exams sub-modules dropdown.

        Returns:
            Dict[str, str]: Mapping from exam scenario ID to display title.
        """
        options: Dict[str, str] = {}
        for s in self._scenarios.values():
            options[s.id] = f"[{s.course_tag}] {s.title}"
        return options

    def getScenarioOptions(self) -> Dict[str, str]:
        """Generates unified key-value dictionary for all application options.

        Returns:
            Dict[str, str]: Combined mapping of study topics and exams.
        """
        options: Dict[str, str] = {}
        for k, v in self.getStudyOptions().items():
            options[k] = f"[Study] {v}"
        for k, v in self.getExamOptions().items():
            options[k] = f"[Exam] {v}"
        return options


# Global singleton registry instance
scenario_registry = ScenarioRegistry()
