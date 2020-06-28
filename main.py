import logging
import time
from typing import Optional

from strategies import default_random_choice

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class RockPaperScissors:
    def __init__(self, n_players: int = 2) -> None:
        self.n_players = n_players
        self.players_and_choices = {
            f'player_{number + 1}': default_random_choice() for number in range(n_players)
        }
        logger.info(f'Starting players and choices: {self.players_and_choices}')

    def knock_out_players(self, eliminated_choice: str) -> None:
        players_before = self.players_and_choices.keys()
        self.players_and_choices = {
            k: v for k, v in self.players_and_choices.items() if v != eliminated_choice
        }
        players_after = self.players_and_choices.keys()
        players_eliminated = set(players_before) - set(players_after)
        if len(players_eliminated) > 0:
            logger.info(f'Players eliminated: {set(players_before) - set(players_after)}')

    def make_choices(self) -> None:
        logging.info(f'Making choices for new round')
        self.players_and_choices = {
            k: default_random_choice() for k, v in self.players_and_choices.items()
        }
        logging.info(f'New choices: {self.players_and_choices}')

    def play_round(self) -> Optional[str]:
        if set(self.players_and_choices.values()) == set(['rock', 'paper', 'scissors']):
            logger.info('Round drawn')
            return None
        elif len(set(self.players_and_choices.values())) == 1:
            logger.info('Players picked same choice. Round drawn.')
            return None

        for player, choice in self.players_and_choices.items():
            if choice == 'rock':
                self.knock_out_players('scissors')
            elif choice == 'paper':
                self.knock_out_players('rock')
            else:  # choice == 'scissors'
                self.knock_out_players('paper')

        if len(self.players_and_choices) == 1:
            winning_player = list(self.players_and_choices.keys())[0]
            logging.info(f'Winning player: {winning_player}')
            return winning_player


if __name__ == '__main__':
    game = RockPaperScissors(n_players=2)
    while True:  # Play until winner is found
        time.sleep(1)
        if game.play_round():
            break
        else:
            game.make_choices()

