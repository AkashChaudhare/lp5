#include<bits/stdc++.h>
#include <omp.h>

using namespace std;

// Function to perform parallel linear regression training
void parallelLinearRegression(const vector<double>& x, const vector<double>& y, double& slope, double& intercept) {
    int numPoints = x.size();
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

    #pragma omp parallel for reduction(+:sumX,sumY,sumXY,sumX2)
    for (int i = 0; i < numPoints; ++i) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
    }

    double meanX = sumX / numPoints;
    double meanY = sumY / numPoints;

    double numerator = sumXY - numPoints * meanX * meanY;
    double denominator = sumX2 - numPoints * meanX * meanX;

    slope = numerator / denominator;
    intercept = meanY - slope * meanX;
}

// Test the linear regression training
int main() {
    vector<double> x = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<double> y = {2.0, 4.0, 6.0, 8.0, 10.0};

    int numPoints = x.size();
    double slope, intercept;
    cout << "-------------------------" <<endl;
    cout << "Parallel Linear Regression Training:" << endl;
    parallelLinearRegression(x, y, slope, intercept);
    cout << "-------------------------" <<endl;
    cout << "Slope is: "<< endl;
    cout << slope << endl;
    cout << "-------------------------" <<endl;
    cout << "Intercept: " << endl;
    cout<< intercept << endl;
    cout << "-------------------------" <<endl;
    cout << "Therefore line of best fit is y = " << slope << "x + " <<intercept;

    return 0;
}