%%%-------------------------------------------------------------------
%%% @author germainjones
%%% @copyright (C) 2025, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 11. Feb 2025 15:59
%%%-------------------------------------------------------------------
-module(solution125).
-author("germainjones").

%% API
-export([]).
-spec is_palindrome(S :: unicode:unicode_binary()) -> boolean().

is_palindrome(S) ->
    List = erlang:binary_to_list(S),
    Reversed_List = lists:reverse(List),
    io:fwrite(List),
    match_characters(List, Reversed_List).

match_characters([], []) ->
    true;
match_characters([a | Tail1], [a | Tail2]) ->
    match_characters(Tail1, Tail2);
match_characters(_, _) ->
    false.
