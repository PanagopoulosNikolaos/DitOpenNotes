"""Past Exam 2023-2024 Scenario Module.

Contains all multiple choice questions, network delay calculations,
ARP tables, RIP routing configurations, and collision/broadcast domain analysis.
"""

from models.scenario import (
    NetworkScenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    QuestionOption,
    CalculationStep,
    TopologyNode,
    TopologyLink,
)


def createScenario() -> NetworkScenario:
    """Constructs and returns the complete Past Exam 2023-2024 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="In the final examination for the course "),
                TextSegment(
                    text="Computer Networks (Academic Year 2023-2024)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="EXAM",
                    tooltip="Official exam paper from the Department of Informatics & Telecommunications",
                ),
                TextSegment(text=", students are required to answer multiple-choice questions and analytical problems covering "),
                TextSegment(
                    text="data transmission modes (Simplex, Duplex)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="COMMUNICATION",
                    tooltip="Data flow directionality and transmission timing",
                ),
                TextSegment(text=", operations of physical and data link layer devices such as "),
                TextSegment(
                    text="Repeater (Physical Layer)",
                    is_highlight=True,
                    category="device",
                    tag_label="L1 DEVICE",
                    tooltip="Regenerates bit signals without inspecting frames",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="Bridge (Data Link Layer)",
                    is_highlight=True,
                    category="device",
                    tag_label="L2 DEVICE",
                    tooltip="Connects LAN segments and isolates collision domains",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The practical section examines the operation of the "),
                TextSegment(
                    text="Address Resolution Protocol (ARP)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ARP L2/L3",
                    tooltip="Mapping logical IP addresses to physical MAC addresses",
                ),
                TextSegment(text=" through the transmission of an "),
                TextSegment(
                    text="ARP Request as Broadcast",
                    is_highlight=True,
                    category="routing",
                    tag_label="BROADCAST",
                    tooltip="Broadcast transmission to destination FF:FF:FF:FF:FF:FF",
                ),
                TextSegment(text=" and an "),
                TextSegment(
                    text="ARP Reply as Unicast",
                    is_highlight=True,
                    category="routing",
                    tag_label="UNICAST",
                    tooltip="Direct MAC delivery back to the querying host",
                ),
                TextSegment(text=", along with configuring "),
                TextSegment(
                    text="RIP v2 Routing",
                    is_highlight=True,
                    category="routing",
                    tag_label="ROUTING PROTOCOL",
                    tooltip="Distance-Vector protocol using hop count as metric",
                ),
                TextSegment(text=" and analyzing "),
                TextSegment(
                    text="Collision & Broadcast Domains",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="Demarcation of collision and broadcast domains",
                ),
                TextSegment(text=" across bus and star topologies."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Data Transmission Modes on a Channel",
            question_type="Multiple Choice",
            prompt_text="Which of the following is **not** a data transmission mode regarding communication directionality and timing?",
            options=[
                QuestionOption("A", "Simplex", False, "Simplex is unidirectional communication (e.g. broadcast radio)."),
                QuestionOption("B", "Multiplexing", True, "Multiplexing is a technique for combining multiple signals over a shared medium, not a directional mode of data exchange."),
                QuestionOption("C", "Half-duplex", False, "Half-duplex enables bidirectional communication but not simultaneously (e.g. walkie-talkie)."),
                QuestionOption("D", "Full duplex", False, "Full-duplex enables simultaneous bidirectional communication (e.g. telephone lines, modern switched Ethernet)."),
            ],
            correct_option_letter="B",
            detailed_justification="Simplex, half-duplex, and full-duplex describe the directionality and timing of transmission across a channel. Multiplexing (FDM, TDM, WDM) is a medium-sharing method.",
        ),
        ExamQuestion(
            question_number=2,
            title="Repeater Layer of Operation",
            question_type="Multiple Choice",
            prompt_text="At which layer of the OSI model does a Repeater operate?",
            options=[
                QuestionOption("A", "Physical layer (Layer 1)", True, "A repeater operates strictly at the Physical Layer (Layer 1), regenerating and amplifying electrical or optical signals."),
                QuestionOption("B", "Data link layer (Layer 2)", False, "Switches and bridges operate at Layer 2."),
                QuestionOption("C", "Network layer (Layer 3)", False, "Routers operate at Layer 3."),
                QuestionOption("D", "Transport layer (Layer 4)", False, "Transport protocols like TCP and UDP operate at Layer 4."),
            ],
            correct_option_letter="A",
            detailed_justification="A repeater has no awareness of MAC addresses or IP packets. Its sole purpose is signal regeneration for bits degraded over physical distance.",
        ),
        ExamQuestion(
            question_number=3,
            title="ARP Protocol Operation & ARP Cache",
            question_type="Theory Analysis",
            prompt_text="Suppose host A wishes to communicate with host C on the same local subnet. Analyze the transmission type of the ARP Request, the ARP Reply, and the behavior of the ARP Cache if a second frame is sent after 5 minutes.",
            detailed_justification=(
                "1. **ARP Request:** Sent as a **Broadcast** (destination MAC: `FF:FF:FF:FF:FF:FF`). All nodes in the local subnet receive and inspect it.\n"
                "2. **ARP Reply:** The target host with the requested IP responds via **Unicast** directly to host A, using host A's MAC address learned from the request header.\n"
                "3. **Subsequent transmission after 5 minutes:** No ARP Request is sent. The IP-to-MAC mapping is cached in host A's local **ARP Cache** (standard cache timeout is 15-20 minutes)."
            ),
            common_pitfalls=[
                "Assuming that the ARP Reply is broadcast (it is always Unicast).",
                "Overlooking the presence and lifetime of the local ARP Cache.",
            ],
        ),
        ExamQuestion(
            question_number=4,
            title="Collision & Broadcast Domains Separation",
            question_type="Multiple Choice",
            prompt_text="Select the correct statement regarding Collision Domains and Broadcast Domains:",
            options=[
                QuestionOption("A", "In a star topology with a switch, all hosts share the same collision domain.", False, "Each port on a switch forms an isolated collision domain."),
                QuestionOption("B", "In a shared bus topology, all hosts share the same collision domain.", True, "On a shared coaxial bus, every transmission is visible across the entire medium and can collide."),
                QuestionOption("C", "A router does not isolate broadcast domains.", False, "A router isolates broadcast domains on each physical interface."),
                QuestionOption("D", "A hub creates an isolated collision domain per port.", False, "A hub maintains a single shared collision domain across all ports."),
            ],
            correct_option_letter="B",
            detailed_justification="In a shared bus topology, all connected hosts share the same physical transmission medium. Conversely, switches employ micro-segmentation so each port forms its own collision domain.",
        ),
    ]

    nodes = [
        TopologyNode("pc_a", "PC A", "host", 120, 150, "195.130.8.25", "00:25:64:D5:10:8B"),
        TopologyNode("sw_1", "Switch LAN", "switch", 320, 150),
        TopologyNode("router_1", "Router Core", "router", 540, 150, "195.130.8.1", "00:00:5E:00:10:01"),
        TopologyNode("cloud_1", "Internet WAN", "cloud", 740, 150, "172.16.1.1", "00:0B:14:E0:00:35"),
    ]

    links = [
        TopologyLink("pc_a", "sw_1", 100, 0.05, 2.0, "copper", "100M UTP"),
        TopologyLink("sw_1", "router_1", 1000, 0.1, 2.0, "copper", "1G Fiber/UTP"),
        TopologyLink("router_1", "cloud_1", 10000, 50.0, 2.0, "fiber", "10G WAN Link"),
    ]

    return NetworkScenario(
        id="exam_past_2023_2024",
        title="Exam Questions (2023-2024)",
        subtitle="Official Exam Paper: Delays, ARP Protocol, RIP Configuration & Domains",
        course_tag="Past Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Identify the operating layer of network devices (Repeater L1, Switch L2, Router L3).",
            "2. Master ARP message exchanges (Request = Broadcast, Reply = Unicast, Cache = Temporary Memory).",
            "3. Distinguish Collision Domains (per switch port) from Broadcast Domains (per router interface).",
        ],
        calculator_type="delay",
    )
