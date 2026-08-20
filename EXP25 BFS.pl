% Best First Search

edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Heuristic values
h(a, 5).
h(b, 4).
h(c, 2).
h(d, 3).
h(e, 1).
h(f, 0).

best_first(Start, Goal, Path, TotalH) :-
    search([Start], Goal, [], Path),
    heuristic_sum(Path, TotalH).

search([Goal|_], Goal, _, [Goal]).

search([Current|Rest], Goal, Visited, [Current|Path]) :-
    findall(H-Next,
        (edge(Current, Next),
         \+ member(Next, Visited),
         h(Next, H)),
        Children),
    sort(Children, Sorted),
    get_nodes(Sorted, Nodes),
    search(Nodes, Goal, [Current|Visited], Path).

get_nodes([], []).

get_nodes([_-Node|Rest], [Node|Nodes]) :-
    get_nodes(Rest, Nodes).

heuristic_sum([], 0).

heuristic_sum([Node|Rest], Total) :-
    h(Node, H),
    heuristic_sum(Rest, Remaining),
    Total is H + Remaining
