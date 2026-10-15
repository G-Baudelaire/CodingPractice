%%%-------------------------------------------------------------------
%%% @author germainjones
%%% @copyright (C) 2025, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 11. Feb 2025 14:54
%%%-------------------------------------------------------------------
-module(solution1).
-author("germainjones").

%% API
-export([length_of_last_word/1]).
-spec length_of_last_word(S :: unicode:unicode_binary()) -> integer().
%% | length_of_last_word(String) -> Length of the last word in String.
%% | If String has no words, returns 0.

length_of_last_word(S) when is_list(S) ->
    %% Split the string on the space character.
    Tokens = string:tokens(S, " "),
    case Tokens of
        [] ->
            0;  %% No words found.
        _ ->
            %% The last token is the last word.
            string:length(lists:last(Tokens))
    end.