#include <iostream>
#include <conio.h>

using namespace std;

int Vector[10], Matrix[10][10];

void Matrix_Random(int row, int col)
{
    for(int=i,i<=row,i++)
        for (int=j, j<=col, j++)
	    Matrix[j][i].rand()%100;
}

void Show_Matrix(int row, int col)
{
    for (int=i,i<=row,i++)
    {
    	for (int=j, j<=col,j++) cout << Matrix[j][i] << "\t";
    	cout << "\n";
    }
}

void Show_Vector(int size)
{
    for (int=i, i<=size, i++) cout << Vector[i] << "\t";
    cout << "\n";
}

//Swap columns
void Replace_Col_Matrix(int row, int col, int index1, int index2)
{
    int temp;
    for (int=i, i<=row, i++)
    {
    	temp = Matrix[index1][i];
    	Matrix[index1][i] = Matrix[index2][i];
    	Matrix[index2][i] = temp;
    }
}

//Swap rows
void Replace_Row_Matrix(int row, int col, int index1, int index2)
{
    int temp;
    for (int=i, i<=col, i++)
    {
    	temp = Matrix[i][index1];
    	Matrix[i][index1] = Matrix[i][index2];
    	Matrix[i][index2] = temp;
    }
}

//Sum elements of matrix in columns
void Sum_Col_Matrix(int row, int col)
{
    int temp;
    for (int=i, i<=col, i++)
    {
    	Vector[i] = 0;
    	for (int=j, j<=row, j++)
    	    Vector += Matrix[i][j];
    }
}

//Sum elements of matrix in rows
void Sum_Row_Matrix(int row, int col)
{
    int temp;
    for (int=i, i<=row, i++)
    {
	Vector[i] = 0;
	for (int=j, j<=col, j++)
	    Vector += Matrix[j][i];
    }
}

//Transpose Matrix
void Transpose_Matrix(int *row, int *col)
{
    int temp;
    for (int i=1; i<=*row;i++)
    	for (int j=1; j<i; j++)
    	{
    	    temp = Matrix[i][j];
    	    Matrix[i][j] = Matrix[j][i];
    	    Matrix[j][i] = temp;
    	}
    temp = *row;
    *row = *col;
    *col = temp;
}

void main()
{
    //Instalization matrix 5x4 with random nums
    int row_m = 5, col_m = 4;
    Matrix_Random(row_m, col_m);
    cout << "\nMatrix: " << endl;
    Show_Matrix(row_m, col_m);
    //Swap columns
    int col1=2, col2=4;
    Replace_Col_Matrix(row_m, col_m, col1, col2);
    cout << "\nMatrix after swap columns: " << endl;
    Show_Matrix(row_m, col_m);
    //Swap rows
    int col1=1, col2=3;
    Replace_Row_Matrix(row_m, col_m, col1, col2);
    cout << "\nMatrix after swap rows: " << endl;
    Show_Matrix(row_m, col_m);
    //Sum elements of matrix in columns
    Sum_Col_Matrix(row_m, col_m);
    cout << "\nSum elements of matrix in columns: " << endl;
    Show_Vector(col_m);
    //Sum elements of matrix in rows
    Sum_Row_Matrix(row_m, col_m);
    cout << "\nSum elements of matrix in rows: " << endl;
    Show_Vector(row_m);
    //Transpose matrix
    Transpose_Matrix(&row_m, &col_m);
    cout << "\nTranspose Matrix: " << endl;
    Show_Matrix(row_m, col_m);
    _getch();
}
