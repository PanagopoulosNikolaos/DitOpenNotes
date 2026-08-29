"""Scenarios package initialization and auto-registration."""

from models.registry import scenario_registry
from .past_exam_1_educational_institution import createPastExam1Scenario
from .past_exam_2_research_institute import createResearchInstituteScenario
from .university_portal import createUniversityPortalScenario
from .synth_exam_1_hospital import createHospitalManagementScenario
from .synth_exam_2_maritime_shipping import createMaritimeShippingScenario
from .synth_exam_3_airline import createAirlineManagementScenario
from .synth_exam_4_banking import createBankingManagementScenario
from .synth_exam_5_hotel import createHotelManagementScenario
from .synth_exam_6_streaming import createStreamingPlatformScenario
from .synth_exam_7_library import createLibraryManagementScenario
from .synth_exam_8_sports_league import createSportsLeagueScenario


def initializeScenarios() -> None:
    """Instantiates and registers all available scenarios into the registry."""
    # Register Scenario 1 (Default)
    research_scenario = createResearchInstituteScenario()
    scenario_registry.registerScenario(research_scenario, set_as_default=True)

    # Register Past Exam 1 Scenario
    past_exam_1_scenario = createPastExam1Scenario()
    scenario_registry.registerScenario(past_exam_1_scenario, set_as_default=False)

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

    # Register Scenario 9: Municipal Library Network (Exam Paper 7)
    library_scenario = createLibraryManagementScenario()
    scenario_registry.registerScenario(library_scenario, set_as_default=False)

    # Register Scenario 10: Sports League Federation (Exam Paper 8)
    sports_scenario = createSportsLeagueScenario()
    scenario_registry.registerScenario(sports_scenario, set_as_default=False)


# Auto-initialize on import
initializeScenarios()

__all__ = [
    "createResearchInstituteScenario",
    "createPastExam1Scenario",
    "createUniversityPortalScenario",
    "createHospitalManagementScenario",
    "createMaritimeShippingScenario",
    "createAirlineManagementScenario",
    "createBankingManagementScenario",
    "createHotelManagementScenario",
    "createStreamingPlatformScenario",
    "createLibraryManagementScenario",
    "createSportsLeagueScenario",
    "initializeScenarios",
]
