// import { guesslist } from "./guesslist";
let word = "";

function sendUserInfo(data) {
  fetch("/getdata", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    // A JSON payload
    body: JSON.stringify({
      data,
    }),
  })
    .then(function (response) {
      // At this point, Flask has printed our JSON
      return response.text();
    })
    .then(function (text) {
      //   console.log("POST response: ");

      // Should be 'OK' if everything was successful
      console.log(text);
    });
}

fetch("/getword", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },

  // A JSON payload
  body: JSON.stringify({
    word,
  }),
})
  .then(function (response) {
    // At this point, Flask has printed our JSON
    return response.text();
  })
  .then(function (text) {
    // console.log("Word: ");

    // Should be 'OK' if everything was successful
    console.log(text);
    word = text;
  });

// console.log("hello");
currentRow = 0;
currentTile = 0;
//change to sync w python

function createGrid(x) {
  //   console.log(board);
  let board = document.getElementById("grid-container");

  for (var rows = 0; rows < x; rows++) {
    let row = document.createElement("div");
    row.setAttribute("id", "row#" + rows);
    row.className = "row";
    for (var columns = 0; columns < 5; columns++) {
      let tile = document.createElement("div");
      tile.setAttribute("id", "row#" + rows + "tile#" + columns);
      tile.setAttribute("color", "lightgray");
      tile.className = "grid";
      row.appendChild(tile);
    }
    board.appendChild(row);
  }
  // $(".grid").width(500/x);
  // $(".grid").height(500/x);
}

function createKeyboard() {
  keys.forEach((key) => {
    let keyboard = document.getElementById("key-container");
    let buttonElement = document.createElement("button");
    buttonElement.setAttribute("id", "key#" + key);
    buttonElement.setAttribute("class", "key");

    buttonElement.textContent = key;
    // console.log(buttonElement.textContent);
    // buttonElement.setAttribute("id", key);
    buttonElement.addEventListener("click", () => clicky(key));
    keyboard.appendChild(buttonElement);
  });
}
const keys = [
  "Q",
  "W",
  "E",
  "R",
  "T",
  "Y",
  "U",
  "I",
  "O",
  "P",
  "A",
  "S",
  "D",
  "F",
  "G",
  "H",
  "J",
  "K",
  "L",
  "ENTER",
  "Z",
  "X",
  "C",
  "V",
  "B",
  "N",
  "M",
  "DELETE",
];

function clicky(letter) {
  // console.log(letter);
  //   addLetter(letter);
  if (letter == "DELETE") {
    deleteLetter();
    return;
  } else if (letter == "ENTER") {
    nextRow();
    return;
  } else {
    addLetter(letter);
  }
}

document.addEventListener("keyup", (e) => {
  let letter = String(e.key).toUpperCase();
  // console.log("letter of keypressed " + letter)
  // console.log("true?" + letter==="S")
  if (letter === "DELETE" || letter === "BACKSPACE") {
    deleteLetter();
  } else if (letter === "ENTER") {
    nextRow();
  } else {
    if (letter.length == 1 && letter.match(/[a-z]/i)) {
      addLetter(letter);
      // console.log("added letter");
    }
  }
});
const colorChange = (input) => {
  var green = "";
  inputChange = word;
  for (let i = 0; i < input.length; i++) {
    // console.log("word[i] " + word[i] + " --input[i] " + input[i]);
    tile = document.getElementById("row#" + currentRow + "tile#" + i);
    button = document.getElementById("key#" + input[i].toUpperCase());
    if (word[i] === input[i]) {
      //   console.log("match");
      // console.log("word " + word[i]);
      green = green.concat("", word[i]).toLowerCase();
      //   console.log("green " + green);
      //tile.textContent = "g";
      tile.setAttribute("style", "background-color: #538d4e");
      inputChange = inputChange.replace(input[i], "");
      console.log("after relacement: " + inputChange + " at position " + i);
      // tile.color = "abc"
      //change textContent to datatype and then match data type to word color
    } else {
      tile.setAttribute("style", "background-color: gray");
      button.setAttribute("style", "background-color: #A9A9A9");
    }
  }

  for (let i = 0; i < input.length; i++) {
    str = tile.getAttribute("style");
    // if !(str ===);
    console.log(input.length);
    if (inputChange.includes(input[i])) {
      tile = document.getElementById("row#" + currentRow + "tile#" + i);

      console.log("changed?: " + inputChange);
      console.log("the word has: " + input[i] + " at position " + i);
      //tile.textContent = "y";
      inputChange = inputChange.replace(word[i], "");
      tile.setAttribute("style", "background-color: #b59f3b");
    }
  }

  //   if (input === word) {
  //     console.log("input=word");
  //   }
};

const addLetter = (letter) => {
  if (currentTile < 5) {
    // console.log(currentRow + " " + currentTile);
    tile = document.getElementById("row#" + currentRow + "tile#" + currentTile);
    tile.textContent = letter;
    // tile.setAttribute("color", letter);
    currentTile++;
  }
};

const nextRow = () => {
  input = "";
  if (currentTile != 5) {
    // console.log("not allowed");
    alert("Word must be 5 letters long");
  }
  if (currentTile == 5) {
    for (var i = 0; i < 5; i++) {
      // console.log(i);
      tile = document.getElementById("row#" + currentRow + "tile#" + i);
      console.log(tile.textContent);
      input = input.concat("", tile.textContent).toLowerCase();
    }
    console.log(input);
    // console.log(guesslist);
    if (guesslist.includes(input)) {
      sendUserInfo(input);
      colorChange(input);
      if (input == word) {
        alert("Congrats, you win!");
      } else {
        currentRow++;
        currentTile = 0;
      }
    } else {
      console.log("not in wordlist");
      alert("Not a Word");
      return;
    }
  }

  //   console.log(input);
  if (currentRow >= 6) {
    alert("Game Over! Try again!");
  }
};

const deleteLetter = () => {
  if (currentTile > 0) {
    currentTile--;
    tile = document.getElementById("row#" + currentRow + "tile#" + currentTile);
    tile.textContent = "";
    tile.setAttribute("color", letter);
  }
};
function refreshGrid(x) {
  $(".grid").remove();
  currentRow = 0;
  currentTile = 0;
  createGrid(x);
}

function insertLetter() {}
$(document).ready(function () {
  createKeyboard();
  createGrid(6);
  $(".newGrid").click(function () {
    refreshGrid(6);
    // console.log("newGrid");
  });
});
