class ListeGenshin {
    constructor() {
        this.array = [];
      }
    constructor(name_, array_) {
      this.array = [{name : name_, array : array_}];
    }

    add(name, array) {
        this.array.push({name : name, array : array})
    }

    remove(name_) {
        this.array.forEach(element => {
            if (element.name === name_) {
                // Supprimerl'élément
            }
        });
    }
}
  
const storageChar = new ListeGenshin("Par défaut", defaultChar_AR);
const storageBoss = new ListeGenshin("Par défaut", defaultBoss_AR);