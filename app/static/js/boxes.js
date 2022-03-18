console.log("hello");
currentRow = 0;
currentTile = 0;
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
  console.log(letter);
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

document.addEventListener("keyup", (e) =>{
  let letter = String(e.key);
  console.log("letter of keypressed " + letter)
  if(letter.equals("DELETE")){
    deleteLetter();
    return
  }else if(letter = "ENTER"){
    nextRow();
    return
  }else{
    addLetter(letter)
  }
})

const addLetter = (letter) => {
  if (currentTile < 5) {
    // console.log(currentRow + " " + currentTile);
    tile = document.getElementById("row#" + currentRow + "tile#" + currentTile);
    tile.textContent = letter;
    tile.setAttribute("color", letter);
    currentTile++;
  }
};

const nextRow = () => {
  guess = "";
  if (currentTile != 5) {
    console.log("not allwoed");
  }
  if (currentTile == 5) {
    for (var i = 0; i < 5; i++) {
      tile = document.getElementById("row#" + currentRow + "tile#" + i);
      guess = guess.concat("", tile.textContent);
    }
    console.log("GUESS: " + guess);
    currentRow++;
    currentTile = 0;
  }
  if (currentRow >= 5) {
    //new wordle
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
  createGrid(x);
}

function insertLetter() {}
$(document).ready(function () {
  createKeyboard();
  createGrid(6);
  $(".newGrid").click(function () {
    refreshGrid(6);
    console.log("newGrid");
  });
});
