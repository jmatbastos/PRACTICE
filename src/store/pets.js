 
import { defineStore } from 'pinia'

export const usePetsStore = defineStore({
  id: 'pets',
  state: () => ({
    pets: [
//      {
//        "id":"1",
//        "name":"Max",
//        "cat_id":"1",
//        "cat_name":"Dogs",
//        "description":"So full of life",
//        "status":"NULL",      
//        "image":"dg1.jpg"
//      },
    ]
  }),
  getters: {
    getpets (state) {
      return state.pets;
    },
    getPetsByCat: (state) => (id) => {
      const results = state.pets.filter(p => {
          return p.cat_id == id;
      })
      return results
    },
    getPetByID: (state) => {
      return (id) => state.pets.filter((p) => p.id === id)
    },     
  }, 
  actions: {
    addpets(pets){
      this.pets = pets
    },  
    async getPetsDB() {
            try {
                const response = await fetch('http://daw.deei.fct.ualg.pt/~a12345/PRACTICE/api/pets.php')
                const data = await response.json()
                console.log('received data:', data)                
                this.addpets(data)
                return true
            } 
            catch (error) {
                console.log('error: ', error)
                return false
            }
        },
  },
})