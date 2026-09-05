"""Synthetic Exam 2: Longest Prefix Match, Forwarding Tables & ARP.

Covers Network Core components, Longest Prefix Match (LPM) rules,
Data Plane vs Control Plane, Count-to-Infinity in Distance Vector,
Cumulative ACKs in TCP, and Forwarding Table lookups.
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
    """Constructs and returns Synthetic Exam 2 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The reference examination paper "),
                TextSegment(
                    text="Synthetic & Realistic Exam 2",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Realistic mock examination paper",
                ),
                TextSegment(text=" analyzes the operation of the "),
                TextSegment(
                    text="Network Core (Routers)",
                    is_highlight=True,
                    category="device",
                    tag_label="ROUTER CORE",
                    tooltip="Intermediate packet switching nodes",
                ),
                TextSegment(text=", the selection rule of "),
                TextSegment(
                    text="Longest Prefix Match (LPM)",
                    is_highlight=True,
                    category="routing",
                    tag_label="LPM RULE",
                    tooltip="Selecting the forwarding entry with the longest prefix length",
                ),
                TextSegment(text=" and the architectural distinction between "),
                TextSegment(
                    text="Data Plane (Forwarding) and Control Plane (Routing)",
                    is_highlight=True,
                    category="routing",
                    tag_label="PLANES",
                    tooltip="Hardware forwarding vs routing algorithm computation",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The second section examines the vulnerability of "),
                TextSegment(
                    text="Count-to-Infinity in Distance-Vector Algorithms",
                    is_highlight=True,
                    category="routing",
                    tag_label="BELLMAN-FORD",
                    tooltip="Slow convergence and routing loops upon link failure",
                ),
                TextSegment(text=", the mechanics of "),
                TextSegment(
                    text="Cumulative ACKs in TCP",
                    is_highlight=True,
                    category="protocol",
                    tag_label="TCP ACKs",
                    tooltip="Cumulative acknowledgment of all contiguous received bytes",
                ),
                TextSegment(text=" and the isolation of "),
                TextSegment(
                    text="Collision Domains per Switch Port",
                    is_highlight=True,
                    category="device",
                    tag_label="SWITCH L2",
                    tooltip="Isolating collision domains without isolating broadcast domains",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Network Core Infrastructure Elements",
            question_type="Multiple Choice",
            prompt_text="Which of the following belongs strictly to the **Network Core**?",
            options=[
                QuestionOption("A", "Web Servers", False, "Servers reside at the Network Edge."),
                QuestionOption("B", "Routers", True, "The network core consists of interconnected routers and switches that forward traffic."),
                QuestionOption("C", "Smartphones", False, "Smartphones are end systems (hosts) at the Network Edge."),
                QuestionOption("D", "Email Client Applications", False, "Client applications run on end systems."),
            ],
            correct_option_letter="B",
            detailed_justification="The Network Core consists of the mesh of interconnected routers and switches that forward data across the network fabric.",
        ),
        ExamQuestion(
            question_number=2,
            title="Longest Prefix Match (LPM) Rule",
            question_type="Multiple Choice",
            prompt_text="According to the Longest Prefix Match (LPM) rule, when a destination IP address matches multiple entries in a forwarding table, which entry is selected?",
            options=[
                QuestionOption("A", "The entry with the fewest bits in the prefix.", False, "A shorter prefix is less specific and discarded."),
                QuestionOption("B", "The entry with the greatest number of bits in the prefix.", True, "The longest prefix is the most specific route and always takes precedence."),
                QuestionOption("C", "The default route (0.0.0.0/0).", False, "The default route is chosen only when no other entry matches."),
                QuestionOption("D", "The first randomly encountered entry in the table.", False, "Table ordering does not dictate LPM forwarding decisions."),
            ],
            correct_option_letter="B",
            detailed_justification="Longest Prefix Match selects the entry with the longest subnet mask (e.g., a /28 route takes precedence over /24 and /16).",
        ),
        ExamQuestion(
            question_number=3,
            title="Data Plane vs Control Plane Responsibilities",
            question_type="Multiple Choice",
            prompt_text="The Data Plane of a network router is responsible for:",
            options=[
                QuestionOption("A", "Executing the Dijkstra shortest path algorithm.", False, "Belongs to the Control Plane."),
                QuestionOption("B", "Physical packet forwarding from an input interface to an output interface.", True, "The Data Plane is implemented in dedicated hardware (ASIC/TCAM) for nanosecond forwarding."),
                QuestionOption("C", "Exchanging OSPF link-state messages with neighboring routers.", False, "Belongs to the Control Plane."),
                QuestionOption("D", "Maintaining the Routing Information Base (RIB).", False, "Belongs to the Control Plane."),
            ],
            correct_option_letter="B",
            detailed_justification="Architectural distinction: Forwarding (Data Plane - per-packet local hardware switching) vs Routing (Control Plane - network-wide route computation via distributed algorithms).",
        ),
        ExamQuestion(
            question_number=4,
            title="Count-to-Infinity in Routing Algorithms",
            question_type="Multiple Choice",
            prompt_text="The 'Count-to-Infinity' phenomenon is a recognized vulnerability in which class of routing algorithms?",
            options=[
                QuestionOption("A", "Link-State (Dijkstra)", False, "Link-State algorithms possess full topology awareness and do not suffer from Count-to-Infinity."),
                QuestionOption("B", "Distance-Vector (Bellman-Ford)", True, "Because bad news travels slowly, nodes can form persistent routing loops, incrementing hop metrics indefinitely."),
                QuestionOption("C", "Longest Prefix Match", False, "LPM is an IP lookup method, not a dynamic routing algorithm."),
                QuestionOption("D", "CSMA/CD", False, "CSMA/CD is a Layer 2 media access control protocol."),
            ],
            correct_option_letter="B",
            detailed_justification="Distance-Vector algorithms (e.g., RIP) use split horizon and poison reverse techniques to mitigate the Count-to-Infinity problem.",
        ),
    ]

    nodes = [
        TopologyNode("r_in", "Ingress Router", "router", 120, 150, "192.168.1.1", "00:11:22:33:44:01"),
        TopologyNode("r_core", "Core Router (LPM)", "router", 420, 150, "10.0.0.1", "00:11:22:33:44:02"),
        TopologyNode("sub1", "Subnet /24 (eth0)", "host", 720, 80, "192.168.10.0/24"),
        TopologyNode("sub2", "Subnet /28 (eth1)", "host", 720, 220, "192.168.10.16/28"),
    ]

    links = [
        TopologyLink("r_in", "r_core", 1000, 10.0, 2.0, "fiber", "1G Fiber"),
        TopologyLink("r_core", "sub1", 100, 0.5, 2.0, "copper", "eth0 /24"),
        TopologyLink("r_core", "sub2", 100, 0.5, 2.0, "copper", "eth1 /28 (LPM Match)"),
    ]

    return NetworkScenario(
        id="exam_synth_2",
        title="Synthetic Exam 2: LPM & Distance-Vector",
        subtitle="Network Core, Longest Prefix Match, Data Plane & Count-to-Infinity",
        course_tag="Synthetic Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Routers = Network Core (Data plane hardware forwarding).",
            "2. LPM: Longest prefix length = Most specific route.",
            "3. Distance-Vector: Count-to-Infinity (Slow convergence upon link failure).",
        ],
        calculator_type="lpm",
    )
