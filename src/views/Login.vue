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

export default {
	setup() {
		const adoptionsStore = useAdoptionsStore()
		const userStore = useUserStore()		
		return { adoptionsStore, userStore }
  	}, 
    components: {
        Footer,
        Header
    },
    data() {
        return {
            email: '',
            password: '', 
            alertMessageStyle: 'display:none;'      
        }
    },
    mounted() {
    },
    methods: {    
   
    },
    computed: {
                       
    },
}
</script>