     
const x = document.querySelector("#myTopnav");
const y  = document.querySelector(".icon");
const k  = document.querySelector(".dropbtn");
const m  = document.querySelector(".dropdown-content");

 y.onclick = ()=>{
    
  if(x.className === "topnav"){
        x.className += " responsive";
}else{
        x.className = "topnav";
}
    
}

k.onmouseenter = ()=>{

  if (m.style.display === 'none'){
    m.style.display = 'block';
    m.style.position = 'fixed';
   
  }else{
   m.style.display = 'none';
  }
 
}

    
