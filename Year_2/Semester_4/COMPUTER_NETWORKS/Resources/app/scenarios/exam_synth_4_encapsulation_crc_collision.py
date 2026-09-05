"""Synthetic Exam 4: Encapsulation, TCP Timeout, Dijkstra & Hamming Codes.

Covers Encapsulation, Collision vs Broadcast Domains, TCP Timeout estimation,
BDP sliding window sizing, Dijkstra Link-State execution, and Hamming Error-Correcting Code.
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
    """Constructs and returns Synthetic Exam 4 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The mock simulation examination paper "),
                TextSegment(
                    text="Synthetic & Realistic Exam 4",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Realistic mock examination paper",
                ),
                TextSegment(text=" examines the process of "),
                TextSegment(
                    text="Encapsulation",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ENCAPSULATION",
                    tooltip="Adding protocol headers across layers",
                ),
                TextSegment(text=", the demarcation of "),
                TextSegment(
                    text="Collision Domains (Switches) vs Broadcast Domains (Routers)",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="Demarcation of collision and broadcast domains",
                ),
                TextSegment(text=" and the calculation of "),
                TextSegment(
                    text="TCP Timeout & Sliding Window (BDP = R * RTT)",
                    is_highlight=True,
                    category="delay",
                    tag_label="TCP BDP",
                    tooltip="R = 200 Mbps, RTT = 50 ms -> Window = 1.25 MB",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The second section executes the "),
                TextSegment(
                    text="Dijkstra Shortest Path on a 7-Node Graph",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA",
                    tooltip="Optimal path from A to G with cost 5 (A -> D -> G)",
                ),
                TextSegment(text=" algorithm and constructs a "),
                TextSegment(
                    text="Hamming Error-Correcting Code (Odd Parity)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="HAMMING CODE",
                    tooltip="2^p >= d + p + 1 -> p = 3 parity bits for d = 4 data bits",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Encapsulation Process",
            question_type="Multiple Choice",
            prompt_text="During the 'Encapsulation' process, as user data travels downward from the Application Layer toward the Physical Layer:",
            options=[
                QuestionOption("A", "Protocol headers are stripped at each layer.", False, "Stripping headers is decapsulation performed at the receiver."),
                QuestionOption("B", "Data is mandatorily encrypted by the Data Link Layer.", False, "Encryption typically occurs at the TLS/Application layer."),
                QuestionOption("C", "A new protocol header is appended at each layer, culminating in the Layer 2 frame.", True, "Each layer wraps the incoming payload with its own protocol header (and trailer at L2)."),
                QuestionOption("D", "The IP address changes at every layer.", False, "The IP address belongs strictly to the Network Layer."),
            ],
            correct_option_letter="C",
            detailed_justification="During transmission (Encapsulation), data descends the protocol stack, with each layer prepending its corresponding header (and L2 appending a frame check sequence trailer).",
        ),
        ExamQuestion(
            question_number=2,
            title="TCP Sliding Window Sizing (BDP)",
            question_type="Calculations",
            prompt_text="Consider an FTP connection over a path with Bandwidth R = 200 Mbps and RTT = 50 ms. For 100% channel utilization without transmitter idle periods, what is the minimum Sliding Window size in MB?",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Bandwidth-Delay Product (BDP) Calculation",
                    formula="Window Size = Bandwidth * RTT",
                    substitution="(200 * 10^6 bps) * 0.050 s",
                    result="10,000,000 bits",
                    rationale="Volume of data emitted during one Round Trip Time.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Conversion to Bytes and Megabytes",
                    formula="Window (Bytes) = 10,000,000 / 8",
                    substitution="1,250,000 Bytes",
                    result="1.25 MBytes",
                    rationale="A window of at least 1.25 MB is required to prevent the sender from pausing while awaiting ACKs.",
                ),
            ],
            detailed_justification="Window = Bandwidth * RTT = 200 Mbps * 0.05 s = 10 Mbits = 1.25 MB.",
        ),
        ExamQuestion(
            question_number=3,
            title="Hamming Code Construction (d = 4 bits, Odd Parity)",
            question_type="Calculations",
            prompt_text="A sender wishes to transmit data word D = 1101 using a Hamming code with Odd Parity. Determine the required number of parity bits p and the final transmitted 7-bit codeword.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Determining Number of Parity Bits p",
                    formula="2^p >= d + p + 1",
                    substitution="2^p >= 4 + p + 1  <=>  2^p >= p + 5",
                    result="p = 3 bits (since 2^3 = 8 >= 8)",
                    rationale="3 parity bits are required at bit positions 1, 2, 4 (powers of 2), giving total length 7 bits.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Parity Bit Calculation (Odd Parity)",
                    formula="P1 (positions 1,3,5,7), P2 (2,3,6,7), P4 (4,5,6,7)",
                    substitution="D = 1101 placed at (3,5,6,7) -> D1=1, D2=1, D3=0, D4=1",
                    result="P1=0, P2=1, P4=1",
                    rationale="Under odd parity, the total number of 1s in each check set must be odd.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Final Transmitted 7-Bit Codeword",
                    formula="[P1, P2, D1, P4, D2, D3, D4]",
                    substitution="[0, 1, 1, 1, 1, 0, 1]",
                    result="0111101",
                    rationale="The resulting codeword enables single-bit error detection and automatic forward error correction.",
                ),
            ],
            detailed_justification="Hamming(7,4) code: 4 data bits + 3 parity bits = 7 bits (0111101).",
        ),
    ]

    nodes = [
        TopologyNode("n_a", "Node A", "router", 120, 150, "10.0.1.1"),
        TopologyNode("n_b", "Node B", "router", 320, 80, "10.0.1.2"),
        TopologyNode("n_c", "Node C", "router", 320, 220, "10.0.2.2"),
        TopologyNode("n_d", "Node D", "router", 520, 150, "10.0.3.1"),
        TopologyNode("n_g", "Node G", "host", 750, 150, "10.0.4.1"),
    ]

    links = [
        TopologyLink("n_a", "n_b", 100, 10.0, 2.0, "fiber", "Cost: 2"),
        TopologyLink("n_a", "n_c", 100, 5.0, 2.0, "copper", "Cost: 1"),
        TopologyLink("n_a", "n_d", 100, 15.0, 2.0, "fiber", "Cost: 3"),
        TopologyLink("n_d", "n_g", 100, 10.0, 2.0, "fiber", "Cost: 2"),
    ]

    return NetworkScenario(
        id="exam_synth_4",
        title="Synthetic Exam 4: TCP BDP, Dijkstra & Hamming",
        subtitle="Encapsulation, TCP Sliding Window (BDP = 1.25MB), Dijkstra & Hamming(7,4)",
        course_tag="Synthetic Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Encapsulation: Header addition per layer.",
            "2. TCP Sliding Window = Bandwidth * RTT = 200 Mbps * 50 ms = 1.25 MB.",
            "3. Hamming(7,4): 2^p >= d + p + 1 (p = 3 bits).",
        ],
        calculator_type="delay",
    )
