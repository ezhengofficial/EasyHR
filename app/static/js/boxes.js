
console.log("hello");
function createGrid(x) {
    for (var rows = 0; rows < x; rows++) {
        for (var columns = 0; columns < x; columns++) {
            $("#grid-container").append("<div class='grid'></div>");
        };
    };
    $(".grid").width(500/x);
    $(".grid").height(500/x);
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
