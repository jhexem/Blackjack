from typing import Tuple

class HouseRules:
	def __init__(
		self,
		dealer_hits_soft_17: bool,
		surrender_allowed: bool,
		insurance_allowed: bool,
		double_after_split_allowed: bool,
		blackjack_payout_ratio: Tuple[int, int],  # e.g. (3,2) or (6,5)
		double_aces_after_split: bool,
		number_of_decks: int,
		resplit_aces_allowed: bool,
		max_splits: int,
		count_cards: bool
	):
		self.dealer_hits_soft_17 = dealer_hits_soft_17
		self.surrender_allowed = surrender_allowed
		self.insurance_allowed = insurance_allowed
		self.double_after_split_allowed = double_after_split_allowed
		self.blackjack_payout_ratio = blackjack_payout_ratio
		self.double_aces_after_split = double_aces_after_split
		self.number_of_decks = number_of_decks
		self.resplit_aces_allowed = resplit_aces_allowed
		self.max_splits = max_splits
		self.count_cards = count_cards