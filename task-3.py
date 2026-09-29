
variables = ["Maths", "Python", "DBMS", "AI"]

domains = {v: ["9:00 AM", "11:00 AM", "2:00 PM"] for v in variables}

not_equal_constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI"),
]



def is_consistent(var, value, assignment):
    """Check whether assigning `value` to `var` violates any constraint
    with the subjects that are already assigned."""
    for a, b in not_equal_constraints:
        if var == a and assignment.get(b) == value:
            return False
        if var == b and assignment.get(a) == value:
            return False
    return True


def backtrack(assignment):
   
    if len(assignment) == len(variables):
        return assignment

    var = next(v for v in variables if v not in assignment)

    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value              # try this slot
            print(f"  Assign {var:<7} -> {value}")
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var]                  # undo (backtrack)
            print(f"  Backtrack: remove {var}")
    return None                                  # no slot works -> fail


def main():
    print("Search trace:")
    solution = backtrack({})

    if solution is None:
        print("\nNo valid timetable exists.")
        return

    print("\nFinal Timetable")
    print("-" * 28)
    for subject in variables:
        print(f"{subject:<8} : {solution[subject]}")

    print("\nConstraint verification")
    print("-" * 28)
    print("Each subject has exactly one slot:",
          all(v in solution for v in variables))
    for a, b in not_equal_constraints:
        ok = solution[a] != solution[b]
        print(f"{a} ({solution[a]}) vs {b} ({solution[b]}): "
              f"{'different slots - OK' if ok else 'CONFLICT'}")


if __name__ == "__main__":
    main()