from collections import OrderedDict, deque
import igraph


def parse_input() -> dict:
    parsed_input = OrderedDict()

    with open('inputs/day7.txt', 'r') as f:
        for line in f:
            part_indices = [i for i, n in enumerate(line) if n == ' ']
            parent_color = line[:part_indices[1]]
            parsed_input[parent_color] = {}

            for i in range(int((len(part_indices) - 3) / 4)):
                cnt = int(line[part_indices[3 + (4 * i)] + 1:part_indices[4 + (4 * i)]])
                color = line[part_indices[4 + (4 * i)] + 1:part_indices[6 + (4 * i)]]
                parsed_input[parent_color][color] = cnt

    return parsed_input


def get_graph_from_input(parsed_input: dict) -> igraph.Graph:
    g = igraph.Graph(directed=True)
    g.add_vertices(len(parsed_input))

    for container, containee in parsed_input.items():
        container_id = list(parsed_input.keys()).index(container)
        for containee_name, containee_count in containee.items():
            contaniee_id = list(parsed_input.keys()).index(containee_name)

            g.add_edge(contaniee_id, container_id)

    return g


def main():
    parsed_input = parse_input()
    g = get_graph_from_input(parsed_input)
    shiny_gold_bag_id = list(parsed_input.keys()).index('shiny gold')

    visited_vertices, parents = g.dfs(vid=shiny_gold_bag_id, mode=1)  # 1 = OUT

    print(len(visited_vertices) - 1) # do not count the shiny gold itself


def main2():
    parsed_input = parse_input()

    to_be_visited = deque(['shiny gold'])
    steps = 0
    while to_be_visited:
        steps += 1

        key = to_be_visited.popleft()
        for containee, cnt in parsed_input[key].items():
            to_be_visited.extend([containee] * cnt)

    print(steps - 1)  # do not count the shiny gold itself


if __name__ == '__main__':
    main()
    main2()
