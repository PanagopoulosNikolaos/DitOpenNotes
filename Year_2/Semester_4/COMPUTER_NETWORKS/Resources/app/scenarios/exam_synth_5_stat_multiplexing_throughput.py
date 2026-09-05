"""Synthetic Exam 5: Statistical Multiplexing, Throughput & CSMA/CD.

Covers Statistical Multiplexing, Multi-hop Delays & RTT with d_proc,
Cisco IOS RIPv2 configuration, CSMA/CD 100Mbps Fast Ethernet (128 Bytes),
Transoceanic BDP (30 Mbits) and Buffer Queuing Delay (8 ms).
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
    """Constructs and returns Synthetic Exam 5 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The mock simulation examination paper "),
                TextSegment(
                    text="Synthetic & Realistic Exam 5",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Realistic mock examination paper",
                ),
                TextSegment(text=" analyzes the advantages of "),
                TextSegment(
                    text="Statistical Multiplexing",
                    is_highlight=True,
                    category="protocol",
                    tag_label="STAT MULTIPLEX",
                    tooltip="Dynamic on-demand resource allocation",
                ),
                TextSegment(text=", delay derivations for "),
                TextSegment(
                    text="Delays across 2 Serial Links (t_total = 0.3006 s)",
                    is_highlight=True,
                    category="delay",
                    tag_label="MULTI-HOP DELAY",
                    tooltip="R1=20kbps, L1=50km, R2=10kbps, L2=100km, P=2000bits",
                ),
                TextSegment(text=" and the configuration of "),
                TextSegment(
                    text="Cisco RIPv2 Routing",
                    is_highlight=True,
                    category="routing",
                    tag_label="CISCO RIPV2",
                    tooltip="CLI commands: router rip, version 2, network...",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The second section evaluates the "),
                TextSegment(
                    text="CSMA/CD Minimum Frame Size at 100 Mbps (128 Bytes)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD 100M",
                    tooltip="L_min = 2 * 5.12 us * 100 Mbps = 1024 bits = 128 Bytes",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="Transoceanic BDP (30 Mbits)",
                    is_highlight=True,
                    category="delay",
                    tag_label="TRANSOCEANIC BDP",
                    tooltip="d = 6000 km, s = 2*10^8 m/s, R = 1 Gbps -> BDP = 30 Mbits",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="Buffer Queuing Delay (d_queue = 8 ms)",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_QUEUE",
                    tooltip="1 MB buffer / 1 Gbps bandwidth = 8 ms",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Packet Switching vs Circuit Switching Advantages",
            question_type="Multiple Choice",
            prompt_text="Which of the following is a defining characteristic of packet switching compared to circuit switching?",
            options=[
                QuestionOption("A", "Exclusive pre-allocation of end-to-end circuit resources.", False, "This is the hallmark of circuit switching."),
                QuestionOption("B", "Capability for statistical multiplexing.", True, "Packet switching shares network resources dynamically on demand, allowing more concurrent users."),
                QuestionOption("C", "Absolute immunity to packet loss.", False, "Packet switching is susceptible to buffer drop under high congestion."),
                QuestionOption("D", "Strictly guaranteed dedicated transmission rate for each user.", False, "Guaranteed throughput requires circuit reservation."),
            ],
            correct_option_letter="B",
            detailed_justification="In statistical multiplexing, users consume transmission bandwidth only when they have active packets to send, dramatically improving average channel utilization.",
        ),
        ExamQuestion(
            question_number=2,
            title="CSMA/CD Minimum Frame Size Calculation at 100 Mbps",
            question_type="Calculations",
            prompt_text="A Fast Ethernet network operates CSMA/CD at R = 100 Mbps. If the maximum one-way propagation delay is t_prop = 5.12 microseconds, what is the minimum frame size in Bytes?",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Application of L_min Criterion",
                    formula="L_min = 2 * t_prop * R",
                    substitution="2 * (5.12 * 10^-6 s) * (100 * 10^6 bps)",
                    result="1024 bits",
                    rationale="Transmission time must be at least equal to the Round-Trip Time (2 * t_prop).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Conversion to Bytes",
                    formula="L_min (Bytes) = 1024 / 8",
                    substitution="1024 / 8",
                    result="128 Bytes",
                    rationale="In 100 Mbps Fast Ethernet covering larger span budgets, L_min is set to 128 Bytes (double the classic 64 Bytes).",
                ),
            ],
            detailed_justification="L_min = 2 * 5.12 microseconds * 100 Mbps = 1024 bits = 128 Bytes.",
        ),
        ExamQuestion(
            question_number=3,
            title="BDP and Buffer Queuing Delay Calculations",
            question_type="Calculations",
            prompt_text="A transoceanic fiber link spans 6,000 km with s = 2*10^8 m/s and Bandwidth R = 1 Gbps. Find d_prop, BDP, and the queuing delay d_queue if the router buffer holds 1,000,000 Bytes.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Propagation Delay d_prop",
                    formula="d_prop = d / s = (6,000 * 10^3 m) / (2 * 10^8 m/s)",
                    substitution="6 * 10^6 / (2 * 10^8)",
                    result="0.03 s = 30 ms",
                    rationale="Transit time of optical pulse through transoceanic fiber.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Bandwidth-Delay Product (BDP)",
                    formula="BDP = R * d_prop = (10^9 bps) * 0.03 s",
                    substitution="1,000,000,000 * 0.03",
                    result="30,000,000 bits = 30 Mbits (3.75 MB)",
                    rationale="Maximum number of in-flight bits inside the undersea cable.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Queuing Delay d_queue",
                    formula="d_queue = Buffer_bits / R_out = (1,000,000 * 8 bits) / 10^9 bps",
                    substitution="8,000,000 / 1,000,000,000",
                    result="8 * 10^-3 s = 8 ms",
                    rationale="Time to drain 1 MB router queue at an egress rate of 1 Gbps.",
                ),
            ],
            detailed_justification="d_prop = 30 ms, BDP = 30 Mbits (3.75 MB), d_queue = 8 ms.",
        ),
    ]

    nodes = [
        TopologyNode("r_trans1", "Router Europe", "router", 120, 150, "192.168.10.1"),
        TopologyNode("r_trans2", "Router US Coast", "router", 620, 150, "10.0.1.1"),
        TopologyNode("srv_us", "US Data Center", "server", 850, 150, "10.0.2.10"),
    ]

    links = [
        TopologyLink("r_trans1", "r_trans2", 1000, 6000.0, 2.0, "fiber", "1G Transatlantic | 6000km"),
        TopologyLink("r_trans2", "srv_us", 10000, 10.0, 2.0, "fiber", "10G Metro"),
    ]

    return NetworkScenario(
        id="exam_synth_5",
        title="Synthetic Exam 5: Stat Multiplexing & BDP",
        subtitle="Statistical Multiplexing, Multi-Hop Delays, CSMA/CD 100M & Transoceanic BDP",
        course_tag="Synthetic Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Statistical Multiplexing: On-demand bandwidth allocation.",
            "2. CSMA/CD 100M: L_min = 2 * 5.12 microseconds * 100 Mbps = 128 Bytes.",
            "3. Transoceanic BDP = 1 Gbps * 30 ms = 30 Mbits.",
            "4. d_queue = 1 MB / 1 Gbps = 8 ms.",
        ],
        calculator_type="delay",
    )
