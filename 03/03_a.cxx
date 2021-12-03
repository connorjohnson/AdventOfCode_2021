#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <exception>
#include <algorithm>

using namespace std;

const int N_BITS = 12;

int main(int argc, char*argv[]){
	if(argc != 2)
	{
		cerr << "Usage: " << argv[0] << " <filename>" << endl;
		return(1);
	}

	ifstream fin(argv[1]);
	if(!fin.is_open())
		throw runtime_error("Unable to open file " + string(argv[1]));

	string a;
	vector<std::bitset<N_BITS> > nums;
	while(fin >> a){
		std::bitset<N_BITS> num(a);
		nums.push_back(num);
	}

	//for(std::bitset<N_BITS> x : nums)
	//	cout << x << ":" << x.to_ulong() << std::endl;

	std::bitset<N_BITS> gamma;
	for(int i = 0 ; i < N_BITS; ++i)
	{
		int n_set = std::count_if(nums.begin(), nums.end(), [i](const bitset<N_BITS> x){return x[i];});
		int n_not = std::count_if(nums.begin(), nums.end(), [i](const bitset<N_BITS> x){return !x[i];});
		gamma[i] = n_set >= n_not;
	}
	cout << gamma << ":" << gamma.to_ulong() << endl;
	std::bitset<N_BITS> epsilon = gamma;
	epsilon.flip();
	cout << epsilon << ":" << epsilon.to_ulong() << endl;

	cout << "Power: " << gamma.to_ulong() * epsilon.to_ulong() << endl;

	return 0;
}
