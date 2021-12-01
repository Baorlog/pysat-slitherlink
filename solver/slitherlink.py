global width
global height


def read_slitherlink(slitherlink, g, num_clause):
    global width
    global height
    width = len(slitherlink[0].split(" "))
    height = len(slitherlink)

    # Rule 1: Number of edges around a box is equal to the number in it
    for i in range(height):
        row = slitherlink[i].split(" ")
        for j in range(width):
            if row[j] != ".":
                num = int(row[j])
                [e1, e2, e3, e4] = get_box_edges(i, j)
                if num == 0:
                    g.add_clause([-e1])
                    g.add_clause([-e2])
                    g.add_clause([-e3])
                    g.add_clause([-e4])

                    num_clause += 4
                elif num == 1:
                    g.add_clause([e1, e2, e3, e4])
                    g.add_clause([-e1, -e2])
                    g.add_clause([-e1, -e3])
                    g.add_clause([-e1, -e4])
                    g.add_clause([-e2, -e3])
                    g.add_clause([-e2, -e4])
                    g.add_clause([-e3, -e4])

                    num_clause += 7
                elif num == 2:
                    g.add_clause([e1, e2, e3])
                    g.add_clause([e1, e2, e4])
                    g.add_clause([e1, e3, e4])
                    g.add_clause([e2, e3, e4])
                    g.add_clause([-e1, -e2, -e3])
                    g.add_clause([-e1, -e2, -e4])
                    g.add_clause([-e1, -e3, -e4])
                    g.add_clause([-e2, -e3, -e4])

                    num_clause += 8
                elif num == 3:
                    g.add_clause([-e1, -e2, -e3, -e4])
                    g.add_clause([e1, e2])
                    g.add_clause([e1, e3])
                    g.add_clause([e1, e4])
                    g.add_clause([e2, e3])
                    g.add_clause([e2, e4])
                    g.add_clause([e3, e4])

                    num_clause += 7
                elif num == 4:
                    g.add_clause([e1])
                    g.add_clause([e2])
                    g.add_clause([e3])
                    g.add_clause([e4])

                    num_clause += 4

    return num_clause


def apply_known_patterns(slitherlink, g, num_clause):
    for i in range(height):
        row = slitherlink[i].split(" ")
        for j in range(width):
            if row[j] != ".":
                num = int(row[j])
                [e1, e2, e3, e4] = get_box_edges(i, j)
                sur_boxes = get_surround_box(i, j, slitherlink)
                if num == 0:

                    # Zero at corner
                    if i == 0 and j == 0:
                        g.add_clause([-(e1 + 1)])
                        g.add_clause([-(e4 + 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e2 + 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e3 + 1])
                            g.add_clause([e2 + 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e4 + 1])
                            g.add_clause([e3 + 1])
                            g.add_clause([e2 + 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 + 1])


                    elif i == 0 and j == width - 1:
                        g.add_clause([-(e1 - 1)])
                        g.add_clause([-(e2 + 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e3 - 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])


                    elif i == height - 1 and j == 0:
                        g.add_clause([-(e3 + 1)])
                        g.add_clause([-(e4 - 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e1 + 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e4 - 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e3 + 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])


                    elif i == height - 1 and j == width - 1:
                        g.add_clause([-(e2 - 1)])
                        g.add_clause([-(e3 - 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e3 - 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e2 - 1])
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])



                    # Zero at edges
                    elif i == 0:
                        g.add_clause([-(e1 + 1)])
                        g.add_clause([-(e1 - 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e2 + 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e3 + 1)])
                            g.add_clause([-(e3 - 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e3 + 1])
                            g.add_clause([e3 - 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[4] == 0:
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[4] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[3] == 1:
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[3] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])


                    elif j == 0:
                        g.add_clause([-(e4 - 1)])
                        g.add_clause([-(e4 + 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e4 - 1])
                            g.add_clause([e2 - 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([-(e2 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e2 - 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[4] == 0:
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[4] == 3:
                            g.add_clause([e3 + 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])

                        if sur_boxes[3] == 1:
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[3] == 3:
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 + 1])


                    elif i == height - 1:
                        g.add_clause([-(e3 - 1)])
                        g.add_clause([-(e3 + 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e4 - 1])
                            g.add_clause([e1 - 1])
                            g.add_clause([e3 - 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e1 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[4] == 0:
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[4] == 3:
                            g.add_clause([e2 - 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[3] == 1:
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[3] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])


                    elif j == width - 1:
                        g.add_clause([-(e2 - 1)])
                        g.add_clause([-(e2 + 1)])

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e3 - 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e4 - 1])
                            g.add_clause([e4 + 1])
                            g.add_clause([e1 - 1])
                            g.add_clause([e3 - 1])

                        if sur_boxes[4] == 0:
                            g.add_clause([-(e1 - 1)])
                        elif sur_boxes[4] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e2 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[3] == 1:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[3] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])


                    # Zero inside
                    else:

                        if sur_boxes[0] == 0:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e1 + 1)])
                        elif sur_boxes[0] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])
                            g.add_clause([e4 - 1])

                        if sur_boxes[2] == 0:
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([-(e2 + 1)])
                        elif sur_boxes[2] == 3:
                            g.add_clause([e2 - 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e1 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[4] == 0:
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[4] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e3 + 1])
                            g.add_clause([e2 + 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[6] == 0:
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[6] == 3:
                            g.add_clause([e4 - 1])
                            g.add_clause([e4 + 1])
                            g.add_clause([e1 - 1])
                            g.add_clause([e3 - 1])

                        if sur_boxes[1] == 1:
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([-(e2 - 1)])
                        elif sur_boxes[1] == 3:
                            g.add_clause([e1 + 1])
                            g.add_clause([e2 - 1])

                        if sur_boxes[3] == 1:
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([-(e3 + 1)])
                        elif sur_boxes[3] == 3:
                            g.add_clause([e2 + 1])
                            g.add_clause([e3 + 1])

                        if sur_boxes[5] == 1:
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e4 + 1)])
                        elif sur_boxes[5] == 3:
                            g.add_clause([e3 - 1])
                            g.add_clause([e4 + 1])

                        if sur_boxes[7] == 1:
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e4 - 1)])
                        elif sur_boxes[7] == 3:
                            g.add_clause([e1 - 1])
                            g.add_clause([e4 - 1])


                elif num == 1:

                    # One at corner
                    if i == 0 and j == 0:
                        g.add_clause([-e1])
                        g.add_clause([-e4])
                    elif i == 0 and j == width - 1:
                        g.add_clause([-e1])
                        g.add_clause([-e2])
                    elif i == height - 1 and j == 0:
                        g.add_clause([-e3])
                        g.add_clause([-e4])
                    elif i == height - 1 and j == width - 1:
                        g.add_clause([-e2])
                        g.add_clause([-e3])

                    # One at edges
                    elif i == 0:

                        if sur_boxes[0] == 1:
                            g.add_clause([-e2])
                        elif sur_boxes[0] == 3:
                            g.add_clause([-e3])
                            g.add_clause([-e4])

                        if sur_boxes[4] == 1:
                            g.add_clause([-e4])
                        elif sur_boxes[4] == 3:
                            g.add_clause([-e2])
                            g.add_clause([-e3])


                    elif j == 0:

                        if sur_boxes[0] == 1:
                            g.add_clause([-e1])
                        elif sur_boxes[0] == 3:
                            g.add_clause([-e2])
                            g.add_clause([-e3])

                        if sur_boxes[4] == 1:
                            g.add_clause([-e3])
                        elif sur_boxes[4] == 3:
                            g.add_clause([-e1])
                            g.add_clause([-e2])


                    elif i == height - 1:

                        if sur_boxes[0] == 1:
                            g.add_clause([-e4])
                        elif sur_boxes[0] == 3:
                            g.add_clause([-e1])
                            g.add_clause([-e2])

                        if sur_boxes[4] == 1:
                            g.add_clause([-e2])
                        elif sur_boxes[4] == 3:
                            g.add_clause([-e1])
                            g.add_clause([-e4])


                    elif j == width - 1:

                        if sur_boxes[0] == 1:
                            g.add_clause([-e3])
                        elif sur_boxes[0] == 3:
                            g.add_clause([-e1])
                            g.add_clause([-e4])

                        if sur_boxes[4] == 1:
                            g.add_clause([-e1])
                        elif sur_boxes[4] == 3:
                            g.add_clause([-e3])
                            g.add_clause([-e4])



                elif num == 3:

                    # Three at corner
                    if i == 0 and j == 0:
                        g.add_clause([e1])
                        g.add_clause([e4])

                        if sur_boxes[0] == 3:
                            g.add_clause([e2])
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([e3 + 1])

                        if sur_boxes[2] == 3:
                            g.add_clause([e3])
                            g.add_clause([-(e3 + 1)])
                            g.add_clause([-(e4 + 1)])
                            g.add_clause([e2 + 1])


                    elif i == 0 and j == width - 1:
                        g.add_clause([e1])
                        g.add_clause([e2])

                        if sur_boxes[0] == 3:
                            g.add_clause([e3])
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e2 + 1)])
                            g.add_clause([e4 + 1])

                        if sur_boxes[2] == 3:
                            g.add_clause([e4])
                            g.add_clause([-(e4 + 1)])
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([e3 - 1])


                    elif i == height - 1 and j == 0:
                        g.add_clause([e3])
                        g.add_clause([e4])

                        if sur_boxes[0] == 3:
                            g.add_clause([e1])
                            g.add_clause([-(e1 + 1)])
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([e2 - 1])

                        if sur_boxes[2] == 3:
                            g.add_clause([e2])
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([-(e3 + 1)])
                            g.add_clause([e1 + 1])


                    elif i == height - 1 and j == width - 1:
                        g.add_clause([e2])
                        g.add_clause([e3])

                        if sur_boxes[0] == 3:
                            g.add_clause([e4])
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([e1 - 1])

                        if sur_boxes[2] == 3:
                            g.add_clause([e1])
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([e4 - 1])


                    # Three at edges
                    elif i == 0:

                        if sur_boxes[0] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e2 + 1)])

                        if sur_boxes[2] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e3 + 1)])

                        if sur_boxes[4] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e4 + 1)])

                        if sur_boxes[1] == 3:
                            g.add_clause([e1])
                            g.add_clause([e4])

                        if sur_boxes[3] == 3:
                            g.add_clause([e1])
                            g.add_clause([e2])


                    elif j == 0:

                        if sur_boxes[0] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e1 + 1)])

                        if sur_boxes[2] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([-(e2 + 1)])

                        if sur_boxes[4] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e3 + 1)])

                        if sur_boxes[1] == 3:
                            g.add_clause([e3])
                            g.add_clause([e4])

                        if sur_boxes[3] == 3:
                            g.add_clause([e1])
                            g.add_clause([e4])


                    elif i == height - 1:

                        if sur_boxes[0] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e4 - 1)])

                        if sur_boxes[2] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e1 + 1)])

                        if sur_boxes[4] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e2 - 1)])

                        if sur_boxes[1] == 3:
                            g.add_clause([e2])
                            g.add_clause([e3])

                        if sur_boxes[3] == 3:
                            g.add_clause([e3])
                            g.add_clause([e4])


                    elif j == width - 1:

                        if sur_boxes[0] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e3 - 1)])

                        if sur_boxes[2] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([-(e4 + 1)])

                        if sur_boxes[4] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e1 - 1)])

                        if sur_boxes[1] == 3:
                            g.add_clause([e1])
                            g.add_clause([e2])

                        if sur_boxes[3] == 3:
                            g.add_clause([e2])
                            g.add_clause([e3])


                    # Three inside
                    else:

                        if sur_boxes[0] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e1 - 1)])
                            g.add_clause([-(e1 + 1)])

                        if sur_boxes[2] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e2 - 1)])
                            g.add_clause([-(e2 + 1)])

                        if sur_boxes[4] == 3:
                            g.add_clause([e1])
                            g.add_clause([e3])
                            g.add_clause([-(e3 - 1)])
                            g.add_clause([-(e3 + 1)])

                        if sur_boxes[6] == 3:
                            g.add_clause([e2])
                            g.add_clause([e4])
                            g.add_clause([-(e4 - 1)])
                            g.add_clause([-(e4 + 1)])

                        if sur_boxes[1] == 3:
                            g.add_clause([e3])
                            g.add_clause([e4])

                        if sur_boxes[3] == 3:
                            g.add_clause([e1])
                            g.add_clause([e4])

                        if sur_boxes[5] == 3:
                            g.add_clause([e1])
                            g.add_clause([e2])

                        if sur_boxes[7] == 3:
                            g.add_clause([e2])
                            g.add_clause([e3])

    return num_clause


def show_slitherlink(var_list, slitherlink):
    for i in range(2 * height + 1):
        for j in range(2 * width + 1):
            if i % 2:
                row = i // 2
                col = j // 2
                if j % 2:
                    char = slitherlink[row].split(" ")[col]
                    if char == ".":
                        print(" ", end="")
                    else:
                        print(char, end="")
                else:
                    item = get_vert_edges(row, col)[2] - 1
                    is_connected = var_list[item]
                    if is_connected > 0:
                        print("|", end="")
                    else:
                        print(" ", end="")
            else:
                if j % 2:
                    row = i // 2
                    col = j // 2
                    item = get_vert_edges(row, col)[1] - 1
                    is_connected = var_list[item]
                    if is_connected > 0:
                        print("_", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
        print()


def check_valid(var_list):
    # Find first connected edge
    first_edge = 0
    for i in range(len(var_list)):
        if var_list[i] > 0:
            first_edge = var_list[i]
            break

    # Find first (left) vertices coordinates
    x = (first_edge - 1) // width
    y = (first_edge - 1) % width

    # Count edges in 1 loop
    edge_count = 1

    # Next vertices
    v_x = x
    v_y = y + 1

    coming_from = 3     # Left

    while v_x != x or v_y != y:

        edges = get_vert_edges(v_x, v_y)
        edges[coming_from] = -1

        # Eliminate non-exists edges
        if v_x == 0 and v_y == 0:
            edges[0] = -1
            edges[3] = -1
        elif v_x == 0 and v_y == width:
            edges[0] = -1
            edges[1] = -1
        elif v_x == height and v_y == 0:
            edges[2] = -1
            edges[3] = -1
        elif v_x == height and v_y == width:
            edges[1] = -1
            edges[2] = -1
        elif v_x == 0:
            edges[0] = -1
        elif v_y == 0:
            edges[3] = -1
        elif v_x == height:
            edges[2] = -1
        elif v_y == width:
            edges[1] = -1

        for i in range(len(edges)):
            if edges[i] != -1 and var_list[edges[i] - 1] > 0:
                edge_count += 1
                if i == 0:
                    v_x -= 1
                    coming_from = 2     # Bottom
                elif i == 1:
                    v_y += 1
                    coming_from = 3     # Left
                elif i == 2:
                    v_x += 1
                    coming_from = 0     # Above
                elif i == 3:
                    v_y -= 1
                    coming_from = 1     # Right

    # Connected edges in solution
    solution_edge_count = 0
    for var_item in var_list:
        if var_item > 0:
            solution_edge_count += 1

    return edge_count == solution_edge_count


def get_box(row, col, slitherlink):
    num = slitherlink[row].split(" ")[col]
    if num != ".":
        return int(num)
    else:
        return -1


def get_surround_box(row, col, slitherlink):
    if row == 0 and col == 0:
        return [
            get_box(row, col+1, slitherlink),
            get_box(row+1, col+1, slitherlink),
            get_box(row+1, col, slitherlink),
        ]
    elif row == 0 and col == width - 1:
        return [
            get_box(row+1, col, slitherlink),
            get_box(row+1, col-1, slitherlink),
            get_box(row, col-1, slitherlink),
        ]
    elif row == height - 1 and col == 0:
        return [
            get_box(row-1, col, slitherlink),
            get_box(row-1, col+1, slitherlink),
            get_box(row, col+1, slitherlink),
        ]
    elif row == height - 1 and col == width - 1:
        return [
            get_box(row, col-1, slitherlink),
            get_box(row-1, col-1, slitherlink),
            get_box(row-1, col, slitherlink),
        ]
    elif row == 0:
        return [
            get_box(row, col+1, slitherlink),
            get_box(row+1, col+1, slitherlink),
            get_box(row+1, col, slitherlink),
            get_box(row+1, col-1, slitherlink),
            get_box(row, col-1, slitherlink),
        ]
    elif col == 0:
        return [
            get_box(row-1, col, slitherlink),
            get_box(row-1, col+1, slitherlink),
            get_box(row, col+1, slitherlink),
            get_box(row+1, col+1, slitherlink),
            get_box(row+1, col, slitherlink),
        ]
    elif row == height - 1:
        return [
            get_box(row, col-1, slitherlink),
            get_box(row-1, col-1, slitherlink),
            get_box(row-1, col, slitherlink),
            get_box(row-1, col+1, slitherlink),
            get_box(row, col+1, slitherlink),
        ]
    elif col == width - 1:
        return [
            get_box(row+1, col, slitherlink),
            get_box(row+1, col-1, slitherlink),
            get_box(row, col-1, slitherlink),
            get_box(row-1, col-1, slitherlink),
            get_box(row-1, col, slitherlink),
        ]
    else:
        return [
            get_box(row-1, col, slitherlink),
            get_box(row-1, col+1, slitherlink),
            get_box(row, col+1, slitherlink),
            get_box(row+1, col+1, slitherlink),
            get_box(row+1, col, slitherlink),
            get_box(row+1, col-1, slitherlink),
            get_box(row, col-1, slitherlink),
            get_box(row-1, col-1, slitherlink),
        ]


def get_box_edges(row, col):
    return [
        row * width + col + 1,
        (height + 1) * width + (col + 1) * height + row + 1,
        (row + 1) * width + col + 1,
        (height + 1) * width + col * height + row + 1
    ]


# def get_edge_vert(i, j, e):
#     if e == 1:
#         return (height + 1) * width + j * height + i
#     elif e == 2:
#         return i * width + j + 1
#     elif e == 3:
#         return (height + 1) * width + j * height + i + 1
#     elif e == 4:
#         return i * width + j


def get_vert_edges(i, j):
    return [
        (height + 1) * width + j * height + i,
        i * width + j + 1,
        (height + 1) * width + j * height + i + 1,
        i * width + j
    ]
