// File: The 100 game
// program: A two player game in C++ where the goal
//         is to reach 100. Each player chooses from 0-10.
//         The first player to reach 100 wins.
// Author: Daad Amar Osman
// Date created : Feb 19,2024
// version : 2.0

#include <iostream>
using namespace std;
int main() {
    home:
//         Welcome Message for the players
    cout << "\n                               The 100 Game \n\n";
    cout << ""
            "          A two players game that starts from 0 and the goal is to \n"
            "          reach the sum of 100, each player alternatively adds a number \n"
            "          from 1 to 10 to the sum.The player who reaches 100 first wins.\n\n";

// The starting number and the target number

    int sum = 0, goal = 100, play;

// The Game

    while (sum < goal) {

        //Player 1 entry and validation
        cout << "\nPlayer 1: Enter a number from 1 - 10: ";
        cin >> play;
        while (play < 1 or play > 10) {
            cout << "Player 1: Enter a number from 1 - 10: ";
            cin >> play;
        }
        // Check if the sum is above the required Goal
        int temp = sum + play;
        while (temp > goal) {
            cout << "The sum must not exceed " << goal << "\n";
            cout << "Player 1: Enter a number from 1 - 10: ";
            cin >> play;
            temp = sum + play;
        }

        sum = sum + play;
        cout << "The Total is now " << sum << endl;
        if (sum >= goal) {
            cout << "\nPlayer 1 Is the Winner!!! \nGame Over \n";
            break;
        } else {
            cout << "";
        }

        //Player 2 entry and validation
        cout << "\nPlayer 2: Enter a number from 1 - 10: ";
        cin >> play;
        while (play < 1 or play > 10) {
            cout << "Player 2: Enter a number from 1 - 10: ";
            cin >> play;
        }
        temp = sum + play;
        while (temp > goal) {
            cout << "The sum must not exceed " << goal << "\n";
            cout << "Player 2: Enter a number from 1 - 10: ";
            cin >> play;
            temp = sum + play;
        }
        sum += play;
        cout << "The Total is now " << sum << endl;
        if (sum >= goal) {
            cout << "\nPlayer 2 Is the Winner!!! \nGame Over \n";
            break;
        } else {
            cout << "";
        }
    }
    int status;
    cout << "\nDo you want to play The 100 Game again ?(1 for yes/ 0 for no)   ";
    cin >> status;
    if (status != 1) {
        cout << "\nGoodbye ";

    }
    else
    {
        goto home;
    }


    return 0;
}

