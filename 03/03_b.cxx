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

	vector<bitset<N_BITS> > oxvals = nums;
	for(int i = N_BITS-1; i >= 0; --i)
	{
		int n_set = std::count_if(oxvals.begin(), oxvals.end(), [i](const bitset<N_BITS> x){return x[i];});
		int n_not = std::count_if(oxvals.begin(), oxvals.end(), [i](const bitset<N_BITS> x){return !x[i];});
		for(int j = oxvals.size() - 1; j >= 0; --j)
		{
			bitset<N_BITS> oxval = oxvals[j];
			if( (n_set > n_not && !oxval[i]) || (n_set < n_not && oxval[i]) || (n_set == n_not && !oxval[i]))
				oxvals.erase(oxvals.begin() + j);
		}
		if(oxvals.size() == 1)
			break;
	}
	if(oxvals.size() != 1)
		throw runtime_error("Failed to find oxval");


	vector<bitset<N_BITS> > co2vals = nums;
	for(int i = N_BITS-1; i >= 0; --i)
	{
		int n_set = std::count_if(co2vals.begin(), co2vals.end(), [i](const bitset<N_BITS> x){return x[i];});
		int n_not = std::count_if(co2vals.begin(), co2vals.end(), [i](const bitset<N_BITS> x){return !x[i];});
		for(int j = co2vals.size() - 1; j >= 0; --j)
		{
			bitset<N_BITS> co2val = co2vals[j];
			if( (n_set > n_not && co2val[i]) || (n_set < n_not && !co2val[i]) || (n_set == n_not && co2val[i]))
				co2vals.erase(co2vals.begin() + j);
		}
		if(co2vals.size() == 1)
			break;
	}
	if(co2vals.size() != 1)
		throw runtime_error("Failed to find co2val");

	cout << oxvals[0] << ":" << oxvals[0].to_ulong() << endl;
	cout << co2vals[0] << ":" << co2vals[0].to_ulong() << endl;
	cout << oxvals[0].to_ulong() * co2vals[0].to_ulong() << endl;

	return 0;
}
