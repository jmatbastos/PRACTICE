<template>
<div>


  
<Header />




				
	



<Footer />

</div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Header from '@/components/Header.vue'

import { useAdoptionsStore } from '@/store/adoptions'
import { useUserStore } from '@/store/user'
import { usePetsStore } from '@/store/pets'
import { usePetCategoriesStore } from '@/store/petcategories'

export default {
    setup() {
		const adoptionsStore = useAdoptionsStore()
		const userStore = useUserStore()
        const petsStore = usePetsStore()	
        const petCategoriesStore = usePetCategoriesStore()	        	
		return { adoptionsStore, userStore,  petsStore, petCategoriesStore }
  	}, 
    components: {
        Footer,
        Header
    },
  

    data() {
        return {
        }
    },
    created() {
    },
    methods: {       
        

       
    },
    computed: {
        
    }
 
}
</script>

<style scoped>


</style>