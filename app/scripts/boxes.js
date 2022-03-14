function createGrid(x) {
    for (var rows = 0; rows < x; rows++) {
        for (var columns = 0; columns < x; columns++) {
            $("#grid-container").append("<div class='grid'></div>");
        };
    };
    $(".grid").width(960/x);
    $(".grid").height(960/x);
};
$(document).ready(function() {
    createGrid(6);
  });
