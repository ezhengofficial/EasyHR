console.log("hello");
currentRow = 0;
currentTile = 0;
word = "hello";
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

document.addEventListener("keyup", (e) =>{
  let letter = String(e.key).toUpperCase();
  // console.log("letter of keypressed " + letter)
  // console.log("true?" + letter==="S")
  if(letter==="DELETE" || letter === "BACKSPACE"){
    deleteLetter();
  }else if(letter==="ENTER"){
    nextRow();
  }else{
    if(letter.length == 1 && letter.match(/[a-z]/i)){
      addLetter(letter);
      // console.log("added letter");
    }

  }
})
const colorChange = (input) =>{
  var green = ""
  for(let i = 0; i < input.length; i++){
    // console.log("word[i] " + word[i] + " --input[i] " + input[i]);
    if(word[i] === input[i]){
      console.log("match");
      // console.log("word " + word[i]);
      green = green.concat("", word[i]).toLowerCase();
      console.log("green " + green);
      tile = document.getElementById("row#" + currentRow + "tile#" + i);
      tile.textContent = "g";
      // tile.color = "abc"
      //change textContent to datatype and then match data type to word color
    }
  }
  if (input===word){
    console.log("input=word");
  }
};
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
  input = "";
  if (currentTile != 5) {
    console.log("not allwoed");
  }
  if (currentTile == 5) {
    for (var i = 0; i < 5; i++) {
      tile = document.getElementById("row#" + currentRow + "tile#" + i);
      input = input.concat("", tile.textContent).toLowerCase();

    currentRow++;
    currentTile = 0;
    $.ajax({
      url:'/',
      type: 'POST',
      data: JSON.stringify(input),
    })
    .done(function(result){
      console.log(result)
    })
  }
  console.log(input);
  colorChange(input);
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
    console.log("newGrid");
  });
});
