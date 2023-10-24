#include<iostream>
#include<vector>
using namespace std;


vector<int> royal_flush(int n){
	vector<int>deck;
	int card = n;
	while (deck.size() != n){
		deck.insert(deck.begin(), card);
		for(int i = 0;i < card; i++){
			int moving_card; moving_card = deck.back();
			deck.pop_back();
			deck.insert(deck.begin(), moving_card);
		}
		card -= 1;
	}
	
	return deck;
		
}

int main(){
	int n;
	cin >> n;
	
	for(int i = 0; i< n; i++){
		int deck_size; cin >> deck_size;
		vector<int>result = royal_flush(deck_size);
		for(int j = 0; j < deck_size; j++){
			cout << result[j] << ' ';
		}
		cout << endl;
	}
	
	
	return 0;
}
