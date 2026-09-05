"""Synthetic Exam 1: Core vs Edge, Delay Breakdown & Subnetting.

Covers OSI layer PDUs, Collision domains in Star topology,
d_trans calculations, IPv4 subnet matching (/25), statistical multiplexing,
and multi-hop delay derivations.
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
    """Constructs and returns Synthetic Exam 1 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The reference examination paper "),
                TextSegment(
                    text="Synthetic & Realistic Exam 1",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Realistic mock examination paper",
                ),
                TextSegment(text=" focuses on protocol architecture, the "),
                TextSegment(
                    text="Data Link Layer (PDU: Frame)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="L2 FRAME",
                    tooltip="Organizing bits into frames with MAC addresses",
                ),
                TextSegment(text=", computing "),
                TextSegment(
                    text="Collision Domains on a Switch (Micro-segmentation)",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="1 Collision Domain per switch port",
                ),
                TextSegment(text=" and the exact calculation of "),
                TextSegment(
                    text="Transmission Delay d_trans = L / R",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_TRANS",
                    tooltip="L = 2000 bits, R = 1 Mbps -> d_trans = 2 ms",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Additionally, the exam covers determining subnet boundaries for IPv4 address "),
                TextSegment(
                    text="192.168.5.130/25",
                    is_highlight=True,
                    category="routing",
                    tag_label="SUBNET /25",
                    tooltip="Subnet mask 255.255.255.128, Block Size 128 (128-255)",
                ),
                TextSegment(text=" and the operational principle of "),
                TextSegment(
                    text="Statistical Multiplexing",
                    is_highlight=True,
                    category="protocol",
                    tag_label="STAT MULTIPLEX",
                    tooltip="Dynamic on-demand bandwidth allocation",
                ),
                TextSegment(text=" in packet switching."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Protocol Data Unit (PDU) at Layer 2",
            question_type="Multiple Choice",
            prompt_text="Which of the following layers of the OSI model uses the **'Frame'** as its PDU?",
            options=[
                QuestionOption("A", "Physical Layer (Layer 1)", False, "The Physical Layer handles raw bits."),
                QuestionOption("B", "Data Link Layer (Layer 2)", True, "The Data Link Layer organizes raw bits into frames with MAC headers."),
                QuestionOption("C", "Network Layer (Layer 3)", False, "The Network Layer operates on packets/datagrams."),
                QuestionOption("D", "Transport Layer (Layer 4)", False, "The Transport Layer handles segments/datagrams."),
            ],
            correct_option_letter="B",
            detailed_justification="Each OSI layer specifies a distinct PDU naming convention: L1=Bit, L2=Frame, L3=Packet, L4=Segment, L5-7=Message.",
        ),
        ExamQuestion(
            question_number=2,
            title="Collision Domains on a Switch",
            question_type="Multiple Choice",
            prompt_text="In a star topology utilizing exclusively a switch, how many collision domains are formed for 8 connected computers?",
            options=[
                QuestionOption("A", "1", False, "This would only apply if an obsolete Layer 1 Hub were used."),
                QuestionOption("B", "8", True, "Each physical port on the switch constitutes an independent collision domain (micro-segmentation)."),
                QuestionOption("C", "4", False, "There is no grouping of 2 ports per domain."),
                QuestionOption("D", "0", False, "Each point-to-point link constitutes a collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification="Switches isolate traffic per port. For 8 computers connected to 8 switch ports, there are exactly 8 isolated collision domains.",
        ),
        ExamQuestion(
            question_number=3,
            title="d_trans Calculation for Packet L = 2000 bits",
            question_type="Calculations",
            prompt_text="The transmission delay (d_trans) for a packet of size L = 2000 bits over a link with transmission rate R = 1 Mbps is:",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Transmission Formula Application",
                    formula="d_trans = L / R",
                    substitution="2000 bits / (1 * 10^6 bps)",
                    result="2 * 10^-3 sec = 2 ms",
                    rationale="Conversion: 1 Mbps = 1,000,000 bps.",
                )
            ],
            detailed_justification="d_trans = 2000 / 10^6 = 0.002 s = 2 ms.",
        ),
        ExamQuestion(
            question_number=4,
            title="IPv4 /25 Subnet Membership",
            question_type="Multiple Choice",
            prompt_text="Which of the following IP addresses belongs to the same subnet as 192.168.5.130/25?",
            options=[
                QuestionOption("A", "192.168.5.10", False, "Belongs to the 1st subnet (.0 through .127)."),
                QuestionOption("B", "192.168.5.200", True, "The /25 mask splits the Class C space into two blocks: 0-127 and 128-255. Both .130 and .200 fall into the 2nd block (128-255)."),
                QuestionOption("C", "192.168.5.255", False, "This is the broadcast address of the 2nd subnet (cannot be assigned to a host)."),
                QuestionOption("D", "192.168.5.126", False, "Belongs to the 1st subnet (0-127)."),
            ],
            correct_option_letter="B",
            detailed_justification="Block size = 256 - 128 = 128. Subnet 1: 192.168.5.0/25 (.1-.126), Subnet 2: 192.168.5.128/25 (.129-.254). Address .200 is a valid host within the same subnet as .130.",
        ),
    ]

    nodes = [
        TopologyNode("h1", "Host 1", "host", 100, 100, "192.168.5.130/25"),
        TopologyNode("h2", "Host 2", "host", 100, 200, "192.168.5.200/25"),
        TopologyNode("sw", "Switch L2", "switch", 350, 150),
        TopologyNode("r1", "Gateway Router", "router", 600, 150, "192.168.5.129/25"),
    ]

    links = [
        TopologyLink("h1", "sw", 100, 0.02, 2.0, "copper", "100M UTP"),
        TopologyLink("h2", "sw", 100, 0.02, 2.0, "copper", "100M UTP"),
        TopologyLink("sw", "r1", 1000, 0.05, 2.0, "copper", "1G UTP"),
    ]

    return NetworkScenario(
        id="exam_synth_1",
        title="Synthetic Exam 1: Core, Delays & Subnetting",
        subtitle="PDUs, Micro-segmentation, d_trans = L/R & /25 Subnet Boundaries",
        course_tag="Synthetic Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. L2 PDU = Frame.",
            "2. Switch ports = 1 collision domain per port.",
            "3. d_trans = L / R = 2000 / 10^6 = 2 ms.",
            "4. /25 CIDR Subnetting: Block size 128 (Subnet 128-255).",
        ],
        calculator_type="delay",
    )
