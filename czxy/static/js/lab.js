function onload() {
    var defa=1;
    var td = document.getElementById('td');
    var rowObj=null;
  for (var i; i<3;i++){
        rowObj= row[i];
        for (var j=1;j<7;j++){
            var s = rowObj.cells[j].innerHTML;

            if (s >= defa){
                rowObj.cells[j].style.backgroundColor = "red";

            }
        }
  }
}