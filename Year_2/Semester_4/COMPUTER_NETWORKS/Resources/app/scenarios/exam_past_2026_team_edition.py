"""Past Exam 2026 Team Edition Scenario Module.

Covers End-to-End Delay Derivations, Bandwidth-Delay Product, Google BBR Congestion Control,
OSPF configuration, BGP Autonomous System Routing, Dijkstra Graph Shortest Path,
and CSMA/CD Minimum Frame Size calculation.
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
    """Constructs and returns the complete Past Exam 2026 (Team Edition) scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The examination paper "),
                TextSegment(
                    text="Computer Networks 2026 (Team Edition)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="EXAM",
                    tooltip="Advanced network architecture and algorithmic problems",
                ),
                TextSegment(text=" focuses on theoretical and computational analysis of "),
                TextSegment(
                    text="End-to-End Delay",
                    is_highlight=True,
                    category="delay",
                    tag_label="DELAYS L/R+d/s",
                    tooltip="Mathematical model of transmission and propagation delays",
                ),
                TextSegment(text=", the calculation of the "),
                TextSegment(
                    text="Bandwidth-Delay Product (BDP)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP = R * RTT",
                    tooltip="Maximum capacity of in-flight bits across the channel",
                ),
                TextSegment(text=" and modern congestion control via "),
                TextSegment(
                    text="Google BBR (CWND = RtProp * BtlBw)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="BBR CONGESTION",
                    tooltip="Congestion control based on minimum RTT and bottleneck bandwidth",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The second section examines inter-domain routing policies between "),
                TextSegment(
                    text="Autonomous Systems (BGP Autonomous Systems)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP AS",
                    tooltip="Inter-domain routing policies between Verizon and AT&T",
                ),
                TextSegment(text=", intra-domain configuration of "),
                TextSegment(
                    text="OSPF (Open Shortest Path First)",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF L3",
                    tooltip="Link-State interior routing",
                ),
                TextSegment(text=", graph execution of the "),
                TextSegment(
                    text="Dijkstra Shortest Path",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA",
                    tooltip="Finding the optimal path on a link-cost topology graph",
                ),
                TextSegment(text=" algorithm, and derivation of the "),
                TextSegment(
                    text="CSMA/CD Minimum Frame Size (L_min = 2 * d_prop * R)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD L_MIN",
                    tooltip="Preventing undetected collisions in shared Ethernet",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Mathematical Formulation of End-to-End Delay",
            question_type="Calculations",
            prompt_text="Formulate the exact end-to-end delay across a single point-to-point link (A -> B) given packet size L, transmission rate R, link length l, and propagation speed u.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Transmission Delay (d_trans)",
                    formula="d_trans = L / R",
                    substitution="L bits / R bps",
                    result="L / R (sec)",
                    rationale="The time required to push all packet bits onto the physical transmission medium.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Propagation Delay (d_prop)",
                    formula="d_prop = l / u",
                    substitution="l meters / u (meters/sec)",
                    result="l / u (sec)",
                    rationale="The time required for a single bit to traverse the physical distance l.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Total Delay (excluding queuing and nodal processing)",
                    formula="d_total = d_trans + d_prop",
                    substitution="(L / R) + (l / u)",
                    result="(L / R) + (l / u) (sec)",
                    rationale="Across a single link without intermediate routers, the sum of transmission and propagation delay yields the total delay.",
                ),
            ],
            detailed_justification="Assumptions note: If processing delay d_proc at node A or queuing delay d_queue is included, they add linearly: d_nodal = d_proc + d_queue + d_trans + d_prop.",
        ),
        ExamQuestion(
            question_number=2,
            title="CSMA/CD Minimum Frame Size Calculation",
            question_type="Calculations",
            prompt_text="A local network employs CSMA/CD with bandwidth R = 10 Mbps. If the maximum one-way propagation delay is d_prop = 25.6 microseconds, calculate the minimum frame size (L_min).",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="CSMA/CD Collision Detection Condition",
                    formula="d_trans >= 2 * d_prop  <=>  (L_min / R) >= 2 * d_prop",
                    substitution="L_min = 2 * d_prop * R",
                    result="L_min = 2 * (25.6 * 10^-6) * (10 * 10^6)",
                    rationale="The transmitting station must continue transmitting for at least 2*d_prop (Round Trip Time) to detect a collision from the furthest network point.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Evaluation in Bits and Bytes",
                    formula="L_min = 51.2 * 10 = 512 bits",
                    substitution="512 bits / 8 bits per byte",
                    result="64 Bytes",
                    rationale="This is precisely why standard IEEE 802.3 Ethernet mandates a minimum frame size of 64 Bytes.",
                ),
            ],
            detailed_justification="If a frame were smaller than 64 bytes (512 bits), the transmitter would finish transmission before the collision signal (JAM signal) could return, incorrectly assuming successful delivery.",
            common_pitfalls=[
                "Omitting the factor of 2 (2 * d_prop for round-trip time).",
                "Failing to convert 512 bits into 64 Bytes.",
            ],
        ),
        ExamQuestion(
            question_number=3,
            title="Google BBR Congestion Control (CWND)",
            question_type="Calculations",
            prompt_text="Given RTT = 5 ms (RtProp) and transmission rate R = 0.125 GB/s (BtlBw), calculate the congestion window size (CWND) according to the BBR congestion control protocol.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Unit Conversion",
                    formula="BtlBw = 0.125 GB/s = 0.125 * 10^9 Bytes/sec = 125 MB/s, RtProp = 5 ms = 0.005 sec",
                    substitution="CWND = RtProp * BtlBw",
                    result="0.005 s * 125,000,000 Bytes/s",
                    rationale="The congestion window in BBR is sized to match the Bandwidth-Delay Product (BDP).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Final Window Calculation",
                    formula="CWND = 0.005 * 125 * 10^6",
                    substitution="CWND = 625,000 Bytes",
                    result="625 KB (or 625,000 Bytes)",
                    rationale="BBR keeps the transmission pipe fully utilized without creating unnecessary queue buildup (bufferbloat).",
                ),
            ],
            detailed_justification="BBR (Bottleneck Bandwidth and RTT) models the physical channel by independently estimating minimum RTT (uncongested) and maximum bottleneck throughput, thereby preventing congestion collapse.",
        ),
    ]

    nodes = [
        TopologyNode("host_a", "Host A", "host", 100, 150, "10.10.10.1", "00:AA:11:22:33:01"),
        TopologyNode("router_b", "Router B (OSPF)", "router", 340, 150, "10.10.10.2", "00:BB:22:33:44:02"),
        TopologyNode("router_c", "Router C (Core)", "router", 580, 150, "172.16.8.1", "00:CC:33:44:55:03"),
        TopologyNode("server_k", "DIT UoI Server", "server", 800, 150, "192.168.1.10", "00:DD:44:55:66:04"),
    ]

    links = [
        TopologyLink("host_a", "router_b", 10, 100.0, 2.5, "copper", "10M | 100km"),
        TopologyLink("router_b", "router_c", 10, 50.0, 2.5, "fiber", "10M | 50km"),
        TopologyLink("router_c", "server_k", 1000, 1.0, 2.0, "fiber", "1G Server Link"),
    ]

    return NetworkScenario(
        id="exam_past_2026_team",
        title="Exam Questions (2026 Team Edition)",
        subtitle="End-to-End Delays, Google BBR CWND, OSPF, Dijkstra & CSMA/CD L_min",
        course_tag="Past Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_total = (L/R) + (l/u) for a single point-to-point link.",
            "2. CSMA/CD Minimum Frame Size: L_min = 2 * d_prop * R (64 Bytes for 10 Mbps Ethernet).",
            "3. BBR Congestion Window: CWND = RtProp * BtlBw (Bandwidth-Delay Product).",
        ],
        calculator_type="delay",
    )
