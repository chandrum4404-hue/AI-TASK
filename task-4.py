
facts = {
    "CGPA_Above_7",
    "PassedAllSubjects",
    "Attendance_Above_75",
    "HasProjects",
    "CodingSkillsGood",
}

rules = [
    ("R1", ["CGPA_Above_7", "PassedAllSubjects"], "GoodAcademicPerformance"),
    ("R2", ["Attendance_Above_75"], "GoodAttendance"),
    ("R3", ["HasProjects", "CodingSkillsGood"], "TechnicallyReady"),
    ("R4", ["GoodAcademicPerformance", "GoodAttendance", "TechnicallyReady"],
     "EligibleForPlacement"),
    ("R5", ["LowCodingScore"], "NeedsExtraPractice"),
]


def prove(goal, depth=0, visiting=None):
    """Try to prove `goal`. Returns True/False and prints reasoning steps."""
    if visiting is None:
        visiting = set()
    indent = "    " * depth

    print(f"{indent}GOAL: Is '{goal}' true?")

    if goal in facts:
        print(f"{indent}  -> '{goal}' is a known FACT. Proven.")
        return True

    if goal in visiting:
        print(f"{indent}  -> Circular dependency on '{goal}'. Failed.")
        return False
    visiting = visiting | {goal}

    candidates = [r for r in rules if r[2] == goal]
    if not candidates:
        print(f"{indent}  -> Not a fact and no rule concludes it. Failed.")
        return False

    for rule_id, conditions, conclusion in candidates:
        print(f"{indent}  Try {rule_id}: IF {' AND '.join(conditions)} "
              f"THEN {conclusion}")
        # Every condition becomes a new sub-goal
        if all(prove(c, depth + 1, visiting) for c in conditions):
            print(f"{indent}  -> {rule_id} fires. '{goal}' is PROVEN.")
            facts.add(goal)          # cache the derived fact
            return True
        print(f"{indent}  -> {rule_id} failed.")

    print(f"{indent}  -> No rule proves '{goal}'. Failed.")
    return False


def main():
    goal = "EligibleForPlacement"   # alternatives: "NeedsExtraPractice", "GoodAcademicPerformance"

    print("Known facts:")
    for f in sorted(facts):
        print(f"  - {f}")
    print(f"\nSelected goal: {goal}\n")
    print("Reasoning steps:")
    print("-" * 60)

    result = prove(goal)

    print("-" * 60)
    if result:
        print(f"\nFinal conclusion: The student IS {goal}.")
    else:
        print(f"\nFinal conclusion: '{goal}' could NOT be proven.")


if __name__ == "__main__":
    main()