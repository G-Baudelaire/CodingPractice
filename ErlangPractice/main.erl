-module(main).
-export([main/0]).

main() ->
    io:format("~p~n", [solution1:length_of_last_word("Hello World")]).
