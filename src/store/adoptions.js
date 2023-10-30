import { defineStore } from 'pinia'

export const useAdoptionsStore = defineStore({
  id: 'adoptions',
  state: () => ({
    adoptions: 
    [
    //{
    //"id":"11",
    //"created_at":"2021-12-03 18:20:31", 
     //"pet_name":"Doggy",
     //"pet_image":"dg1.jpg",     
    //}
    ]
  }),
  getters: {
    getadoptions (state) {
      return state.adoptions
    },   
  }, 
    actions: {
      addadoptions(adoptions){
        this.adoptions = adoptions
      },
      newAdoption(order){
        this.adoptions = [order, ...this.adoptions]
      },  
    async getMyadoptionsDB(id) {
            try {
                const response = await fetch(`http://daw.deei.fct.ualg.pt/~a12345/PRACTICE/api/adoptions.php?petlover_id=${id}`)
                const data = await response.json()
                console.log('received data:', data)                
                this.addadoptions(data)
                return true
            } 
            catch (error) {
              console.log('error: ', error)
              return false
            }
        },
    async newAdoptionDB(newAdoption) {         
          try {
              const response = await fetch('http://daw.deei.fct.ualg.pt/~a12345/PRACTICE/api/adoptions.php', {
                  method: 'POST',
                  body: JSON.stringify(newAdoption),
                  headers: { 'Content-type': 'text/html; charset=UTF-8' },
              })
              const data = await response.json()
              console.log('received data:', data)
              this.newAdoption(data)
              return true
          } 
          catch (error) {
              console.error(error)
              return false
          }
      },     
  },
})
