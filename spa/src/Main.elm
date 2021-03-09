module Main exposing (..)

-- simple chess timer
--
-- includes:
--    one button for each player's clock, button face is the clock time
--    a pause button to stop time on both clocks
--    a reset button to start over - sets time on both clocks to default time
--    a increase time button to add more time to both clocks
--    a decrease time button to subtract time from both clocks
-- MAIN

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick)
import Time


main : Program () Model Msg
main =
    Browser.element { init = init, subscriptions = subscriptions, update = update, view = view }



-- MODEL


type Player
    = He
    | She
    | Neither


startTimeDefault : number
startTimeDefault =
    300


deltaTime : number
deltaTime =
    30


type alias Model =
    { hisTime : Int
    , herTime : Int
    , currentPlayer : Player
    }


init : () -> ( Model, Cmd Msg )
init _ =
    ( Model startTimeDefault startTimeDefault Neither, Cmd.none )



-- UPDATE


type Msg
    = IncrementTimeLeft
    | DecrementTimeLeft
    | Tick Time.Posix
    | Pause
    | Reset
    | HeStops
    | SheStops


lostTime : number -> number
lostTime t =
    if t <= 0 then
        0

    else
        t

update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        HeStops ->
            ( { model | currentPlayer = She }, Cmd.none )

        SheStops ->
            ( { model | currentPlayer = He }, Cmd.none )

        IncrementTimeLeft ->
            ( { model | hisTime = model.hisTime + deltaTime, herTime = model.herTime + deltaTime }, Cmd.none )

        DecrementTimeLeft ->
            ( { model | hisTime = lostTime (model.hisTime - deltaTime), herTime = lostTime (model.herTime - deltaTime) }, Cmd.none )

        Tick _ ->
            case model.currentPlayer of
                She ->
                    ( { model | herTime = lostTime (model.herTime - 1) }, Cmd.none )

                He ->
                    ( { model | hisTime = lostTime (model.hisTime - 1) }, Cmd.none )

                Neither ->
                    ( model, Cmd.none )

        Pause ->
            ( { model | currentPlayer = Neither }, Cmd.none )

        Reset ->
            ( { model | currentPlayer = Neither, hisTime = startTimeDefault, herTime = startTimeDefault }, Cmd.none )



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions _ =
    Time.every 1000 Tick



-- VIEW


activeBtnColor : b -> b -> String
activeBtnColor currPlayer isThisPerson =
    if currPlayer == isThisPerson then
        "yellow"

    else
        "white"


btnColor : { a | hisTime : number, herTime : number, currentPlayer : Player } -> Player -> String
btnColor m isThisPerson =
    if getTimeForPlayer m isThisPerson == 0 then
        "red"

    else
        activeBtnColor m.currentPlayer isThisPerson


minsec : Int -> String
minsec seconds =
    String.padLeft 2 '0' (String.fromInt (seconds // 60)) ++ ":" ++ String.padLeft 2 '0' (String.fromInt (remainderBy 60 seconds))


getTimeForPlayer : { a | hisTime : number, herTime : number } -> Player -> number
getTimeForPlayer model player =
    case player of
        He ->
            model.hisTime

        She ->
            model.herTime

        Neither ->
            1


view : Model -> Html Msg
view model =
    div
        []
        [ button [ onClick HeStops, style "font-size" "300px", style "background-color" (btnColor model He) ]
            [ text (minsec model.hisTime) ]
        , button [ onClick DecrementTimeLeft, style "font-size" "75px" ]
            [ text "  -  " ]
        , button [ onClick IncrementTimeLeft, style "font-size" "75px" ]
            [ text "  +  " ]
        , button [ onClick Reset, style "font-size" "75px" ]
            [ text " Reset " ]
        , button [ onClick Pause, style "font-size" "75px" ]
            [ text " Pause " ]
        , button [ onClick SheStops, style "font-size" "300px", style "background-color" (btnColor model She) ]
            [ text (minsec model.herTime) ]
        ]
