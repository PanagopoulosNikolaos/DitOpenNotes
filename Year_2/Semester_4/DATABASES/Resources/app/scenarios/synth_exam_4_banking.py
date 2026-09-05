"""Banking Management and Transactions case study scenario module.

Contains the complete parsed and modeled ER analysis for the Core Banking System
(Branches, Employees, Customers, Bank Accounts, Account Transactions, Loans),
including full attribute breakdowns, relationship cardinalities, keys analysis, Crow's Foot
ER diagram layout, relational schema mapping, and SQL DDL.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    Entity,
    Attribute,
    RelationshipAttribute,
    KeyAnalysisRow,
    Relationship,
    ERTable,
    ERTableAttr,
    EREdge,
    RelationalJustification,
)


def createBankingManagementScenario() -> Scenario:
    """Constructs and returns the Banking Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="A banking group is designing a new core information system to manage "),
                TextSegment(
                    text="branches",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Autonomous banking branch with unique Branch Code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="customers",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Natural person customer with unique Tax ID (AFM).",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="bank accounts",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Bank account with international IBAN code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="loans",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Loan contract with unique loan number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="transactions / movements",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Weak Entity: Account transaction existentially dependent on the bank account.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="banking staff",
                    is_highlight=True,
                    category="entity",
                    tag_label="ENTITY",
                    badge_class="badge-entity-strong",
                    tooltip="Strong Entity: Bank employee with unique Employee ID (AMY).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Banking Branches:</strong> Each branch possesses a "),
                TextSegment(
                    text="unique branch number (Branch Code)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique branch code.",
                ),
                TextSegment(text=", a "),
                TextSegment(
                    text="unique branch name (e.g., 'Central Syntagma')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique branch commercial name.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="host city", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", and its "),
                TextSegment(text="annual operating budget", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each branch is "),
                TextSegment(
                    text="mandatorily managed by a specific employee (Branch Manager)",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:1",
                    badge_class="badge-rel-11",
                    tooltip="1:1 Relationship (MANAGES): Total participation for Branch, partial for Employee.",
                ),
                TextSegment(text=". For each manager, the "),
                TextSegment(
                    text="appointment date",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="Relationship Attribute: Embedded in BRANCH table as Foreign Key attribute.",
                ),
                TextSegment(text=". An employee may manage at most one branch."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Banking Staff & Hierarchy:</strong> For each employee, the following are recorded: the "),
                TextSegment(
                    text="Employee ID Number (AMY)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique staff employee registry number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="Tax ID (AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique employee tax identification number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="monthly salary", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="hire date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(
                    text="residential address (street, number, city)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into street, number, and city.",
                ),
                TextSegment(text=". Each employee "),
                TextSegment(
                    text="belongs mandatorily to a specific branch where they work",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (WORKS_IN): A branch employs multiple employees.",
                ),
                TextSegment(text=". Within the managerial hierarchy, "),
                TextSegment(
                    text="each employee (except the General Manager) is directly supervised by another senior employee (supervisor)",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Recursive 1:N Relationship (SUPERVISES): Self-referencing link on EMPLOYEE entity.",
                ),
                TextSegment(text=", while a supervisor may supervise multiple employees."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Bank Customers:</strong> For each customer (natural person), the following are recorded: the "),
                TextSegment(
                    text="unique Tax ID (AFM)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique customer tax identification number.",
                ),
                TextSegment(text=", the "),
                TextSegment(
                    text="National ID Number (ADT)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Candidate Key: Unique police identification card number.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="first name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="last name", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="date of birth", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(
                    text="residential address (composite: street, number, postal code, city)",
                    is_highlight=True,
                    category="attr",
                    tag_label="COMPOSITE",
                    badge_class="badge-attr-composite",
                    tooltip="Composite Attribute: Decomposed into street, number, postal code, city.",
                ),
                TextSegment(text=" and the "),
                TextSegment(text="credit score", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". A customer may register one or more "),
                TextSegment(
                    text="contact telephone numbers (landline, mobile, work)",
                    is_highlight=True,
                    category="attr",
                    tag_label="MULTIVALUED",
                    badge_class="badge-attr-multi",
                    tooltip="Multivalued Attribute: Requires a separate CUSTOMER_PHONE table.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Bank Accounts & Co-Holders:</strong> Each account is identified by its "),
                TextSegment(
                    text="international IBAN code (unique)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique account IBAN code.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="current balance", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="account type (e.g., 'Savings', 'Checking', 'Payroll')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="opening date", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each account is "),
                TextSegment(
                    text="opened at a specific branch",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (OPENED_AT): A branch services multiple accounts.",
                ),
                TextSegment(text=". An account may have "),
                TextSegment(
                    text="more than one joint co-holder customer (joint account), and a customer may hold multiple accounts",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (HOLDS_ACCOUNT): Implemented via junction table ACCOUNT_HOLDER.",
                ),
                TextSegment(text=". For each customer-account relationship, the "),
                TextSegment(
                    text="holder status (e.g., 'Primary Holder', 'Joint Holder')",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="N:M Relationship Attribute: Stored in table ACCOUNT_HOLDER.",
                ),
                TextSegment(text=" and the "),
                TextSegment(
                    text="addition date to the account",
                    is_highlight=True,
                    category="attr",
                    tag_label="REL ATTRIBUTE",
                    badge_class="badge-attr-simple",
                    tooltip="N:M Relationship Attribute: Stored in table ACCOUNT_HOLDER.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Account Transactions:</strong> Each time a transaction is executed on an account, a new movement is recorded. Each transaction is characterized by a "),
                TextSegment(
                    text="sequential transaction number within the specific account",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Partial Key (Discriminator): Identifies the transaction only in combination with the IBAN.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="exact transaction timestamp", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="amount", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="transaction type ('Deposit', 'Withdrawal', 'Payment', 'Transfer')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="service channel (e.g., 'ATM', 'Web Banking', 'Branch')", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="A transaction cannot exist autonomously without its corresponding bank account",
                    is_highlight=True,
                    category="entity",
                    tag_label="WEAK ENTITY",
                    badge_class="badge-entity-weak",
                    tooltip="Existential Dependency: Identifying owner entity is BANK_ACCOUNT.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Bank Loans:</strong> Each loan has a "),
                TextSegment(
                    text="unique loan number",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Primary Key: Unique loan contract code.",
                ),
                TextSegment(text=", the "),
                TextSegment(text="original approved principal", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="current outstanding balance", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=", the "),
                TextSegment(text="interest rate", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=" and the "),
                TextSegment(text="duration in months", is_highlight=True, category="attr", tag_label="ATTRIBUTE", badge_class="badge-attr-simple"),
                TextSegment(text=". Each loan is "),
                TextSegment(
                    text="granted by a specific banking branch",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="1:N Relationship (GRANTED_BY): Each loan is issued by one branch.",
                ),
                TextSegment(text=" and "),
                TextSegment(
                    text="associated with one or more borrower customers",
                    is_highlight=True,
                    category="rel",
                    tag_label="RELATIONSHIP N:M",
                    badge_class="badge-rel-nm",
                    tooltip="N:M Relationship (BORROWER): A loan may have co-borrowers and a customer may hold multiple loans.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="BRANCH",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous administrative unit of the banking group with independent existence and unique Branch Code.",
            attributes=[
                Attribute("branch_code", "Simple / Single-valued", is_pk=True, notes="Unique branch code (PK)"),
                Attribute("branch_name", "Simple / Single-valued", is_candidate=True, notes="Unique commercial branch name (Candidate Key)"),
                Attribute("city", "Simple / Single-valued", notes="Branch headquarters city"),
                Attribute("annual_budget", "Simple / Single-valued", notes="Annual operating budget"),
            ],
        ),
        Entity(
            name="EMPLOYEE",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Natural person banking employee with independent existence and unique AMY and AFM identifiers.",
            attributes=[
                Attribute("amy", "Simple / Single-valued", is_pk=True, notes="Employee Registration Number (PK)"),
                Attribute("afm", "Simple / Single-valued", is_candidate=True, notes="Tax ID (Candidate Key)"),
                Attribute("first_name", "Simple / Single-valued", notes="Employee first name"),
                Attribute("last_name", "Simple / Single-valued", notes="Employee last name"),
                Attribute("salary", "Simple / Single-valued", notes="Monthly gross salary"),
                Attribute("hire_date", "Simple / Single-valued", notes="Hiring date"),
                Attribute("address", "Composite", components=["street", "number", "city"], notes="Residential address (street, number, city)"),
            ],
        ),
        Entity(
            name="CUSTOMER",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Natural person customer interacting with the bank, with unique AFM and identity card number.",
            attributes=[
                Attribute("afm", "Simple / Single-valued", is_pk=True, notes="Tax ID (PK)"),
                Attribute("adt", "Simple / Single-valued", is_candidate=True, notes="National ID Card Number (Candidate Key)"),
                Attribute("first_name", "Simple / Single-valued", notes="Customer first name"),
                Attribute("last_name", "Simple / Single-valued", notes="Customer last name"),
                Attribute("birth_date", "Simple / Single-valued", notes="Date of birth"),
                Attribute("address", "Composite", components=["street", "number", "postal_code", "city"], notes="Residential address (street, number, postal code, city)"),
                Attribute("credit_score", "Simple / Single-valued", notes="Credit rating evaluation score"),
                Attribute("phones", "Multivalued", notes="Multiple contact phone numbers (Table CUSTOMER_PHONE)"),
            ],
        ),
        Entity(
            name="BANK_ACCOUNT",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous financial entity with globally unique IBAN account number.",
            attributes=[
                Attribute("iban", "Simple / Single-valued", is_pk=True, notes="International Bank Account Number (PK)"),
                Attribute("balance", "Simple / Single-valued", notes="Current ledger balance"),
                Attribute("account_type", "Simple / Single-valued", notes="Type ('Savings', 'Checking', 'Payroll')"),
                Attribute("opening_date", "Simple / Single-valued", notes="Account opening date"),
            ],
        ),
        Entity(
            name="ACCOUNT_TRANSACTION",
            entity_type="Weak Entity",
            is_weak=True,
            owner_entity="BANK_ACCOUNT",
            justification="Weak entity existentially and identifiably dependent on bank account. No transaction exists without an IBAN.",
            attributes=[
                Attribute("transaction_number", "Simple / Single-valued", is_partial=True, notes="Partial Key (Discriminator) within the account"),
                Attribute("transaction_timestamp", "Simple / Single-valued", notes="Exact timestamp of transaction execution"),
                Attribute("amount", "Simple / Single-valued", notes="Transaction monetary amount"),
                Attribute("transaction_type", "Simple / Single-valued", notes="Type ('Deposit', 'Withdrawal', 'Payment', 'Transfer')"),
                Attribute("channel", "Simple / Single-valued", notes="Channel ('ATM', 'Web Banking', 'Branch')"),
            ],
        ),
        Entity(
            name="LOAN",
            entity_type="Strong Entity",
            is_weak=False,
            owner_entity=None,
            justification="Autonomous loan contract with unique Loan Number.",
            attributes=[
                Attribute("loan_number", "Simple / Single-valued", is_pk=True, notes="Unique loan contract number (PK)"),
                Attribute("original_amount", "Simple / Single-valued", notes="Original approved principal amount"),
                Attribute("outstanding_balance", "Simple / Single-valued", notes="Current outstanding owed balance"),
                Attribute("interest_rate", "Simple / Single-valued", notes="Annual lending interest rate (%)"),
                Attribute("duration_months", "Simple / Single-valued", notes="Total repayment duration in months"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="appointment_date",
            relationship_name="MANAGES (BRANCH - EMPLOYEE)",
            justification="Date on which the employee assumed management duties at the branch (embedded in BRANCH table).",
        ),
        RelationshipAttribute(
            name="holder_status",
            relationship_name="HOLDS_ACCOUNT (CUSTOMER - BANK_ACCOUNT)",
            justification="Customer classification as 'Primary Holder' or 'Joint Holder' for the specific joint account.",
        ),
        RelationshipAttribute(
            name="addition_date",
            relationship_name="HOLDS_ACCOUNT (CUSTOMER - BANK_ACCOUNT)",
            justification="Date on which the co-holder was added to the bank account.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="BRANCH",
            key_count="2 Candidate",
            key_types="Candidate: {branch_code}, {branch_name}",
            final_pk_selection="branch_code",
            justification="Compact, stable, numeric identifier optimal for Primary Key and Foreign Key indexing.",
        ),
        KeyAnalysisRow(
            entity_name="EMPLOYEE",
            key_count="2 Candidate",
            key_types="Candidate: {amy}, {afm}",
            final_pk_selection="amy",
            justification="Internal registry number (AMY) is compact and invariant, while AFM is protected as Unique Candidate Key.",
        ),
        KeyAnalysisRow(
            entity_name="CUSTOMER",
            key_count="2 Candidate",
            key_types="Candidate: {afm}, {adt}",
            final_pk_selection="afm",
            justification="AFM is the official, invariant tax identification number across all financial institutions.",
        ),
        KeyAnalysisRow(
            entity_name="BANK_ACCOUNT",
            key_count="1 Candidate",
            key_types="Candidate: {iban}",
            final_pk_selection="iban",
            justification="Global IBAN standard code uniquely identifies every account internationally.",
        ),
        KeyAnalysisRow(
            entity_name="ACCOUNT_TRANSACTION",
            key_count="Weak (1 Partial)",
            key_types="Partial Key: {transaction_number}",
            final_pk_selection="(iban, transaction_number)",
            justification="Composite primary key consisting of the owner entity Foreign Key and sequential transaction number.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="LOAN",
            key_count="1 Candidate",
            key_types="Candidate: {loan_number}",
            final_pk_selection="loan_number",
            justification="Unique loan contract code issued by the credit approval system.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="a",
            name="MANAGES",
            connected_entities="BRANCH <-> EMPLOYEE",
            cardinality="1:1",
            participation="Total for Branch (1,1), Partial for Employee (0,1)",
            relationship_type="Regular Relationship",
            attributes=["appointment_date"],
            justification="Each branch is mandatorily managed by one manager. An employee can manage at most one branch or none.",
        ),
        Relationship(
            letter_id="b",
            name="WORKS_IN",
            connected_entities="BRANCH <-> EMPLOYEE",
            cardinality="1:N",
            participation="Total for Employee (1,1), Total for Branch (1,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each employee belongs mandatorily to one branch. A branch employs multiple employees.",
        ),
        Relationship(
            letter_id="c",
            name="SUPERVISES",
            connected_entities="EMPLOYEE <-> EMPLOYEE",
            cardinality="1:N",
            participation="Partial for Supervisor (0,N), Partial for Subordinate (0,1)",
            relationship_type="Recursive 1:N Relationship",
            attributes=[],
            justification="A supervisor supervises multiple employees. Each employee is supervised by one supervisor (except the General Manager with 0).",
        ),
        Relationship(
            letter_id="d",
            name="ACCOUNT_OPENING",
            connected_entities="BRANCH <-> BANK_ACCOUNT",
            cardinality="1:N",
            participation="Total for Account (1,1), Partial for Branch (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each account is opened at a specific servicing branch. A branch maintains multiple accounts.",
        ),
        Relationship(
            letter_id="e",
            name="ACCOUNT_OWNERSHIP",
            connected_entities="CUSTOMER <-> BANK_ACCOUNT",
            cardinality="N:M",
            participation="Total for Account (1,N), Partial for Customer (0,N)",
            relationship_type="Associative Entity (Junction)",
            attributes=["holder_status", "addition_date"],
            justification="An account may have multiple joint co-holders and a customer may hold multiple accounts.",
        ),
        Relationship(
            letter_id="f",
            name="CONTAINS_TRANSACTION",
            connected_entities="BANK_ACCOUNT <-> ACCOUNT_TRANSACTION",
            cardinality="1:N",
            participation="Total for Transaction (1,1), Partial for Account (0,N)",
            relationship_type="Identifying Relationship",
            attributes=[],
            justification="Identifying relationship of weak entity ACCOUNT_TRANSACTION from identifying BANK_ACCOUNT.",
        ),
        Relationship(
            letter_id="g",
            name="LOAN_GRANTING",
            connected_entities="BRANCH <-> LOAN",
            cardinality="1:N",
            participation="Total for Loan (1,1), Partial for Branch (0,N)",
            relationship_type="Regular Relationship",
            attributes=[],
            justification="Each loan is issued by a specific branch of the bank.",
        ),
        Relationship(
            letter_id="h",
            name="LOAN_BORROWERS",
            connected_entities="CUSTOMER <-> LOAN",
            cardinality="N:M",
            participation="Total for Loan (1,N), Partial for Customer (0,N)",
            relationship_type="Associative Entity (Junction)",
            attributes=[],
            justification="A loan may have a primary borrower and guarantors/co-signers, and a customer may obtain multiple loans.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "The General Manager has no supervisor (supervisor_amy IS NULL) in the recursive hierarchy.",
        "Each bank account has at least one primary holder (holder_status = 'Primary Holder').",
        "Customer contact phone numbers are extracted to an independent relational table CUSTOMER_PHONE with composite primary key (afm, phone_number).",
        "Account transactions are numbered sequentially (1, 2, 3, ...) per account (transaction_number).",
        "The 1:1 branch management relationship is implemented with Foreign Key manager_amy in table BRANCH with a UNIQUE constraint.",
    ]

    # 7. ER Diagram Tables (Coordinates & Attributes for Crow's Foot Diagram)
    er_tables = [
        ERTable(
            id="t-branch",
            label="BRANCH",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("branch_code", pk=True),
                ERTableAttr("branch_name"),
                ERTableAttr("city"),
                ERTableAttr("annual_budget"),
                ERTableAttr("manager_amy", fk=True),
                ERTableAttr("appointment_date"),
            ],
        ),
        ERTable(
            id="t-employee",
            label="EMPLOYEE",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("amy", pk=True),
                ERTableAttr("afm"),
                ERTableAttr("first_name"),
                ERTableAttr("last_name"),
                ERTableAttr("salary"),
                ERTableAttr("hire_date"),
                ERTableAttr("address_street"),
                ERTableAttr("address_number"),
                ERTableAttr("address_city"),
                ERTableAttr("branch_code", fk=True),
                ERTableAttr("supervisor_amy", fk=True),
            ],
        ),
        ERTable(
            id="t-customer",
            label="CUSTOMER",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("afm", pk=True),
                ERTableAttr("adt"),
                ERTableAttr("first_name"),
                ERTableAttr("last_name"),
                ERTableAttr("birth_date"),
                ERTableAttr("street"),
                ERTableAttr("street_number"),
                ERTableAttr("postal_code"),
                ERTableAttr("city"),
                ERTableAttr("credit_score"),
            ],
        ),
        ERTable(
            id="t-cust-phone",
            label="CUSTOMER_PHONE",
            x=850,
            y=430,
            attrs=[
                ERTableAttr("afm", pk=True, fk=True),
                ERTableAttr("phone_number", pk=True),
                ERTableAttr("phone_type"),
            ],
        ),
        ERTable(
            id="t-account",
            label="BANK_ACCOUNT",
            x=50,
            y=390,
            attrs=[
                ERTableAttr("iban", pk=True),
                ERTableAttr("balance"),
                ERTableAttr("account_type"),
                ERTableAttr("opening_date"),
                ERTableAttr("branch_code", fk=True),
            ],
        ),
        ERTable(
            id="t-transaction",
            label="ACCOUNT_TRANSACTION",
            x=50,
            y=640,
            attrs=[
                ERTableAttr("iban", pk=True, fk=True),
                ERTableAttr("transaction_number", pk=True),
                ERTableAttr("transaction_timestamp"),
                ERTableAttr("amount"),
                ERTableAttr("transaction_type"),
                ERTableAttr("channel"),
            ],
        ),
        ERTable(
            id="t-account-holder",
            label="ACCOUNT_HOLDER",
            x=450,
            y=430,
            attrs=[
                ERTableAttr("iban", pk=True, fk=True),
                ERTableAttr("afm", pk=True, fk=True),
                ERTableAttr("holder_status"),
                ERTableAttr("addition_date"),
            ],
        ),
        ERTable(
            id="t-loan",
            label="LOAN",
            x=450,
            y=640,
            attrs=[
                ERTableAttr("loan_number", pk=True),
                ERTableAttr("original_amount"),
                ERTableAttr("outstanding_balance"),
                ERTableAttr("interest_rate"),
                ERTableAttr("duration_months"),
                ERTableAttr("branch_code", fk=True),
            ],
        ),
        ERTable(
            id="t-borrower",
            label="LOAN_BORROWER",
            x=850,
            y=640,
            attrs=[
                ERTableAttr("loan_number", pk=True, fk=True),
                ERTableAttr("afm", pk=True, fk=True),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Branch directs Employee (1:1)
        EREdge("M 310 80 L 450 80", "start-one-mandatory", "end-one-optional", "Manages (1:1)", 380, 70),
        # Branch employs Employees (1:N)
        EREdge("M 310 120 L 450 120", "start-one-mandatory", "end-many-mandatory", "Works In (1:N)", 380, 135),
        # Employee recursive supervisor (1:N)
        EREdge("M 650 90 C 720 30, 720 170, 650 150", "start-one-optional", "end-many-optional", "Supervises (1:N)", 730, 100),
        # Branch opens Accounts (1:N)
        EREdge("M 150 210 L 150 390", "start-one-mandatory", "end-many-mandatory", "Opens Account (1:N)", 165, 300),
        # Account contains Movements (1:N identifying)
        EREdge("M 150 530 L 150 640", "start-one-mandatory", "end-many-mandatory", "Contains Movement (1:N)", 165, 585),
        # Account to Co-holders (1:N)
        EREdge("M 310 430 L 450 430", "start-one-mandatory", "end-many-mandatory", "Co-holders (1:N)", 380, 420),
        # Customer to Co-holders (1:N)
        EREdge("M 850 160 L 710 430", "start-one-optional", "end-many-mandatory", "Holds (1:N)", 780, 300),
        # Customer to Phone numbers (1:N)
        EREdge("M 980 378 L 980 430", "start-one-optional", "end-many-mandatory", "Has Phone (1:N)", 995, 400),
        # Branch issues Loans (1:N)
        EREdge("M 200 210 L 450 670", "start-one-mandatory", "end-many-mandatory", "Issues Loan (1:N)", 310, 480),
        # Loan to Borrowers (1:N)
        EREdge("M 650 680 L 850 680", "start-one-mandatory", "end-many-mandatory", "Borrower (1:N)", 750, 670),
        # Customer to Borrowers (1:N routed around phone table)
        EREdge("M 1110 200 L 1140 200 L 1140 680 L 1110 680", "start-one-optional", "end-many-mandatory", "Receives Loan (1:N)", 1150, 440),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Conversion of Strong Entities (BRANCH, EMPLOYEE, CUSTOMER, BANK_ACCOUNT, LOAN)",
            color_class="border-blue-500",
            description="Each strong entity is converted into an independent table with its primary key selected from candidate keys (branch_code, amy, afm, iban, loan_number). Composite address attributes are decomposed into atomic columns.",
        ),
        RelationalJustification(
            title="2. Conversion of Weak Entity (ACCOUNT_TRANSACTION)",
            color_class="border-red-500",
            description="Table ACCOUNT_TRANSACTION receives primary key iban from identifying owner entity BANK_ACCOUNT as Foreign Key. The primary key is composite: PRIMARY KEY (iban, transaction_number) with ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Conversion of 1:1 and 1:N Relationships (MANAGES, WORKS_IN, SUPERVISES, ACCOUNT_OPENING, LOAN_GRANTING)",
            color_class="border-emerald-500",
            description="In 1:1 relationship MANAGES, Foreign Key manager_amy and attribute appointment_date are placed in table BRANCH with a UNIQUE constraint. In 1:N relationships, the PK of side 1 is placed as FK on side N.",
        ),
        RelationalJustification(
            title="4. Conversion of N:M Relationships (ACCOUNT_OWNERSHIP, LOAN_BORROWERS)",
            color_class="border-amber-500",
            description="Junction tables ACCOUNT_HOLDER (composite PK iban + afm and relationship attributes) and LOAN_BORROWER (composite PK loan_number + afm) are created.",
        ),
        RelationalJustification(
            title="5. Conversion of Multivalued Attribute (CUSTOMER_PHONES)",
            color_class="border-purple-500",
            description="The multivalued phone attribute is extracted to table CUSTOMER_PHONE with composite primary key PRIMARY KEY (afm, phone_number) and FOREIGN KEY (afm) REFERENCES CUSTOMER(afm) ON DELETE CASCADE.",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Banking System
-- Case Study: Exam Paper 4 (Banking Group & Transactions)
-- ==========================================================

-- 1. Entity: EMPLOYEE (Pre-created for foreign keys)
CREATE TABLE EMPLOYEE (
    amy VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(9) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL CHECK (salary > 0),
    hire_date DATE NOT NULL,
    address_street VARCHAR(50) NOT NULL,
    address_number VARCHAR(10) NOT NULL,
    address_city VARCHAR(50) NOT NULL,
    branch_code VARCHAR(10) NOT NULL,
    supervisor_amy VARCHAR(15),
    FOREIGN KEY (supervisor_amy) REFERENCES EMPLOYEE(amy) ON DELETE SET NULL
);

-- 2. Entity: BRANCH
CREATE TABLE BRANCH (
    branch_code VARCHAR(10) PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(50) NOT NULL,
    annual_budget DECIMAL(14, 2) NOT NULL CHECK (annual_budget >= 0),
    manager_amy VARCHAR(15) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (manager_amy) REFERENCES EMPLOYEE(amy)
);

-- Add circular foreign key for Employee's workplace
ALTER TABLE EMPLOYEE
ADD CONSTRAINT fk_emp_branch
FOREIGN KEY (branch_code) REFERENCES BRANCH(branch_code);

-- 3. Entity: CUSTOMER
CREATE TABLE CUSTOMER (
    afm VARCHAR(9) PRIMARY KEY,
    adt VARCHAR(15) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    street VARCHAR(50) NOT NULL,
    street_number VARCHAR(10) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL,
    credit_score INT NOT NULL CHECK (credit_score BETWEEN 300 AND 850)
);

-- 4. Multi-valued Attribute: CUSTOMER_PHONE
CREATE TABLE CUSTOMER_PHONE (
    afm VARCHAR(9) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    phone_type VARCHAR(20) DEFAULT 'Mobile',
    PRIMARY KEY (afm, phone_number),
    FOREIGN KEY (afm) REFERENCES CUSTOMER(afm) ON DELETE CASCADE
);

-- 5. Entity: BANK_ACCOUNT
CREATE TABLE BANK_ACCOUNT (
    iban VARCHAR(34) PRIMARY KEY,
    balance DECIMAL(14, 2) NOT NULL DEFAULT 0.00,
    account_type VARCHAR(30) NOT NULL CHECK (account_type IN ('Savings', 'Checking', 'Payroll', 'Fixed Deposit')),
    opening_date DATE NOT NULL,
    branch_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (branch_code) REFERENCES BRANCH(branch_code)
);

-- 6. Weak Entity: ACCOUNT_TRANSACTION
CREATE TABLE ACCOUNT_TRANSACTION (
    iban VARCHAR(34) NOT NULL,
    transaction_number INT NOT NULL,
    transaction_timestamp TIMESTAMP NOT NULL,
    amount DECIMAL(12, 2) NOT NULL CHECK (amount > 0),
    transaction_type VARCHAR(30) NOT NULL CHECK (transaction_type IN ('Deposit', 'Withdrawal', 'Payment', 'Transfer')),
    channel VARCHAR(30) NOT NULL CHECK (channel IN ('ATM', 'Web Banking', 'Branch', 'Mobile App')),
    PRIMARY KEY (iban, transaction_number),
    FOREIGN KEY (iban) REFERENCES BANK_ACCOUNT(iban) ON DELETE CASCADE
);

-- 7. Junction Table: ACCOUNT_HOLDER (N:M)
CREATE TABLE ACCOUNT_HOLDER (
    iban VARCHAR(34) NOT NULL,
    afm VARCHAR(9) NOT NULL,
    holder_status VARCHAR(30) NOT NULL CHECK (holder_status IN ('Primary Holder', 'Joint Holder')),
    addition_date DATE NOT NULL,
    PRIMARY KEY (iban, afm),
    FOREIGN KEY (iban) REFERENCES BANK_ACCOUNT(iban) ON DELETE CASCADE,
    FOREIGN KEY (afm) REFERENCES CUSTOMER(afm) ON DELETE CASCADE
);

-- 8. Entity: LOAN
CREATE TABLE LOAN (
    loan_number VARCHAR(20) PRIMARY KEY,
    original_amount DECIMAL(14, 2) NOT NULL CHECK (original_amount > 0),
    outstanding_balance DECIMAL(14, 2) NOT NULL CHECK (outstanding_balance >= 0),
    interest_rate DECIMAL(5, 2) NOT NULL CHECK (interest_rate >= 0),
    duration_months INT NOT NULL CHECK (duration_months > 0),
    branch_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (branch_code) REFERENCES BRANCH(branch_code)
);

-- 9. Junction Table: LOAN_BORROWER (N:M)
CREATE TABLE LOAN_BORROWER (
    loan_number VARCHAR(20) NOT NULL,
    afm VARCHAR(9) NOT NULL,
    PRIMARY KEY (loan_number, afm),
    FOREIGN KEY (loan_number) REFERENCES LOAN(loan_number) ON DELETE CASCADE,
    FOREIGN KEY (afm) REFERENCES CUSTOMER(afm) ON DELETE CASCADE
);"""

    return Scenario(
        id="banking_management",
        title="Banking Group & Transaction Management System",
        subtitle="Entity-Relationship Modeling for Branches, Employees, Customers, Bank Accounts, Transactions & Loans",
        course_tag="Databases (Progress Test 2025-2026 - Topic 4)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=assumptions,
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )
