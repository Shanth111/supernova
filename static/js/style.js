
function move() {
    var elem = document.getElementById("myBar");   
    var width = 0;
    var id = setInterval(frame, 40);
    function frame() {
      if (width >= 80) {
        clearInterval(id);
      } else {
        width++; 
        elem.style.width = width + '%'; 
        elem.innerHTML = width * 1  + '%';
      }
    }
  }