
console.log("hello");
function createGrid(x) {
  let board = document.getElementById("grid-container");

    for (var rows = 0; rows < x; rows++) {
      let row = document.createElement("div");
      row.className = "row";
        for (var columns = 0; columns < 5; columns++) {
          let box = document.createElement("div");
          box.className = "grid";
          row.appendChild(box);
        };
        board.appendChild(row)
    };
    // $(".grid").width(500/x);
    // $(".grid").height(500/x);
};


function refreshGrid(x){
  $(".grid").remove();
  createGrid(x)
}
$(document).ready(function() {
    createGrid(6);
    $(".newGrid").click(function(){
      refreshGrid(6);
      console.log("newGrid");
    });
  });
