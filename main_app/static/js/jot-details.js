/*------------------------ Cached Element References ------------------------*/
const jotBtn = document.getElementById('button-addon2')


/*----------------------------- Event Listeners -----------------------------*/
//document.getElementById('jotBtn').addEventListener('click', addJot)


/*----------------------------- Functions -----------------------------*/

function addJot(){
  console.log('this is working')
  document.getElementById('button-addon2').innerText = "Jot Added!"

  clearTimeout(timeout)
  timeout = setTimeout(function(){
    jotBtn.innerHTML = 'Jot Down!'
  }, 2000);
}
