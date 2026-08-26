"""Scenarios package initialization and auto-registration."""

from models.registry import scenario_registry
from .research_institute import createResearchInstituteScenario
from .university_portal import createUniversityPortalScenario
from .hospital_management import createHospitalManagementScenario
from .maritime_shipping import createMaritimeShippingScenario
from .airline_management import createAirlineManagementScenario
from .banking_management import createBankingManagementScenario
from .hotel_management import createHotelManagementScenario
from .streaming_platform import createStreamingPlatformScenario


def initializeScenarios() -> None:
    """Instantiates and registers all available scenarios into the registry."""
    # Register Scenario 1 (Default)
    research_scenario = createResearchInstituteScenario()
    scenario_registry.registerScenario(research_scenario, set_as_default=True)

    # Register Scenario 2: University Portal
    university_scenario = createUniversityPortalScenario()
    scenario_registry.registerScenario(university_scenario, set_as_default=False)

    # Register Scenario 3: Hospital Management (Exam Paper 1)
    hospital_scenario = createHospitalManagementScenario()
    scenario_registry.registerScenario(hospital_scenario, set_as_default=False)

    # Register Scenario 4: Maritime Shipping (Exam Paper 2)
    maritime_scenario = createMaritimeShippingScenario()
    scenario_registry.registerScenario(maritime_scenario, set_as_default=False)

    # Register Scenario 5: Airline Operations (Exam Paper 3)
    airline_scenario = createAirlineManagementScenario()
    scenario_registry.registerScenario(airline_scenario, set_as_default=False)

    # Register Scenario 6: Banking Management (Exam Paper 4)
    banking_scenario = createBankingManagementScenario()
    scenario_registry.registerScenario(banking_scenario, set_as_default=False)

    # Register Scenario 7: Hotel Resort Management (Exam Paper 5)
    hotel_scenario = createHotelManagementScenario()
    scenario_registry.registerScenario(hotel_scenario, set_as_default=False)

    # Register Scenario 8: Streaming Platform (Exam Paper 6)
    streaming_scenario = createStreamingPlatformScenario()
    scenario_registry.registerScenario(streaming_scenario, set_as_default=False)


# Auto-initialize on import
initializeScenarios()

__all__ = [
    "createResearchInstituteScenario",
    "createUniversityPortalScenario",
    "createHospitalManagementScenario",
    "createMaritimeShippingScenario",
    "createAirlineManagementScenario",
    "createBankingManagementScenario",
    "createHotelManagementScenario",
    "createStreamingPlatformScenario",
    "initializeScenarios",
]
