import xml.etree.ElementTree as ET
import os


def findMatchPeriods(xml_path):
    """
    Parses the XML file to calculate time distances between original and rematch games.

    The function maps each pair of teams to their corresponding match and rematch periods,
    then calculates the difference.

    Args:
        xml_path (str): The absolute path to the XML scheduling file.

    Returns:
        dict (tuple, int): A dictionary where keys are team pairs (i, j)
                            and values are the period difference.
    """
    if not os.path.exists(xml_path):
        print(f"File not found: {xml_path}")
        return {}

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Matches are usually stored in a mapping to keep track of both (Home, Away) and (Away, Home).
    match_data = {}
    period_distances = {}

    # Navigates the XML structure based on typical ITC2021 format.
    for game in root.findall(".//Game"):
        # Extracts match details including home team, away team, and defined period.
        h_team = int(game.get("home"))
        a_team = int(game.get("away"))
        period = int(game.get("slot", 0))

        # Normalizes the pair (min, max) to identify match and rematch consistently.
        t_pair = tuple(sorted((h_team, a_team)))

        if t_pair not in match_data:
            match_data[t_pair] = []
        match_data[t_pair].append({"home": h_team, "away": a_team, "period": period})

    # Evaluates the gap between match instances for each distinctive team pair.
    for team_pair, matches in match_data.items():
        if len(matches) >= 2:
            m1 = matches[0]
            m2 = matches[1]
            # Calculates the temporal distance in periods regardless of direction.
            dist = abs(m1["period"] - m2["period"])
            period_distances[team_pair] = dist

    return period_distances


def displayMatchDistances(xml_path):
    """
    Executes the analysis and displays match period differences for all pairings.

    Args:
        xml_path (str): The target XML file to parse.
    """
    distances = findMatchPeriods(xml_path)

    if not distances:
        print("No valid matches found or file error.")
        return

    print("Match-Rematch Period Distances (Day Intervals):")
    for (t1, t2), diff in distances.items():
        # Only displays relevant pairings to avoid redundant info.
        print(f"Teams {t1}-{t2}: Difference = {diff} periods.")


if __name__ == "__main__":
    # Standard location based on Exercise instructions.
    xml_filename = "./ITC2021_Test8_SolGenMethodA.xml"
    displayMatchDistances(xml_filename)
