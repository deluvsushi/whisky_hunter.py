from requests import get

class WhiskyHunter:
	def __init__(self) -> None:
		self.api = "https://whiskyhunter.net/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def read_auction_data(self, slug: str) -> dict:
		return get(
			f"{self.api}/auction_data/{slug}/auction_data_read",
			headers=self.headers).json()
	
	def get_auctions_data(self) -> dict:
		return get(
			f"{self.api}/auctions_data/auctions_data_list",
			headers=self.headers).json()
	
	def get_auctions_info(self) -> dict:
		return get(
			f"{self.api}/auctions_info/auctions_info_list",
			headers=self.headers).json()
	
	def get_distilleries_info(self) -> dict:
		return get(
			f"{self.api}/distilleries_info/distilleries_info_list",
			headers=self.headers).json()
	
	def read_distillery_data(self, slug: str) -> dict:
		return get(
			f"{self.api}/distillery_data/{slug}/distillery_data_read",
			headers=self.headers).json()
			
