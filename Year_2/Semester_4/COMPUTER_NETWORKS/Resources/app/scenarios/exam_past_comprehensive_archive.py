"""Past Exam Comprehensive Archive Scenario Module.

Contains all questions from the archival exam paper:
- The 4 Nodal Delays (d_proc, d_queue, d_trans, d_prop)
- Bandwidth-Delay Product (BDP)
- OSPF Area Configuration
- BGP Path Routing & Autonomous Systems
- Multi-hop RTT Calculations with Intermediate Router Processing
- Dijkstra Shortest Path Algorithm Execution
- CSMA/CD Minimum Frame Size Criteria
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
    """Constructs and returns the comprehensive archival exam scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="The archival examination paper "),
                TextSegment(
                    text="Computer Networks (Comprehensive Archive)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ARCHIVE",
                    tooltip="Comprehensive examination across all course modules",
                ),
                TextSegment(text=" provides an exhaustive analysis of "),
                TextSegment(
                    text="Nodal Delay d_nodal = d_proc + d_queue + d_trans + d_prop",
                    is_highlight=True,
                    category="delay",
                    tag_label="4 DELAYS",
                    tooltip="Analysis of the 4 nodal delay components",
                ),
                TextSegment(text=", evaluation of the "),
                TextSegment(
                    text="BDP (Bandwidth-Delay Product)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP",
                    tooltip="Link capacity in bits",
                ),
                TextSegment(text=" and configuration of "),
                TextSegment(
                    text="OSPF in a Single Area",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF",
                    tooltip="Open Shortest Path First routing configuration",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="The second section analyzes inter-domain routing between "),
                TextSegment(
                    text="Autonomous Systems (BGP)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP",
                    tooltip="Hot Potato routing vs shortest AS path",
                ),
                TextSegment(text=", calculations of "),
                TextSegment(
                    text="RTT with intermediate processing d_proc = 0.02 ms",
                    is_highlight=True,
                    category="delay",
                    tag_label="RTT",
                    tooltip="Round-trip time with nodal processing",
                ),
                TextSegment(text=", execution of the "),
                TextSegment(
                    text="Dijkstra algorithm on an 11-node topology",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA LSA",
                    tooltip="Shortest path calculation from node a to node k",
                ),
                TextSegment(text=" and determination of the "),
                TextSegment(
                    text="CSMA/CD Minimum Frame Size",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD",
                    tooltip="L_min = 2 * d_prop * R = 512 bits = 64 Bytes",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Analysis of the 4 Nodal Delay Components",
            question_type="Theory Analysis",
            prompt_text="Formulate the total end-to-end nodal delay as a mathematical expression and explain each of the 4 constituent terms in detail.",
            detailed_justification=(
                "Total nodal delay is expressed as: **d_nodal = d_proc + d_queue + d_trans + d_prop**\n\n"
                "1. **d_proc (Processing Delay):** Time spent inspecting packet headers, resolving the output port via forwarding table lookups, and verifying checksum integrity (typically microseconds).\n"
                "2. **d_queue (Queuing Delay):** Waiting time spent inside router buffer queues until the transmission link becomes idle. Depends directly on network traffic intensity and arrival distribution.\n"
                "3. **d_trans (Transmission Delay):** d_trans = L / R, where L represents packet length in bits and R represents channel bandwidth in bps.\n"
                "4. **d_prop (Propagation Delay):** d_prop = d / s, where d is physical link distance and s is signal propagation velocity in the transmission medium (e.g. 2*10^8 m/s in copper/fiber)."
            ),
            common_pitfalls=[
                "Confusing transmission delay (L/R) with propagation delay (d/s).",
                "Omitting queuing or processing delay when evaluating real-world routers.",
            ],
        ),
        ExamQuestion(
            question_number=2,
            title="Bandwidth-Delay Product (BDP) Calculation",
            question_type="Calculations",
            prompt_text="Consider a link with Bandwidth R = 1000 KB/s and one-way delay D = 5 ms. What is the maximum number of bits that can be 'in flight' across the link simultaneously?",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Unit Conversion for Bandwidth and Delay",
                    formula="R = 1000 KB/s = 1000 * 8000 bps = 8,000,000 bps, D = 5 ms = 0.005 s",
                    substitution="BDP = R * D",
                    result="8,000,000 bps * 0.005 s",
                    rationale="The Bandwidth-Delay Product defines the physical bit capacity of the transmission pipeline.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Final Calculation in Bits and Bytes",
                    formula="BDP = 40,000 bits",
                    substitution="40,000 bits / 8 bits per byte",
                    result="5,000 Bytes (5 KB)",
                    rationale="To maintain 100% link utilization, the sender's window must be sized to at least 5 KB.",
                ),
            ],
            detailed_justification="The BDP represents the volume of data required to fill the physical medium. In high-speed long-distance links (Long Fat Networks - LFNs), the BDP is exceptionally large.",
        ),
        ExamQuestion(
            question_number=3,
            title="Multi-hop RTT Calculation with Intermediate Processing (A -> C -> A)",
            question_type="Calculations",
            prompt_text="Consider 2 consecutive links (A-B and B-C) with R1 = R2 = 10 Mbps, L1 = 100 km, L2 = 50 km, and propagation speed u = 2.5 * 10^8 m/s. A packet of size L = 10,000 bits is sent from A to C and immediately echoed back. Each node incurs processing delay d_proc = 0.02 ms. Calculate the total RTT.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Transmission Delay per Hop",
                    formula="d_trans = L / R = 10,000 / (10 * 10^6)",
                    substitution="10,000 / 10,000,000",
                    result="1 ms",
                    rationale="Transmitting the packet takes 1 ms at each hop.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Propagation Delays",
                    formula="d_prop1 = 100,000m / 2.5*10^8 = 0.4 ms, d_prop2 = 50,000m / 2.5*10^8 = 0.2 ms",
                    substitution="d_prop_oneway = 0.4 + 0.2",
                    result="0.6 ms one-way",
                    rationale="Total round-trip propagation delay across both links = 2 * 0.6 = 1.2 ms.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Total Round-Trip Time (RTT)",
                    formula="RTT = 4 * d_trans + 2 * d_prop_oneway + d_proc_total",
                    substitution="4 * 1.0ms + 2 * 0.6ms + 3 * 0.02ms (at intermediate/terminal hops)",
                    result="5.26 ms",
                    rationale="The packet is transmitted 4 times (A->B, B->C, C->B, B->A) and propagates twice across each link.",
                ),
            ],
            detailed_justification="The RTT must account for all Store-and-Forward transmissions along both the outbound path and the return path, plus processing delays at all intermediate forwarding nodes.",
        ),
    ]

    nodes = [
        TopologyNode("node_a", "Node A", "host", 100, 150, "10.0.1.1", "00:11:22:33:44:01"),
        TopologyNode("node_b", "Router B", "router", 380, 150, "10.0.1.2", "00:11:22:33:44:02"),
        TopologyNode("node_c", "Node C", "host", 660, 150, "10.0.2.1", "00:11:22:33:44:03"),
    ]

    links = [
        TopologyLink("node_a", "node_b", 10, 100.0, 2.5, "fiber", "10M | 100km"),
        TopologyLink("node_b", "node_c", 10, 50.0, 2.5, "fiber", "10M | 50km"),
    ]

    return NetworkScenario(
        id="exam_past_archive",
        title="Exam Questions (Comprehensive Archive)",
        subtitle="4 Nodal Delays, BDP Product, OSPF, BGP Routing & Multi-hop RTT",
        course_tag="Past Exam",
        duration_info="2 hours and 15 minutes",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_nodal = d_proc + d_queue + d_trans + d_prop.",
            "2. BDP = Bandwidth * Delay (Maximum in-flight bits).",
            "3. Multi-hop RTT = Sum(d_trans_out + d_trans_back) + 2*Sum(d_prop) + Sum(d_proc).",
        ],
        calculator_type="delay",
    )
