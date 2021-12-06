from pysat.solvers import Glucose3
from solver.slitherlink import read_slitherlink, get_vert_edges, show_slitherlink, check_valid, apply_known_patterns
import time
import datetime


def current_milli_time():
    return time.time() * 1000


def pysat_slitherlink_binomal(slitherlink):
    # Glucose initialize
    g = Glucose3()

    height = len(slitherlink)
    width = len(slitherlink[0].split(" "))

    # Number of clause
    num_clause = 0

    num_clause = read_slitherlink(slitherlink, g, num_clause)

    # Implement basic rules of slitherlink
    # g.add_clause([-56])

    # Rule 2: No crossing at 1 vertices
    for i in range(height + 1):
        for j in range(width + 1):

            [e1, e2, e3, e4] = get_vert_edges(i, j)

            # Identify where the vertices is
            # Upper-left corner
            if i == 0 and j == 0:
                g.add_clause([-e2, e3])
                g.add_clause([e2, -e3])

                num_clause += 2
            # Upper-right corner
            elif i == 0 and j == width:
                g.add_clause([-e4, e3])
                g.add_clause([e4, -e3])

                num_clause += 2
            # Lower-left corner
            elif i == height and j == 0:
                g.add_clause([-e2, e1])
                g.add_clause([e2, -e1])

                num_clause += 2
            # Lower-right corner
            elif i == height and j == width:
                g.add_clause([-e1, e4])
                g.add_clause([e1, -e4])

                num_clause += 2

            # Upper edge
            elif i == 0:
                g.add_clause([-e2, e3, e4])
                g.add_clause([e2, -e3, e4])
                g.add_clause([e2, e3, -e4])
                g.add_clause([-e2, -e3, -e4])

                num_clause += 4
            # Left edge
            elif j == 0:
                g.add_clause([-e1, e2, e3])
                g.add_clause([e1, -e2, e3])
                g.add_clause([e1, e2, -e3])
                g.add_clause([-e1, -e2, -e3])

                num_clause += 4
            # Lower edge
            elif i == height:
                g.add_clause([-e1, e2, e4])
                g.add_clause([e1, -e2, e4])
                g.add_clause([e1, e2, -e4])
                g.add_clause([-e1, -e2, -e4])

                num_clause += 4
            # Right edge
            elif j == width:
                g.add_clause([-e1, e3, e4])
                g.add_clause([e1, -e3, e4])
                g.add_clause([e1, e3, -e4])
                g.add_clause([-e1, -e3, -e4])

                num_clause += 4
            # Inside
            else:
                g.add_clause([-e1, e2, e3, e4])
                g.add_clause([e1, -e2, e3, e4])
                g.add_clause([e1, e2, -e3, e4])
                g.add_clause([e1, e2, e3, -e4])
                g.add_clause([-e1, -e2, -e3])
                g.add_clause([-e1, -e2, -e4])
                g.add_clause([-e1, -e3, -e4])
                g.add_clause([-e2, -e3, -e4])

                num_clause += 8

    apply_known_patterns(slitherlink, g, num_clause)

    print("Processing...")
    start = time.time()
    success = g.solve()

    if success:

        var_count = 0
        loop_count = 0

        # Rule 3: Only 1 loop exists
        for solution in g.enum_models():
            loop_count += 1
            if check_valid(solution):
                show_slitherlink(solution, slitherlink)
                var_count = len(solution)
                print(solution)
                break
        end = time.time()

        print("Time to solve: " + str(end - start) + " (ms)")
        print("Number of clauses: " + str(num_clause) + " clauses.")
        print("Number of variables: " + str(var_count))
        print("Number of loops (for rule 3): " + str(loop_count))

        return success, solution, end-start, num_clause, var_count, loop_count

    else:
        return success, None, None, None, None, None

