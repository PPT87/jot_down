const card = document.getElementById("card");
let removeCompleteBtn = document.getElementById("removeCompleteBtn");
let checkCircle = document.getElementById("check-circle");

document.getElementById("removeCompleteBtn").addEventListener("click", removeComplete);

function removeComplete() {
    if (checkCircle = True){
      card.remove()
    }
  }