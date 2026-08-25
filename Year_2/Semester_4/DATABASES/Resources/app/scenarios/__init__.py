"""Scenarios package initialization and auto-registration."""

from models.registry import scenario_registry
from .research_institute import createResearchInstituteScenario
from .university_portal import createUniversityPortalScenario


def initializeScenarios() -> None:
    """Instantiates and registers all available scenarios into the registry."""
    # Register Scenario 1 (Default)
    research_scenario = createResearchInstituteScenario()
    scenario_registry.registerScenario(research_scenario, set_as_default=True)

    # Register Scenario 2
    university_scenario = createUniversityPortalScenario()
    scenario_registry.registerScenario(university_scenario, set_as_default=False)


# Auto-initialize on import
initializeScenarios()

__all__ = [
    "createResearchInstituteScenario",
    "createUniversityPortalScenario",
    "initializeScenarios",
]
