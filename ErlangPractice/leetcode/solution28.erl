%%%-------------------------------------------------------------------
%%% @author germainjones
%%% @copyright (C) 2025, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 11. Feb 2025 15:33
%%%-------------------------------------------------------------------
-module(solution28).
-author("germainjones").

%% API
-export([]).
-spec str_str(Haystack :: unicode:unicode_binary(), Needle :: unicode:unicode_binary()) -> integer().
str_str(Haystack, Needle) ->
    %% Convert both inputs from binary to list
    HList = erlang:binary_to_list(Haystack),
    NList = erlang:binary_to_list(Needle),
    find_index(HList, NList, 0).

%% If the Haystack list is empty, Needle wasn’t found.
find_index([], _Needle, _Count) ->
    -1;
%% Otherwise, if Needle is a prefix of Haystack, return the current count.
find_index(Haystack, Needle, Count) ->
    case is_prefix(Needle, Haystack) of
        true -> Count;
        false ->
            %% Continue searching from the tail of Haystack.
            find_index(tl(Haystack), Needle, Count + 1)
    end.

%% is_prefix(Prefix, List) returns true if Prefix is the prefix of List.
is_prefix([], _List) ->
    true;
is_prefix(_Prefix, []) ->
    false;
is_prefix([H1|T1], [H2|T2]) when H1 =:= H2 ->
    is_prefix(T1, T2);
is_prefix(_, _) ->
    false.