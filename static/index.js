const totalPlayers = 6;

function fillGrid(){
    var doc = document.getElementsByClassName('grid-container');
    for(var i = 0; i < totalPlayers; i++){
      var next = document.createElement('button');
      //next.setAttribute('class', 'present');
      setAttributes(next, {'id':String('section'+i), 'class':'section'});
      next.onclick = click;
      doc.insertAdjacentElement('beforeend', next);
    }
  }

function setAttributes(next, attrs){
    for(var key in attrs){
        next.setAttribute(key, attrs[key]);
    }
}

function click(e) {
    e.target.classList.add("open-present")