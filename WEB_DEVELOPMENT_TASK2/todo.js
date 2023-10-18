const inputBox=document.getElementById("inputbox");
const toDo=document.getElementById("to-do-list");
function addTask(){
  if(inputBox.value === ''){
    alert("You must write something!");
  }
  else{
    let j=0;
    let li=document.createElement("li");
    li.innerHTML=inputBox.value;
    toDo.appendChild(li);
    let span=document.createElement("span");
    span.innerHTML="\u00d7";
    li.appendChild(span);
  }
  inputBox.value='';
  saveData();
}
toDo.addEventListener("click", function(e){
  if(e.target.tagName==="LI"){
    e.target.classList.toggle("checked");
    saveData();
  }
  else if(e.target.tagName==="SPAN"){
    e.target.parentElement.remove();
    saveData();
  }
}, false);
function saveData(){
  localStorage.setItem("data", toDo.innerHTML)
}
function showTask(){
  toDo.innerHTML=localStorage.getItem("data")
}
showTask();