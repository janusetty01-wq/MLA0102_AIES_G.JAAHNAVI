% Vowel Identification using Rule-Based Logic

vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

vowel(A) :-
    char_lower(A, Lower),
    vowel(Lower).

% Convert uppercase to lowercase
char_lower(A, Lower) :-
    char_code(A, Code),
    Code >= 65,
    Code =< 90,
    LowerCode is Code + 32,
    char_code(Lower, LowerCode).

% Identify vowels in a sentence
identify_vowels([]).

identify_vowels([H|T]) :-
    ( vowel(H) ->
        write(H), write(' -> Vowel'), nl
    ;
        true
    ),
    identify_vowels(T).
