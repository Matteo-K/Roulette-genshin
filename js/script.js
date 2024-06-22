let detailChar_AR = [];
let defaultChar_AR = [];

let detailBoss_AR = [];
let defaultBoss_AR = [];

/* Gère les différents onglets */
function tabMenu(event, section) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabContent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.querySelectorAll(".tabLink");
    tablinks.forEach(element => {
        element.classList.remove("active");
    });
    document.getElementById(section).style.display = "block";
    event.currentTarget.classList.add("active");
    const main = document.querySelector("main");
    main.style.backgroundImage = "url(images/background_"+section+".png)";
}

/* Ouvre et ferme le menu des listes */
let menuOpen = 0;
function openMenuCharacter(event) {
  const aside = document.querySelector("aside");
  const btnChar = document.querySelector(".btnCharacter");
  if (menuOpen%2 == 0) {
    event.currentTarget.style.backgroundColor = "white";
    aside.style.transform = "translateX(0%)";
    btnChar.style.top = "85vh";
  } else {
    event.currentTarget.style.backgroundColor = "#444";
    event.currentTarget.style.filter = "drop-shadow(3px 3px 3px black)";
    aside.style.transform = "translateX(100%)";
    btnChar.style.top = "70vh";
  }
  menuOpen++;
}

/* Renvoie un nombre aléatoire entre 0 et max-1
Exemple : max = 3; 0, 1 ou 2 */
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

/**
 * 
 * @param {Array} array 
 * @param {Integer} N 
 * @returns renvoie une liste de N personnes d'une liste sélectionner. Si la taille de la liste est est inférieur à N alors, il renvoie une erreur.
 */
function genNChar(array,N) {
  let AR_char = [];
  let randomValue;
  while (AR_char.length < N) {
    randomValue = getRandomInt(array.length);
    if (!AR_char.includes(array[randomValue])) {
      AR_char.push(array[randomValue]);
    }
  }
  return AR_char;
}

/* Génère l'aléatoire des abyss */
function genAbyss() {
  const composants = document.querySelectorAll(".part_abyss img, .part_abyss figcaption");
  let size_ = 8;
  let size_ARChar = detailChar_AR.length;
  let res = genNChar(defaultChar_AR, size_);
  let stop, id;
  
  for (let index = 0; index < size_ * 2; index += 2) {
    stop = true;
    id = 0;
    
    while (stop && id < size_ARChar) {
      if (res[index / 2] === detailChar_AR[id].name) {
        stop = false;
        composants[index].src = "images/genshin/perso/" + detailChar_AR[id].img;
        composants[index].alt = detailChar_AR[id].name;
        composants[index + 1].textContent = detailChar_AR[id].name;
      }
      id++;
    }
  }
}

function genBoss() {
  const composants = document.querySelectorAll("#boss img, #boss figcaption");
  let size_ = 1;
  let size_ARBoss = detailBoss_AR.length;
  let res = genNChar(defaultBoss_AR, size_);
  let stop, id;
  
  for (let index = 0; index < size_ * 2; index += 2) {
    stop = true;
    id = 0;
    
    while (stop && id < size_ARBoss) {
      if (res[index / 2] === detailBoss_AR[id].name) {
        stop = false;
        composants[index].src = "images/genshin/" + detailBoss_AR[id].img;
        composants[index].alt = detailBoss_AR[id].name;
        composants[index + 1].textContent = detailBoss_AR[id].name;
      }
      id++;
    }
  }
}
  
/* ### Open File ### */
async function openFile() {
  let [findHandle] = await window.showOpenFilePicker();
  let fileData = await findHandle.getFile();
  let text = await fileData.text();
  console.log(text);
}

fetch("lstPersoGenshin.json")
  .then(res => {
    if (res.ok) {
      res.json().then(data => {
        data.forEach(element => {
          detailChar_AR.push(element)
          defaultChar_AR.push(element.name)
        });
      })
    } else {
      
    }
  });

  fetch("lstBossGenshin.json")
  .then(res => {
    if (res.ok) {
      res.json().then(data => {
        data.forEach(element => {
          detailBoss_AR.push(element)
          defaultBoss_AR.push(element.name)
        });
      })
    } else {
      
    }
  });