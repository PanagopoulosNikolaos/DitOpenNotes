"""Synthetic Exam 3: P2P, Store-and-Forward & End-to-End Delays.

Covers Peer-to-Peer vs Client-Server, Store-and-Forward packet transmission,
Traceroute TTL mechanism, /26 subnet matching, and multi-hop delay calculations.
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
    """Constructs and returns Synthetic Exam 3 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The mock simulation examination paper "),
                TextSegment(
                    text="Synthetic & Realistic Exam 3",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Realistic mock examination paper",
                ),
                TextSegment(text=" focuses on "),
                TextSegment(
                    text="Peer-to-Peer (P2P)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="P2P",
                    tooltip="Each node functions simultaneously as both client and server",
                ),
                TextSegment(text=" architecture, the operational principle of "),
                TextSegment(
                    text="Store-and-Forward in Routers",
                    is_highlight=True,
                    category="routing",
                    tag_label="STORE & FORWARD",
                    tooltip="Complete packet reception prior to outbound forwarding",
                ),
                TextSegment(text=" and the mechanism of "),
                TextSegment(
                    text="Traceroute via the TTL (Time-To-Live) field",
                    is_highlight=True,
                    category="protocol",
                    tag_label="TRACEROUTE TTL",
                    tooltip="Discovering intermediate routers using ICMP Time Exceeded",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The computational section includes an exhaustive problem evaluating "),
                TextSegment(
                    text="End-to-End Delay for N = 3 Hops",
                    is_highlight=True,
                    category="delay",
                    tag_label="3 HOPS DELAY",
                    tooltip="d = 1000 km, s = 2*10^8 m/s, R = 10 Mbps, L = 10000 bits",
                ),
                TextSegment(text=" with intermediate store-and-forward routing and analysis of "),
                TextSegment(
                    text="IPv4 Subnetting /26",
                    is_highlight=True,
                    category="routing",
                    tag_label="SUBNET /26",
                    tooltip="Subnet mask 255.255.255.192, Block Size 64 (192-255)",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Peer-to-Peer (P2P) Architecture Characteristics",
            question_type="Multiple Choice",
            prompt_text="In a pure Peer-to-Peer (P2P) network architecture, which of the following statements is correct?",
            options=[
                QuestionOption("A", "Network reliability relies entirely on a centralized server.", False, "In pure P2P there is no centralized server (fully decentralized)."),
                QuestionOption("B", "Adding new peers always decreases total available bandwidth.", False, "New peers contribute upload bandwidth, providing self-scalability."),
                QuestionOption("C", "Each participating peer acts simultaneously as both a client and a server.", True, "Each peer requests data as a client and serves content to other peers as a server."),
                QuestionOption("D", "Direct file sharing between peers is impossible.", False, "P2P is widely used for distributed file sharing (e.g., BitTorrent)."),
            ],
            correct_option_letter="C",
            detailed_justification="In the Peer-to-Peer paradigm, all participating nodes are equals (servents = server + client), providing inherent self-scalability as peer count grows.",
        ),
        ExamQuestion(
            question_number=2,
            title="Store-and-Forward Operational Principle",
            question_type="Multiple Choice",
            prompt_text="The 'Store-and-Forward' mechanism in a packet-switching router signifies that:",
            options=[
                QuestionOption("A", "The router must receive the complete packet before beginning its transmission onto the outbound link.", True, "All L bits must be received and verified against checksum/CRC before retransmission begins on the next link."),
                QuestionOption("B", "The router permanently stores all forwarded packets on non-volatile storage.", False, "Packets are stored temporarily in volatile RAM buffer queues."),
                QuestionOption("C", "Forwarding begins as soon as only the header bits have arrived.", False, "That describes Cut-Through switching, not Store-and-Forward."),
                QuestionOption("D", "The router never performs packet integrity checks.", False, "It performs header checksum verification and frame CRC validation."),
            ],
            correct_option_letter="A",
            detailed_justification="Store-and-Forward introduces a transmission delay penalty (L/R) at each intermediate hop, because the router buffers the full packet prior to forwarding.",
        ),
        ExamQuestion(
            question_number=3,
            title="End-to-End Delay Calculation for N = 3 Hops",
            question_type="Calculations",
            prompt_text="Consider a network path from Host A to Host B traversing 2 intermediate routers (N = 3 hops). Each link has distance d = 1000 km, propagation speed s = 2*10^8 m/s, and transmission rate R = 10 Mbps. A packet of size L = 10,000 bits is sent from A to B. Calculate the total end-to-end delay (ignoring queuing and nodal processing delays).",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Transmission Delay per Hop (d_trans)",
                    formula="d_trans = L / R = 10,000 bits / (10 * 10^6 bps)",
                    substitution="10,000 / 10,000,000",
                    result="1 * 10^-3 s = 1 ms",
                    rationale="Time required to push all packet bits onto a single link.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Propagation Delay per Hop (d_prop)",
                    formula="d_prop = d / s = 1,000,000 m / (2 * 10^8 m/s)",
                    substitution="10^6 / (2 * 10^8)",
                    result="5 * 10^-3 s = 5 ms",
                    rationale="Signal transit time over a distance of 1,000 km.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Total End-to-End Delay across 3 Hops",
                    formula="T_total = N * d_trans + N * d_prop",
                    substitution="3 * 1.0 ms + 3 * 5.0 ms",
                    result="3 ms + 15 ms = 18 ms",
                    rationale="The packet is transmitted 3 times (A->R1, R1->R2, R2->B) and propagates 3 times.",
                ),
            ],
            detailed_justification="Across 3 consecutive Store-and-Forward links without pipelining of multiple packets, the total delay is T = 3 * (1 ms + 5 ms) = 18 ms.",
        ),
    ]

    nodes = [
        TopologyNode("h_a", "Host A", "host", 100, 150, "172.16.30.1/26"),
        TopologyNode("r_1", "Router 1", "router", 350, 150, "172.16.30.65/26"),
        TopologyNode("r_2", "Router 2", "router", 600, 150, "172.16.30.129/26"),
        TopologyNode("h_b", "Host B", "host", 850, 150, "172.16.30.200/26"),
    ]

    links = [
        TopologyLink("h_a", "r_1", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
        TopologyLink("r_1", "r_2", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
        TopologyLink("r_2", "h_b", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
    ]

    return NetworkScenario(
        id="exam_synth_3",
        title="Synthetic Exam 3: P2P & Store-and-Forward",
        subtitle="P2P Architecture, Store-and-Forward, Traceroute & 3-Hop Delays",
        course_tag="Synthetic Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. P2P: Servents (Clients + Servers concurrently).",
            "2. Store-and-Forward: Receive complete packet L prior to outbound transmission.",
            "3. 3-Hop Delay = 3 * (L/R + d/s) = 3 * (1 ms + 5 ms) = 18 ms.",
        ],
        calculator_type="delay",
    )
