
// function that will set up the value for playerMove, computerMove and result to be appear in the input forms 
// declaration of the variables for computerMove randomized moves and result as a function that takes as parameters playerMove (move) and computerMove
 function play(move) {
            document.getElementById('playerMove').value = move;
            const computerMove = computerChoice();
            document.getElementById('computerMove').value = computerMove;
            let result = determineWinner(move, computerMove);
            document.getElementById('result').value = result;
        }

// function to create random moves for the computer
function computerChoice() {
     let randomNumber = Math.random();
     // initializing the variable as an empty string to make sure no value is assigned at the beginning of the match
     let computerMove = '';    
     if ( randomNumber <= 1/3 ) {
       computerMove = "rock";
      } else if ( randomNumber <= 2/3 ) {
       computerMove = "paper";
      } else {
       computerMove = "scissors";
      }
       return computerMove;
      }  

// function to determine the winner of the match
function determineWinner(playerMove, computerMove) {
  let result;
     
     if (playerMove === computerMove) {
    result = "tie!";
  } else if ((playerMove === 'rock' && computerMove === 'scissors') ||
             (playerMove === 'paper' && computerMove === 'rock') ||
             (playerMove === 'scissors' && computerMove === 'paper')) {
    result = "you win!";
  } else {
    result = "you lose!";
  }
  return result;
}

// event listeners to handle buttons clicks and start the game
rock.addEventListener('click', function () {
  play('rock');
});

paper.addEventListener('click', function () {
  play('paper');
});

scissors.addEventListener('click', function () {
  play('scissors');

// function that will set up the value for playerMove, computerMove and result to be appear in the input forms 
// declaration of the variables for computerMove randomized moves and result as a function that takes as parameters playerMove (move) and computerMove
 function play(move) {
            document.getElementById('playerMove').value = move;
            const computerMove = computerChoice();
            document.getElementById('computerMove').value = computerMove;
            let result = determineWinner(move, computerMove);
            document.getElementById('result').value = result;
        }

// function to create random moves for the computer
function computerChoice() {
     let randomNumber = Math.random();
     // initializing the variable as an empty string to make sure no value is assigned at the beginning of the match
     let computerMove = '';    
     if ( randomNumber <= 1/3 ) {
       computerMove = "rock";
      } else if ( randomNumber <= 2/3 ) {
       computerMove = "paper";
      } else {
       computerMove = "scissors";
      }
       return computerMove;
      }  

// function to determine the winner of the match
function determineWinner(playerMove, computerMove) {
  let result;
     
     if (playerMove === computerMove) {
    result = "tie!";
  } else if ((playerMove === 'rock' && computerMove === 'scissors') ||
             (playerMove === 'paper' && computerMove === 'rock') ||
             (playerMove === 'scissors' && computerMove === 'paper')) {
    result = "you win!";
  } else {
    result = "you lose!";
  }
  return result;
}

// event listeners to handle buttons clicks and start the game
rock.addEventListener('click', function () {
  play('rock');
});

paper.addEventListener('click', function () {
  play('paper');
});

scissors.addEventListener('click', function () {
  play('scissors');
});
