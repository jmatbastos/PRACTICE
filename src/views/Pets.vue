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

export default {
    setup() {
		const adoptionsStore = useAdoptionsStore()
		const userStore = useUserStore()
        const petsStore = usePetsStore()		
		return { adoptionsStore, userStore,  petsStore}
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